#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
import math
from std_msgs.msg import Float32


motor_front_left_rpm = 0
motor_front_right_rpm = 0
motor_rear_left_rpm = 0
motor_rear_right_rpm = 0

sub_motor_front_left = None
sub_motor_front_right = None
sub_motor_rear_left = None
sub_motor_rear_right = None


def to_rpm(angular_velocity):
    return 60 * angular_velocity / (2 * math.pi)


def handle_motor_front_left(param):
    global motor_front_left_rpm
    motor_front_left_rpm = param.data


def handle_motor_front_right(param):
    global motor_front_right_rpm
    motor_front_right_rpm = param.data


def handle_motor_rear_left(param):
    global motor_rear_left_rpm
    motor_rear_left_rpm = param.data


def handle_motor_rear_right(param):
    global motor_rear_right_rpm
    motor_rear_right_rpm = param.data


if __name__ == '__main__':
    try:
        rospy.init_node('dummy_motors')
        rate = rospy.Rate(1)

        sub_motor_front_left = rospy.Subscriber(
            'motor/front_left', Float32, handle_motor_front_left)
        sub_motor_front_right = rospy.Subscriber(
            'motor/front_right', Float32, handle_motor_front_right)
        sub_motor_rear_left = rospy.Subscriber(
            'motor/rear_left', Float32, handle_motor_rear_left)
        sub_motor_rear_right = rospy.Subscriber(
            'motor/rear_right', Float32, handle_motor_rear_right)

        while not rospy.is_shutdown():
            rospy.loginfo('front {0:.2f}, {1:.2f}'.format(
                motor_front_left_rpm,
                - motor_front_right_rpm
            ))
            rospy.loginfo('rear  {0:.2f}, {1:.2f}'.format(
                motor_rear_left_rpm,
                - motor_rear_right_rpm
            ))
            rate.sleep()

    except rospy.ROSInterruptException:
        pass
