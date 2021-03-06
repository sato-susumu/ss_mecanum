#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
import math
from std_msgs.msg import Float32
from std_msgs.msg import Int32MultiArray

motor_front_left_rpm = 0
motor_front_right_rpm = 0
motor_rear_left_rpm = 0
motor_rear_right_rpm = 0

sub_motor_front_left = None
sub_motor_front_right = None
sub_motor_rear_left = None
sub_motor_rear_right = None

LIMIT_RPM = 12.5
MINIMUM_RPM = 1

reverse_rotation_of_right_motor_enabled = True

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


def rpm_to_pwm(rpm):
    if rpm > LIMIT_RPM:
        rpm = LIMIT_RPM
    if rpm < -LIMIT_RPM:
        rpm = -LIMIT_RPM
    if abs(rpm) < MINIMUM_RPM:
        # brake
        return 0xffff, 0, 0
    if rpm >= 0:
        # rotate counterclockwise
        return 0xffff * rpm / LIMIT_RPM, 0xffff, 0
    # rotate clockwise
    return 0xffff * -rpm / LIMIT_RPM, 0, 0xffff


def stop():
    array = []
    array.extend([0, 0, 0, 0, 0, 0])
    array.extend([0, 0, 0, 0, 0, 0])
    array.extend([-1, -1, -1, -1])
    array_for_publish = Int32MultiArray(data=array)
    pub.publish(array_for_publish)


def handle_shutdown():
    rospy.logwarn('handle_shutdown')
    stop()


if __name__ == '__main__':
    try:
        rospy.init_node('ss_mecanum_motors')
        rospy.on_shutdown(handle_shutdown)
        rate = rospy.Rate(10)

        pub = rospy.Publisher('command', Int32MultiArray, queue_size=1)

        sub_motor_front_left = rospy.Subscriber(
            'motor/front_left', Float32, handle_motor_front_left)
        sub_motor_front_right = rospy.Subscriber(
            'motor/front_right', Float32, handle_motor_front_right)
        sub_motor_rear_left = rospy.Subscriber(
            'motor/rear_left', Float32, handle_motor_rear_left)
        sub_motor_rear_right = rospy.Subscriber(
            'motor/rear_right', Float32, handle_motor_rear_right)

        while not rospy.is_shutdown():
            array = []

            ena, in1, in2 = rpm_to_pwm(motor_front_right_rpm)
            enb, in3, in4 = rpm_to_pwm(motor_front_left_rpm)
            if reverse_rotation_of_right_motor_enabled:
                array.extend([ena, in2, in1, in3, in4, enb])
            else:
                array.extend([ena, in1, in2, in3, in4, enb])

            ena, in1, in2 = rpm_to_pwm(motor_rear_right_rpm)
            enb, in3, in4 = rpm_to_pwm(motor_rear_left_rpm)
            if reverse_rotation_of_right_motor_enabled:
                array.extend([ena, in2, in1, in3, in4, enb])
            else:
                array.extend([ena, in1, in2, in3, in4, enb])

            array.extend([-1, -1, -1, -1])

            array_for_publish = Int32MultiArray(data=array)
            pub.publish(array_for_publish)
            # rospy.logwarn('rpm {0:.2f}, {1:.2f}, {2:.2f}, {3:.2f}'.format(
            #    motor_front_left_rpm,
            #    motor_front_right_rpm,
            #    motor_rear_left_rpm,
            #    motor_rear_right_rpm))
            rate.sleep()

    except rospy.ROSInterruptException:
        pass
