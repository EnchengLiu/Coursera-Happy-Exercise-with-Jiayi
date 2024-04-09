#! /usr/bin/env python

import rospy
from geometry_msgs.msg import PoseStamped
from std_msgs.msg import Header
from intera_core_msgs.srv import SolvePositionIK, SolvePositionIKRequest

# import custom grasp planner from 206B proj4_pkg
from proj4_pkg import grasping


def ik_service_client():
    service_name = "ExternalTools/right/PositionKinematicsNode/IKService"
    ik_service_proxy = rospy.ServiceProxy(service_name, SolvePositionIK)
    ik_request = SolvePositionIKRequest()
    header = Header(stamp=rospy.Time.now(), frame_id='base')

    # Create a PoseStamped and specify header (specifying a header is very important!)
    pose_stamped = PoseStamped()
    pose_stamped.header = header

    # Set end effector position: YOUR CODE HERE
    # typein=[]
    # for i in range(3):
    #     print("please in put the coordinate")
    #     typein.append(input())
    
    

    #Given object
    obj = 'nozzle' # should be 'pawn' or 'nozzle'.
    
    # mesh = trimesh.Trimesh(vertices=vertices, faces=poses, vertex_normals=normals)
    print("Visualize planning for the pawn object")
    vertices, normals, poses, results = grasping.load_grasp_data(obj)
    mesh = grasping.load_mesh(obj)
    
    for v, p in zip(vertices, poses):
        visualize_grasp(mesh, v, p)

    # you may or may not find the code below helpful:) i was supposed to delete this from the starter code but i didn't so enjoy
    print("Grasp planning for the pawn object")
    v_and_p = [custom_grasp_planner(mesh, v) for v in vertices]
    
    #getting new pose from custom grasp planner
    # (4x4 np.ndarray): The rigid transform for the desired pose of the gripper, in the object's reference frame.
    new_pose=grasping.custom_grasp_planner()
    
    
    
    
    # pose_stamped.pose.position.z = float(typein[2])
    pose_stamped.pose.position.x = 0.739
    pose_stamped.pose.position.y = 0.179
    pose_stamped.pose.position.z = -0.107
    
    # Set end effector quaternion: YOUR CODE HERE
    pose_stamped.pose.orientation.x = 0.0
    pose_stamped.pose.orientation.y = 1.0
    pose_stamped.pose.orientation.z = 0.0
    pose_stamped.pose.orientation.w = 0.0
    
    # Add desired pose for inverse kinematics
    ik_request.pose_stamp.append(pose_stamped)
    # Request inverse kinematics from base to "right_hand" link
    ik_request.tip_names.append('right_hand')

    rospy.loginfo("Running Simple IK Service Client example.")

    try:
        rospy.wait_for_service(service_name, 5.0)
        response = ik_service_proxy(ik_request)
    except (rospy.ServiceException, rospy.ROSException) as e:
        rospy.logerr("Service call failed: %s" % (e,))
        return

    # Check if result valid, and type of seed ultimately used to get solution
    if (response.result_type[0] > 0):
        rospy.loginfo("SUCCESS!")
        # Format solution into Limb API-compatible dictionary
        limb_joints = dict(list(zip(response.joints[0].name, response.joints[0].position)))
        rospy.loginfo("\nIK Joint Solution:\n%s", limb_joints)
        rospy.loginfo("------------------")
        rospy.loginfo("Response Message:\n%s", response)
    else:
        rospy.logerr("INVALID POSE - No Valid Joint Solution Found.")
        rospy.logerr("Result Error %d", response.result_type[0])
        return False

    return True


def main():
    rospy.init_node("ik_service_client")

    ik_service_client()

if __name__ == '__main__':
    main()
