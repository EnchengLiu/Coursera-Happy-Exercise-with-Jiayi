#!/usr/bin/env python -W ignore::DeprecationWarning
"""
Starter code for EE106B grasp planning project.
Author: Amay Saxena, Tiffany Cappellari
Modified by: Kirthi Kumar
"""
# may need more imports
import numpy as np
from utils import *
from utils import adj
import utils
import math
import trimesh
import vedo
import sys
from scipy.spatial import ConvexHull

MAX_GRIPPER_DIST = 0.075
MIN_GRIPPER_DIST = 0.03
GRIPPER_LENGTH = 0.105

import cvxpy as cvx # suggested, but you may change your solver to anything you'd like (ex. casadi)



def compute_force_closure(vertices, normals, num_facets, mu, gamma, object_mass):
    """
    Compute the force closure of some object at contacts, with normal vectors 
    stored in normals. Since this is two contact grasp, we are using a basic algorithm
    wherein a grasp is in force closure as ling as the line connecting the two contact
    points lies in both friction cones.

    Parameters
    ----------
    vertices (2x3 np.ndarray): obj mesh vertices on which the fingers will be placed
    normals (2x3 np.ndarray): obj mesh normals at the contact points
    num_facets (int): number of vectors to use to approximate the friction cone, vectors 
        will be along the friction cone boundary
    mu (float): coefficient of friction
    gamma (float): torsional friction coefficient
    object_mass (float): mass of the object

    Returns
    -------
    (float): quality of the grasp
    """
     # calculate slope vector between points
    slope = normalize(vertices[0] - vertices[1])

    score = 0

    # print("Vertices: ", vertices)
    # print("Normals: ", normals)
    
    # for each point
    for i in range(len(vertices)):
        
        # find angle of line with surface of object at the particular contact point
        # <x, y> = ||x||||y|| cos(th)
        line_angle = min(np.arccos(np.dot(normals[i], slope)), np.arccos(np.dot(normals[i], -slope)))


        # find the angle of the friction cone at the same point
        cone_angle = np.arctan(mu)
        # print("Line angle: ", line_angle)
        # if the line angle is greater than the cone angle, then not force closure
        if line_angle > cone_angle:
            return 0
    return 1






def get_grasp_map(vertices, normals, num_facets, mu, gamma):
    """ 
    Defined in the book on page 219. Compute the grasp map given the contact
    points and their surface normals

    Parameters
    ----------
    vertices (2x3 np.ndarray): obj mesh vertices on which the fingers will be placed
    normals (2x3 np.ndarray): obj mesh normals at the contact points
    num_facets (int): number of vectors to use to approximate the friction cone, vectors 
        will be along the friction cone boundary
    mu (float): coefficient of friction
    gamma (float): torsional friction coefficient

    Returns
    -------
    (np.ndarray): grasp map
    """
    B = np.matrix([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 1]]).T
    
    #Initialize grasp map
    grasp_map = None
    # print("Vertices: ", vertices)
    # print("Normals: ", normals)
    adj=None
    
    def adjoint(g):
            # print("g: ", g)
            R = g[:3, :3]  # rotation part of g
            p = g[:3, 3]  # translation part of g

            # print("R: ", R)

            # Skew-symmetric matrix for cross product
            p1=p[0, 0]
            p2=p[1, 0]
            p3=p[2, 0]
            # print("p1: ", p1, "p2: ", p2, "p3: ", p3)

            p_hat = np.array([[0, -p3, p2], [p3, 0, -p1], [-p2, p1, 0]])

            adj_g = np.block([[R, np.dot(p_hat, R)], [np.zeros((3, 3)), R]])

            return adj_g
    adj_g=None
    for i in range(len(vertices)):
        translation = vertices[i]
        # print("Translation: ", translation)
        original_axis = np.array([0, 0, 1])
        final_axis = normals[i]

        # Calculate rotation matrix
        cross_axis = np.cross(original_axis, final_axis)
        skew_symmetic_matrix = np.matrix([[0, -cross_axis[2], cross_axis[1]],[cross_axis[2], 0, -cross_axis[0]], [-cross_axis[1], cross_axis[0], 0]])
        
        #Using Rodrigues' formula
        costheta = np.dot(original_axis, final_axis) / (np.linalg.norm(original_axis)*np.linalg.norm(final_axis))
        rotation = np.eye(3) + np.sin(np.arccos(costheta)) * skew_symmetic_matrix + np.dot(skew_symmetic_matrix, skew_symmetic_matrix)*costheta

        g = np.vstack((rotation, np.array([0, 0, 0])))
        c = np.vstack((np.matrix(translation).T, np.array([1])))
        g = np.hstack((g, c))
        
        adj_g = adjoint(g)

        # print("shape of adj: ", adj.shape, "shape of g: ", g.shape)
        if grasp_map is None:
            grasp_map = np.dot(adj_g, B.T)
            # print("111shape of grasp map: ", grasp_map.shape)
        else:
            grasp_map = np.hstack((grasp_map, np.dot(adj_g, B.T)))
        # print("222shape of grasp map: ", grasp_map.shape)
        # print("Grasp map: ", grasp_map)
    return grasp_map



