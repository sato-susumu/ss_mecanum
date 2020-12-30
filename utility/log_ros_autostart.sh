#!/bin/sh

set -x
journalctl | grep -e roslaunch_autostart
