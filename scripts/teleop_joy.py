#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from sensor_msgs.msg import Joy
from geometry_msgs.msg import Twist

max_vel_x = 1
max_vel_y = 1
max_vel_th = 1.0


def handle_joy(joy_msg):
    twist = Twist()
    twist.linear.x = joy_msg.axes[1] * max_vel_x
    twist.linear.y = joy_msg.axes[0] * max_vel_y
    # twist.angular.z = joy_msg.axes[0] * max_vel_th
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