def contact_forces_exist(vertices, normals, num_facets, mu, gamma, desired_wrench):
    """
    Compute whether the given grasp (at contacts with surface normals) can produce 
    the desired_wrench. Will be used for gravity resistance. 

    Parameters
    ----------
    vertices (2x3 np.ndarray): obj mesh vertices on which the fingers will be placed
    normals (2x3 np.ndarray): obj mesh normals at the contact points
    num_facets (int): number of vectors to use to approximate the friction cone, vectors 
        will be along the friction cone boundary
    mu (float): coefficient of friction
    gamma (float): torsional friction coefficient
    desired_wrench (np.ndarray):potential wrench to be produced

    Returns
    -------
    (bool): whether contact forces can produce the desired_wrench on the object
    """
    # YOUR CODE HERE
    



    # # YOUR CODE HERE
    grasp_map = get_grasp_map(vertices, normals, num_facets, mu, gamma)
    if num_facets<1:
        return 0
    A = np.empty((2, 0))  # Initialize an empty 2x0 matrix
    # print("Num facets: ", num_facets)
    num_facets=int(num_facets)
    for i in range(num_facets):
        angle = i * 2 * np.pi / num_facets
        vector = np.array([[np.cos(angle)], [np.sin(angle)]])  # 2x1 vector
        #denote the cordiantes of the cone vertices
        A = np.hstack((A, vector))  # Horizontally stack the new vector
    
    #A is a 2xnum_facets matrix
    
    
    # Define the variables
    #Matrix B is 6*4
    #adj_g is 6*6
    #grasp_map is 6*8
    #desired_wrench is 6*1
    #So, fc is 8*1
    # grasp_map@fc is 6*1
    
    
    #low case f is the frictional force
    fc = cvx.Variable((8, 1))
    #this contains two f1 f2 f3 f4, one for force 1 and one for force 2
    
    b1 = cvx.Variable((1+num_facets,1)) # for contact1
    b2 = cvx.Variable((1+num_facets,1)) # for contact2
    
    # Define the objective
    # print("Grasp map: ", grasp_map.shape, "desired wrench: ", desired_wrench.shape, "fc: ", fc.shape)
    objective = cvx.Minimize(cvx.norm(grasp_map @ fc - desired_wrench.reshape(-1, 1)))
    
    # Define the constraints
    constraints = [
        cvx.norm(fc[:2]) <= mu*fc[2],
        cvx.norm(fc[4:6]) <= mu*fc[5],
        fc[2]>=0,
        fc[6]>=0,
        ##
        fc[2]<=1,
        fc[6]<=1,
        ##
        gamma*fc[2]>=cvx.abs(fc[3]),
        gamma*fc[5]>=cvx.abs(fc[7]),
        b1[0]==fc[2],
        b2[0]==fc[6]
    ]
    for i in range(num_facets):
        constraints.append(b1[i+1]>=0)
        constraints.append(b2[i+1]>=0)
        constraints.append(b1[i+1]<=mu*b1[0])
        constraints.append(b2[i+1]<=mu*b2[0])
        
    constraints.append(fc[:2]==A@b1[1:])
    constraints.append(fc[4:6]==A@b2[1:])
    
    
    constraints.append(cvx.sum(b1[1:])<=1)
    constraints.append(cvx.sum(b2[1:])<=1)
    

    
    # Solve the problem
    problem = cvx.Problem(objective, constraints)
    problem.solve()
    # print("Problem status: ", problem.status)
    # Check if the problem is feasible
    if problem.status == cvx.OPTIMAL:
            # print("Problem is feasible")
            return 1
    return 0
   


