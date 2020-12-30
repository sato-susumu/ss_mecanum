#!/bin/sh

set -x

mkdir -p ~/catkin_ws/src
cd ~/catkin_ws/src
git clone https://github.com/yoshito-n-students/remote_rosbag_record.git
cd ~/catkin_ws
catkin_make

