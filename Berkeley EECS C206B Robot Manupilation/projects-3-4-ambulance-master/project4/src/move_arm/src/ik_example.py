#!/usr/bin/env python
import rospy
from intera_interface import gripper as robot_gripper
from moveit_msgs.srv import GetPositionIK, GetPositionIKRequest, GetPositionIKResponse
from geometry_msgs.msg import PoseStamped
from moveit_commander import MoveGroupCommander
import numpy as np
from numpy import linalg
import sys
import tf.transformations as tf_trans


# import custom grasp planner from 206B proj4_pkg
from proj4_pkg import grasping

def main(): 
    # Wait for the IK service to become available
    rospy.wait_for_service('compute_ik')
    rospy.init_node('service_query')
    # Create the function used to call the service
    compute_ik = rospy.ServiceProxy('compute_ik', GetPositionIK)
    # Set up the right gripper
    right_gripper = robot_gripper.Gripper('right_gripper')    
    while not rospy.is_shutdown():
        # input('Press [ Enter ]: ')
        
        # Construct the request
        request = GetPositionIKRequest()
        request.ik_request.group_name = "right_arm"

        # If a Sawyer does not have a gripper, replace '_gripper_tip' with '_wrist' instead
        link = "right_gripper_tip"

        request.ik_request.ik_link_name = link
        # request.ik_request.attempts = 20
        request.ik_request.pose_stamped.header.frame_id = "base"
        
        
        
        #Given object
        obj = 'nozzle' # should be 'pawn' or 'nozzle'.
        
        # mesh = trimesh.Trimesh(vertices=vertices, faces=poses, vertex_normals=normals)
        print("Visualize planning for the pawn object")
        vertices, normals, poses, results = grasping.load_grasp_data(obj)
        mesh = grasping.load_mesh(obj)
        
        for v, p in zip(vertices, poses):
            grasping.visualize_grasp(mesh, v, p)




        #how to change the pose from object's reference frame to the robot r
        '''
        - Translation: [0.744, 0.175, -0.132]
        - Rotation: in Quaternion [0.034, 0.996, -0.031, 0.080]
                    in RPY (radian) [-3.084, 0.163, 3.078]
                    in RPY (degree) [-176.674, 9.320, 176.383]
        '''
        object_pose_translation = np.array([0.744, 0.175, -0.132])
        object_pose_rotation = tf_trans.quaternion_matrix([0.034, 0.996, -0.031, 0.080])

        # Combine the translation and rotation into a single 4x4 transformation matrix
        object_pose_in_base_link = np.dot(tf_trans.translation_matrix(object_pose_translation), object_pose_rotation)




        # you may or may not find the code below helpful:) i was supposed to delete this from the starter code but i didn't so enjoy
        print("Grasp planning for the pawn object")
        for v in vertices:
            print("Grasp planning for vertex: ", v)
            #getting new pose from custom grasp planner
            # (4x4 np.ndarray): The rigid transform for the desired pose of the gripper, in the object's reference frame.
            new_pose=grasping.custom_grasp_planner()
            print(new_pose)
            # Get the new pose in the object's frame

            # Assume new_pose is a 4-element array [x, y, z, 1]. If not, you need to convert it to this format.
            # Then, transform the new pose to the base_link frame
            new_pose_in_base_link_frame = np.dot(object_pose_in_base_link, new_pose)
            print(new_pose_in_base_link_frame)
        
        
        
        
        # Set the desired orientation for the end effector HERE
        request.ik_request.pose_stamped.pose.position.x = 0.739
        request.ik_request.pose_stamped.pose.position.y = 0.179
        request.ik_request.pose_stamped.pose.position.z = -0.107       
        request.ik_request.pose_stamped.pose.orientation.x = 0.0
        request.ik_request.pose_stamped.pose.orientation.y = 1.0
        request.ik_request.pose_stamped.pose.orientation.z = 0.0
        request.ik_request.pose_stamped.pose.orientation.w = 0.0


        
        try:
            # Send the request to the service
            response = compute_ik(request)
            
            # Print the response HERE
            print(response)
            group = MoveGroupCommander("right_arm")

            # Setting position and orientation target
            group.set_pose_target(request.ik_request.pose_stamped)

            # TRY THIS
            # Setting just the position without specifying the orientation
            ###group.set_position_target([0.5, 0.5, 0.0])

            #Plan IK
            plan = group.plan()
            user_input = input("Enter 'y' if the trajectory looks safe on RVIZ")
            
            right_gripper.open()
            #Execute IK if safe
            if user_input == 'y':
                group.execute(plan[1])
                right_gripper.close()
            
        except rospy.ServiceException as e:
            print("Service call failed: %s"%e)

    
        try:
            # Set the desired orientation for the end effector HERE
            request.ik_request.pose_stamped.pose.position.x = 0.739
            request.ik_request.pose_stamped.pose.position.y = 0.179
            request.ik_request.pose_stamped.pose.position.z = 0      
            request.ik_request.pose_stamped.pose.orientation.x = 0.0
            request.ik_request.pose_stamped.pose.orientation.y = 1.0
            request.ik_request.pose_stamped.pose.orientation.z = 0.0
            request.ik_request.pose_stamped.pose.orientation.w = 0.0
            
            # Send the request to the service
            response = compute_ik(request)
            
            # Print the response HERE
            print(response)
            group = MoveGroupCommander("right_arm")

            # Setting position and orientation target
            group.set_pose_target(request.ik_request.pose_stamped)

            # TRY THIS
            # Setting just the position without specifying the orientation
            ###group.set_position_target([0.5, 0.5, 0.0])

            #Plan IK
            plan = group.plan()
            user_input = input("Enter 'y' if the trajectory looks safe on RVIZ")
            

            #Execute IK if safe
            if user_input == 'y':
                group.execute(plan[1])

            
        except rospy.ServiceException as e:
            print("Service call failed: %s"%e)
# Python's syntax for a main() method
if __name__ == '__main__':
    main()
