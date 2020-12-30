#!/bin/sh

set -x

sudo apt-get install ros-melodic-hls-lfcd-lds-driver -y
sudo chmod a+rw /dev/ttyUSB0