def compute_gravity_resistance(vertices, normals, num_facets, mu, gamma, object_mass):
    """
    Gravity produces some wrench on your object. Computes whether the grasp can 
    produce an equal and opposite wrench.

    Parameters
    ----------
    vertices (2x3 np.ndarray): obj mesh vertices on which the fingers will be placed
    normals (2x3 np.ndarray): obj mesh normals at the contact points
    num_facets (int): number of vectors to use to approximate the friction cone, vectors 
        will be along the friction cone boundary
    mu (float): coefficient of friction
    gamma (float): torsional friction coefficient
        torsional friction coefficient
    object_mass (float): mass of the object

    Returns
    -------
    (float): quality of the grasp
    """
    # YOUR CODE HERE
    gravity_wrench = np.array([0, 0, -9.8 * object_mass, 0, 0, 0])
        
    return contact_forces_exist(vertices, normals, num_facets, mu, gamma, gravity_wrench)
    

"""
you're encouraged to implement a version of this method, 
def sample_around_vertices(delta, vertices, object_mesh=None):
    raise NotImplementedError
"""

def compute_robust_force_closure(vertices, normals, num_facets, mu, gamma, object_mass):
    """
    Should return a score for the grasp according to the robust force closure metric.

    Parameters        # fc[2]<=1,
        # fc[6]<=1,
    ----------
    vertices (2x3 np.ndarray): obj mesh vertices on which the fingers will be placed
    normals (2x3 np.ndarray): obj mesh normals at the contact points
    num_facets (int): number of vectors to use to approximate the friction cone, vectors 
        will be along the friction cone boundary
    mu (float): coefficient of friction
    gamma (float): torsional friction coefficient
        torsional friction coefficient
    object_mass (float): mass of the object

    Returns
    -------
    (float): quality of the grasp
    """
    # YOUR CODE HERE
    num_samples=500
    gravity_wrench = np.array([0, 0, -9.8 * object_mass, 0, 0, 0])
    successful_grasps=0
    for _ in range(num_samples):
        # Add a random disturbance to the pose
        delta = np.random.normal(0, 1, vertices.shape)
        disturbed_vertices = vertices + delta

        # Compute the force closure for the disturbed pose
        if contact_forces_exist(disturbed_vertices, normals, num_facets, mu, gamma, gravity_wrench):
            successful_grasps += 1

    # Return the proportion of successful grasps
    return successful_grasps / num_samples


