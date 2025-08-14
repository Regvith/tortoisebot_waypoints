# This is a simulation for tortoisebot, here the testing takes place using rostest so the conditions for failing and passing will be listed below



# launch the gazebo world then using 
   - source /opt/ros/noetic/setup.bash
   - source ~/simulation_ws/devel/setup.bash
   - roslaunch tortoisebot_gazebo tortoisebot_playground.launch

# colcon build and start the action server 
    - source /opt/ros/noetic/setup.bash
    - cd ~/simulation_ws && catkin_make && source devel/setup.bash
    - rosrun tortoisebot_waypoints tortoisebot_action_server.py

# run the test unit 
    - source /opt/ros/noetic/setup.bash
    - cd ~/simulation_ws && catkin_make && source devel/setup.bash
    - rostest tortoisebot_waypoints waypoints_test.test --reuse-master

# Conditions for passing and failing
    # For passing
        - The robot must have values with regards to visual inspection. For instance, if robot is at (0,0)
          and there is a sofa' side at (1,1), any values less than 1,1 for x,y in test code will work. 
        - In conclusion, it is essential to make sure that the selcted the values of x,y must be away from obstacles.
        def test_first_waypoint(self):
        self.send_and_check_goal(0.2, 0.4)

        def test_second_waypoint(self):
            self.send_and_check_goal(0.1, 0.45)
    # For failing
        - The robot times-out after 15s and the robot moves at a fixed velocity of 0.6 m/s linearly and either 0.65 or -0.65 angularly.
          trot = pi/w = 3.1457/0.65 = 4.83 s ; td = d/v ; Ttot = trot + td 
          so, if Ttot >15 it will fail, provided there is no obstacles.
        - THe obstacles are placed extremely closeby so if x is either greater than 1.0 or y is greater than 1.0, the tests are bound to fail
        def test_first_waypoint(self):
            self.send_and_check_goal(1.0, 0.4)

        