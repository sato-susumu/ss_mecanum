#!/bin/sh

set -x
sudo cp -f roslaunch_autostart /usr/sbin/
sudo cp -f ros_autostart.service  /etc/systemd/system/
sudo systemctl enable ros_autostart
sudo systemctl start ros_autostart