def compute_ferrari_canny(vertices, normals, num_facets, mu, gamma, object_mass):
    """
    Should return a score for the grasp according to the Ferrari Canny metric.
    Use your favourite python convex optimization package. We suggest cvxpy.

    Parameters
    ----------
    vertices (2x3 np.ndarray): obj mesh vertices on which the fingers will be placed
    normals (2x3 np.ndarray): obj mesh normals at the contact points
    num_facets (int): number of vectors to use to approximate the friction cone, vectors 
        will be along the friction cone boundary
    mu (float): coefficient of friction
    gamma (float): torsional friction coefficient
        torsional friction coefficient
    object_mass (float): mass of the object

    Returns
    -------
    (float): quality of the grasp
    """
    # YOUR CODE HERE
        # Compute the gravity wrench
    gravity_wrench = np.array([0, 0, -9.8 * object_mass, 0, 0, 0])

    # Initialize the minimum radius to infinity
    min_radius = np.inf

    # For each trial, add a random noise to the wrench and check if the contact forces exist
    num_trials = 10
    print("gamma: ", gamma)
    for _ in range(num_trials):
        # Add a random noise to the wrench
        noisy_wrench = gravity_wrench + np.random.normal(scale=0.1, size=6)

        # Check if the contact forces exist
        forces_exist = contact_forces_exist(vertices, normals, num_facets, mu, gamma, noisy_wrench)

        # If the contact forces exist, compute the radius of the smallest sphere that contains the wrench
        if forces_exist:
            radius = np.linalg.norm(noisy_wrench)
            min_radius = min(min_radius, radius)

    # If the minimum radius is still infinity, then the grasp is not force-closure and its quality is zero
    if min_radius == np.inf:
        return 0

    # Otherwise, the quality of the grasp is the inverse of the minimum radius
    return 1 / min_radius



def custom_grasp_planner(object_mesh, vertices):
    """
    Write your own grasp planning algorithm! You will take as input the mesh
    of an object, and a pair of contact points from the surface of the mesh.
    You should return a 4x4 ridig transform specifying the desired pose of the
    end-effector (the gripper tip) that you would like the gripper to be at
    before closing in order to execute your grasp.

    You should be prepared to handle malformed grasps. Return None if no
    good grasp is possible with the provided pair of contact points.
    Keep in mind the constraints of the gripper (length, minimum and maximum
    distance between fingers, etc) when picking a good pose, and also keep in
    mind limitations of the robot (can the robot approach a grasp from the inside
    of the mesh? How about from below?). You should also make sure that the robot
    can successfully make contact with the given contact points without colliding
    with the mesh.

    The trimesh package has several useful functions that allow you to check for
    collisions between meshes and rays, between meshes and other meshes, etc, which
    you may want to use to make sure your grasp is not in collision with the mesh.

    Take a look at the functions find_intersections, find_grasp_vertices, 
    normal_at_point in utils.py for examples of how you might use these trimesh 
    utilities. Be wary of using these functions directly. While they will probably 
    work, they don't do excessive edge-case handling. You should spend some time
    reading the documentation of these packages to find other useful utilities.
    You may also find the collision, proximity, and intersections modules of trimesh
    useful.

    Feel free to change the signature of this function to add more arguments
    if you believe they will be useful to your planner.

    Parameters
    ----------
    object_mesh (trimesh.base.Trimesh): A triangular mesh of the object, as loaded in with trimesh.
    vertices (2x3 np.ndarray): obj mesh vertices on which the fingers will be placed

    Returns
    -------
    (4x4 np.ndarray): The rigid transform for the desired pose of the gripper, in the object's reference frame.
    """


    # constants -- you may or may not want to use these variables below
    num_facets = 64
    mu = 0.5
    gamma = 0.1
    object_mass = 0.25
    g = 9.8
    desired_wrench = np.array([0, 0, g * object_mass, 0, 0, 0]).T

    trials = 100
    delta = 0.04
    gravity_th = 0
    ferrari_th = 0.4
    force_c_th = 0.5

    # YOUR CODE HERE
    for _ in range(trials):
        # Sample around vertices to get new normals and new vertices
        normals = object_mesh.face_normals
        sampled_normals = normals[np.random.choice(normals.shape[0], size=2, replace=False)]
        sampled_vertices = vertices + delta * sampled_normals

        # Check if contact forces exist
        forces = compute_force_closure(sampled_vertices, sampled_normals, num_facets, mu, gamma, object_mass)
        if forces == 1:
            # Compute the 3 metrics
            print("Forces: ", forces)
            print("before gravity resistance")
            gravity_resistance = compute_gravity_resistance(
                sampled_vertices, sampled_normals, num_facets, mu, gamma, object_mass)
            print("Gravity resistance: ", gravity_resistance)
            print("before ferrari canny")
            ferrari_canny = compute_ferrari_canny(
                sampled_vertices, sampled_normals, num_facets, mu, gamma, object_mass)
            print("Ferrari canny: ", ferrari_canny)
            print("before force closure")
            force_closure = compute_robust_force_closure(
                sampled_vertices, sampled_normals, num_facets, mu, gamma, object_mass)
            print("Force closure: ", force_closure)
            if gravity_resistance is None or ferrari_canny is None or force_closure is None:
                continue
            # If the three metrics’ thresholds are met, return the generated pose
            if gravity_resistance > gravity_th and ferrari_canny > ferrari_th and force_closure > force_c_th:
                # Compute the pose of the gripper
                angle_x0 = np.arccos(np.dot(sampled_normals[0], [1, 0, 0]))
                angle_x1 = np.arccos(np.dot(sampled_normals[1], [1, 0, 0]))

                # Use these angles as the Euler angles
                gripper_pose = trimesh.transformations.euler_matrix(angle_x0, angle_x1, 0)
                gripper_pose[:3, 3] = sampled_vertices.mean(axis=0)
                return gripper_pose

    # If no good grasp is found, return None
    return None



