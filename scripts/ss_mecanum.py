#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# The original algorithm is http://robotsforroboticists.com/drive-kinematics/

import rospy
from std_msgs.msg import Float32
from geometry_msgs.msg import Twist

DISTANCE_LEFT_TO_RIGHT_WHEEL = 0.21
DISTANCE_FRONT_TO_REAR_WHEEL = 0.10
WHEEL_RADIUS = 0.04

pub_motor_front_left = None
pub_motor_front_right = None
pub_motor_rear_left = None
pub_motor_rear_right = None


def handle_cmd_vel(twist_param):
    x = twist_param.linear.x
    y = twist_param.linear.y
    z = twist_param.angular.z
    wheel_separation_width = DISTANCE_LEFT_TO_RIGHT_WHEEL / 2
    wheel_separation_length = DISTANCE_FRONT_TO_REAR_WHEEL / 2

    wheel_front_left = (1 / WHEEL_RADIUS) * (x - y -
                                             (wheel_separation_width + wheel_separation_length) * z)
    wheel_front_right = (1 / WHEEL_RADIUS) * (x + y +
                                              (wheel_separation_width + wheel_separation_length) * z)
    wheel_rear_left = (1 / WHEEL_RADIUS) * (x + y -
                                            (wheel_separation_width + wheel_separation_length) * z)
    wheel_rear_right = (1 / WHEEL_RADIUS) * (x - y +
                                             (wheel_separation_width + wheel_separation_length) * z)

    wheel_front_right = -1 * wheel_front_right
    wheel_rear_right = -1 * wheel_rear_right

    pub_motor_front_left.publish(wheel_front_left)
    pub_motor_front_right.publish(wheel_front_right)
    pub_motor_rear_left.publish(wheel_rear_left)
    pub_motor_rear_right.publish(wheel_rear_right)


if __name__ == '__main__':
    try:
        rospy.init_node('ss_mecanum')

        sub = rospy.Subscriber('cmd_vel', Twist, handle_cmd_vel)

        pub_motor_front_left = rospy.Publisher(
            'motor/front_left', Float32, queue_size=1)
        pub_motor_front_right = rospy.Publisher(
            'motor/front_right', Float32, queue_size=1)
        pub_motor_rear_left = rospy.Publisher(
            'motor/rear_left', Float32, queue_size=1)
        pub_motor_rear_right = rospy.Publisher(
            'motor/rear_right', Float32, queue_size=1)

        rospy.spin()
    except rospy.ROSInterruptException:
        pass
