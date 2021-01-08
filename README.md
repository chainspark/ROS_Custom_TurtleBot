# ROS Kinetic Custom TurtleBot

The package includes URDF and launch files for Differential Drive Robot with a XtionPro RGB-D Camera sensor to visualize the environment in the Gazebo using turtlebot teleoperation control node.

## Custom Differential Drive Robot Linkages
[embed]https://github.com/chainspark/ROS_Custom_TurtleBot/blob/main/src/star_wookie/urdf/differential_wheeled_robot.pdf[/embed]

## Rviz Visualization of Robot
![](https://github.com/chainspark/ROS_Custom_TurtleBot/blob/main/src/Screenshots/Rviz_Robot_Description.png)

## Movement of robot using Turtlebot Teleoperation
![](https://github.com/chainspark/ROS_Custom_TurtleBot/blob/main/src/Screenshots/Gazebo_world.png)

## OpenCV Node image processing  
OpenCv bridge for ROS to used to perform convolution on raw image feed to create cartoon and sketch effect on the feed. 
![](https://github.com/chainspark/ROS_Custom_TurtleBot/blob/main/src/Screenshots/Gazebo_world_OpenCv_Bridge.png)

### Raw Image feed
![](https://github.com/chainspark/ROS_Custom_TurtleBot/blob/main/src/Screenshots/Raw_Image%20window_screenshot.png)

### Cartoonized Image
![](https://github.com/chainspark/ROS_Custom_TurtleBot/blob/main/src/Screenshots/OpenCV_Cartoonized%20Window_screenshot.png)

### Sketch Image
![](https://github.com/chainspark/ROS_Custom_TurtleBot/blob/main/src/Screenshots/OpenCV_Sketch_Window_screenshot_.png)