def get_gripper_pose(vertices, object_mesh): # you may or may not need this method 
    """
    Creates a 3D Rotation Matrix at the origin such that the y axis is the same
    as the direction specified.  There are infinitely many of such matrices,
    but we choose the one where the z axis is as vertical as possible.
    z -> y
    x -> x
    y -> z

    Parameters
    ----------
    origin : 3x1 :obj:`numpy.ndarray`
    x : 3x1 :obj:`numpy.ndarray`

    Returns
    -------
    4x4 :obj:`numpy.ndarray`
    """
    origin = np.mean(vertices, axis=0)
    direction = vertices[0] - vertices[1]

    up = np.array([0, 0, 1])
    y = normalize(direction)
    x = normalize(np.cross(up, y))
    z = np.cross(x, y)

    gripper_top = origin + GRIPPER_LENGTH * z
    gripper_double = origin + 2 * GRIPPER_LENGTH * z
    if len(find_intersections(object_mesh, gripper_top, gripper_double)[0]) > 0:
        z = normalize(np.cross(up, y))
        x = np.cross(y, x)
    result = np.eye(4)
    result[0:3,0] = x
    result[0:3,1] = y
    result[0:3,2] = z
    result[0:3,3] = origin
    return result


def visualize_grasp(mesh, vertices, pose):
    """Visualizes a grasp on an object. Object specified by a mesh, as
    loaded by trimesh. vertices is a pair of (x, y, z) contact points.
    pose is the pose of the gripper tip.

    Parameters
    ----------
    mesh (trimesh.base.Trimesh): mesh of the object
    vertices (np.ndarray): 2x3 matrix, coordinates of the 2 contact points
    pose (np.ndarray): 4x4 homogenous transform matrix
    """
    p1, p2 = vertices
    center = (p1 + p2) / 2
    approach = pose[:3, 2]
    tail = center - GRIPPER_LENGTH * approach

    contact_points = []
    for v in vertices:
        contact_points.append(vedo.Point(pos=v, r=30))

    vec = (p1 - p2) / np.linalg.norm(p1 - p2)
    line = vedo.shapes.Tube([center + 0.5 * MAX_GRIPPER_DIST * vec,
                                   center - 0.5 * MAX_GRIPPER_DIST * vec], r=0.001, c='g')
    approach = vedo.shapes.Tube([center, tail], r=0.001, c='g')
    vedo.show([mesh, line, approach] + contact_points, new=True)


