#!/bin/sh

set -x
sudo systemctl stop ros_autostart
sudo systemctl disable ros_autostart
sudo rm /usr/sbin/roslaunch_autostart
sudo rm /etc/systemd/system/ros_autostart.service
