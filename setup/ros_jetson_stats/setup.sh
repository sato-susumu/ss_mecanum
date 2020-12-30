#!/bin/sh

set -x

sudo apt install python-pip
sudo -H pip install -U jetson-stats
mkdir -p ~/catkin_ws/src
cd ~/catkin_ws/src
git clone https://github.com/rbonghi/ros_jetson_stats.git
cd ~/catkin_ws
catkin_make
echo 'Required reboot.'

