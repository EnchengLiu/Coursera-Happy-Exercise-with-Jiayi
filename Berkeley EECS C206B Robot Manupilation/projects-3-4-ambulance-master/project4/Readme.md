# Project 4

#EECS-C206B Lab 4

EECS C206B: Robotic Manipulation and Interaction

Project 4: Grasp Planning with Sawyer 

Professor: Shankar Sastry

Team Members: Tianqi Zeng, Encheng Liu, Enyang Zou

Lab Doc: https://ucb-ee106.github.io/106b-sp24site/assets/proj/proj4.pdf

Lab Report Video: https://drive.google.com/file/d/1GXad7t8-8eQQp-zyBbwTg42D6n97q5GY/view?usp=drive_link



The purpose of this project is to combine many of the topics presented in this course to plan and execute a grasp
with a manipulator in the lab. This will consist of detecting the object to grasp, planning a stable grasp, moving into
position, closing the grippers, and lifting.

The starter code is only tested with `python3.8`.

The returned Vertices and poses
[array([[-0.61715641,  0.58159332,  0.52996904,  0.00100499],
       [-0.        ,  0.67354062, -0.73915021,  0.00758837],
       [-0.7868405 , -0.45617129, -0.41567991,  0.07906145],
       [ 0.        ,  0.        ,  0.        ,  1.        ]]),
array([[-0.90434786,  0.32739525,  0.27380155, -0.00531081],
       [-0.        ,  0.64152772, -0.76709985, -0.01202467],
       [-0.42679613, -0.69372511, -0.58016423,  0.0618564 ],
       [ 0.        ,  0.        ,  0.        ,  1.        ]]), 
array([[-0.54372507,  0.70496948, -0.45539113, -0.0229532 ],
       [-0.        , -0.54260811, -0.83998597, -0.02891737],
       [-0.83926339, -0.45672144,  0.29502964,  0.04847022],
       [ 0.        ,  0.        ,  0.        ,  1.        ]]), 
array([[-0.86096587,  0.18979348, -0.47192817, -0.03439192],
       [-0.        , -0.92778211, -0.37312244,  0.0114155 ],
       [-0.50866272, -0.32124569,  0.79878873,  0.06675429],
       [ 0.        ,  0.        ,  0.        ,  1.        ]]), 
array([[ 0.35880305,  0.56387456, -0.74384532, -0.00758277],
       [ 0.        , -0.79690886, -0.60409956, -0.00602424],
       [-0.93341329,  0.21675276, -0.28593333,  0.06555393],
       [ 0.        ,  0.        ,  0.        ,  1.        ]])]
