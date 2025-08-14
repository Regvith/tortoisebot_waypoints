cmake_minimum_required(VERSION 3.0.2)
project(tortoisebot_waypoints)

find_package(catkin REQUIRED COMPONENTS
  actionlib
  actionlib_msgs
  geometry_msgs
  message_generation
  nav_msgs
  rospy
  std_msgs
)

## Declare action files
add_action_files(
  FILES
  Waypoint.action
)

## Generate messages from action files
generate_messages(
  DEPENDENCIES
  std_msgs
  geometry_msgs
  actionlib_msgs
)

## Declare catkin package
catkin_package(
  CATKIN_DEPENDS
    actionlib_msgs
    geometry_msgs
    std_msgs
    message_runtime
    
)

include_directories(
  ${catkin_INCLUDE_DIRS}
)

## Install Python action server script
catkin_install_python(PROGRAMS
  scripts/tortoisebot_action_server.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

## Testing
if(CATKIN_ENABLE_TESTING)
  find_package(rostest REQUIRED)
  add_rostest(launch/waypoints_test.test)
endif()
