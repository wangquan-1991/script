#!bin/bash
awk '{print $3}' test.dat.gnu > 111.dat
awk 'ORS=NR%250?" ":"\n"{print}' 111.dat>juzhen.dat
rm 111.dat
