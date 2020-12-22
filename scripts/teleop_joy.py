#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from sensor_msgs.msg import Joy
from geometry_msgs.msg import Twist

max_vel_x = 0.5
max_vel_y = 0.5
max_vel_th = 3.0

JOY_AXES_ANALOG_STICK_L_X = 1
JOY_AXES_ANALOG_STICK_L_Y = 0
JOY_BUTTONS_LB = 4
JOY_BUTTONS_RB = 5

def handle_joy(joy_msg):
    twist = Twist()
    twist.linear.x = joy_msg.axes[JOY_AXES_ANALOG_STICK_L_X] * max_vel_x
    twist.linear.y = joy_msg.axes[JOY_AXES_ANALOG_STICK_L_Y] * max_vel_y
    if joy_msg.buttons[JOY_BUTTONS_LB] == 1:
        twist.angular.z = max_vel_th
    elif joy_msg.buttons[JOY_BUTTONS_RB] == 1:
        twist.angular.z = -max_vel_th
    else:
        twist.angular.z = 0
    pub.publish(twist)

def stop():
    twist = Twist()
    twist.linear.x = 0
    twist.linear.y = 0
    twist.linear.z = 0
    pub.publish(twist)

def handle_shutdown():
    rospy.logwarn('handle_shutdown')
    stop()

if __name__ == '__main__':
    try:
        rospy.init_node('teleop_joy')
        rospy.on_shutdown(handle_shutdown)
        sub = rospy.Subscriber('joy', Joy, handle_joy, queue_size=16)
        pub = rospy.Publisher('cmd_vel', Twist, queue_size=1)
        rospy.spin()
    except rospy.ROSInterruptException:
        pass

