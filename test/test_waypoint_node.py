#!/usr/bin/env python

import rospy
import unittest
import actionlib
from geometry_msgs.msg import Point
from tortoisebot_waypoints.msg import WaypointGoal, WaypointAction

class TestWaypointNode(unittest.TestCase):
    def setUp(self):
        rospy.init_node('test_waypoint_node', anonymous=True)
        self.client = actionlib.SimpleActionClient('/tortoisebot_as', WaypointAction)
        self.assertTrue(self.client.wait_for_server(rospy.Duration(10)))

    def send_and_check_goal(self, x, y, z=0.0):
       try:
            goal = WaypointGoal()
            goal.position = Point(x=x, y=y, z=z)
            self.client.send_goal(goal)
            finished_before_timeout = self.client.wait_for_result(rospy.Duration(15.0))

            self.assertTrue(finished_before_timeout, "Timed out waiting for waypoint action to finish")

            result = self.client.get_result()
            self.assertIsNotNone(result, "No result received from action server")
            self.assertTrue(result.success, f"Waypoint action to ({x}, {y}) reported failure")
            rospy.sleep(2)
       except Exception as e:
            self.fail(f"Exception during send_and_check_goal: {e}")

    def test_first_waypoint(self):
        self.send_and_check_goal(0.2, 0.4)

    def test_second_waypoint(self):
        self.send_and_check_goal(0.1, 0.45)

if __name__ == '__main__':
    import rostest
    rostest.rosrun('tortoisebot_waypoints', 'test_waypoint_node', TestWaypointNode)
