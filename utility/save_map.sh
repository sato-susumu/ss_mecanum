#!/bin/sh

set -x
rosrun map_server map_saver -f  ../maps/map
convert ../maps/map.pgm ../maps/map.png
rm ../maps/map.pgm
perl -pi -e 's/.pgm/.png/g' ../maps/map.yaml