def randomly_sample_from_mesh(mesh, n):
    """Example of sampling points from the surface of a mesh.
    Returns n (x, y, z) points sampled from the surface of the input mesh
    uniformly at random. Also returns the corresponding surface normals.

    Parameters
    ----------
    mesh (trimesh.base.Trimesh): mesh of the object
    n (int): number of desired sample points

    Returns
    -------
    vertices (np.ndarray): nx3 matrix, coordinates of the n surface points
    normals (np.ndarray): nx3 matrix, normals of the n surface points
    """
    vertices, face_ind = trimesh.sample.sample_surface(mesh, n)
    # you may want to check out the trimesh mehtods here:)
    
    normals = mesh.face_normals[face_ind]
    return vertices, normals


def load_grasp_data(object_name):
    """Loads grasp data from the provided NPZ files. It returns three arrays:

    Parameters
    ----------
    object_name (String): type of object

    Returns
    -------
    vertices (np.ndarray): nx3 matrix, coordinates of the n surface points
    normals (np.ndarray): nx3 matrix, normals of the n surface points

    grasp_vertices (np.ndarray): 5x2x3 matrix. For each of the 5 grasps,
            this stores a pair of (x, y, z) locations that are the contact points
            of the grasp.
    normals (np.ndarray): 5x2x3 matrix. For each grasp, stores the normal
            vector to the mesh at the two contact points. Remember that the normal
            vectors to a closed mesh always point OUTWARD from the mesh.
    tip_poses (np.ndarray): 5x4x4 matrix. For each of the five grasps, this
            stores the 4x4 rigid transform of the reference frame of the gripper
            tip before the gripper is closed in order to grasp the object.
    results (np.ndarray): 5x5 matrix. Stores the result of five trials for
            each of the five grasps. Entry (i, j) is a 1 if the jth trial of the
            ith grasp was successful, 0 otherwise.
    """
    data = np.load('/home/cc/ee106b/sp24/class/ee106b-abh/EECS-C206B/projects-3-4-ambulance/project4/src/proj4_pkg/grasp_data/{}.npz'.format(object_name))
    return data['grasp_vertices'], data['normals'], data['tip_poses'], data['results']


def load_mesh(object_name):
    mesh = trimesh.load_mesh('/home/cc/ee106b/sp24/class/ee106b-abh/EECS-C206B/projects-3-4-ambulance/project4/src/proj4_pkg/objects/{}.obj'.format(object_name))
    mesh.fix_normals()
    return mesh

# mesh = load_mesh('pawn')
# # load_mesh('pawn') # you can set this here, or not

def main():
    """ Example for interacting with the codebase. Loads data and
    visualizes each grasp against the corresponding mesh of the given
    object.
    """
    obj = 'nozzle' # should be 'pawn' or 'nozzle'.
    
    # mesh = trimesh.Trimesh(vertices=vertices, faces=poses, vertex_normals=normals)
    print("Visualize planning for the pawn object")
    vertices, normals, poses, results = load_grasp_data(obj)
    mesh = load_mesh(obj)
    
    print("Vertices: ", vertices)
    
    for v, p in zip(vertices, poses):
        visualize_grasp(mesh, v, p)

    # you may or may not find the code below helpful:) i was supposed to delete this from the starter code but i didn't so enjoy
    print("Grasp planning for the pawn object")
    v_and_p = [custom_grasp_planner(mesh, v) for v in vertices]
    print("v_and_p: ", v_and_p)
    for v, p in zip(vertices,v_and_p):
        if not p is None:
            visualize_grasp(mesh, v, p)
        else:
            print("None")
    vert1, norm1 = randomly_sample_from_mesh(mesh, 3)
    while len(vert1) < 3:
        vert1, norm1 = randomly_sample_from_mesh(mesh, 3)
    vert2 = np.array([find_intersections(mesh, vert1[i], vert1[i] - 5 * norm1[i])[0][-1] for i in range(len(vert1))]) #randomly_sample_from_mesh(mesh, 3)
    vertices = list(zip(vert1, vert2))


if __name__ == '__main__':
    main()

