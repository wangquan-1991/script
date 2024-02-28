#########################################################################
# File Name: plot.sh
# Author: A. Penheimer
# Created Time: Fri Jul 11 09:28:38 2014
#########################################################################
#!/bin/bash
filename="cdj4_h.dat"
sed -i "s/\ /\ 0/g" $filename
sed -i "s/\./\ 20/g" $filename
sed -i "s/\-/\ 40/g" $filename
sed -i "s/o/\ 60/g" $filename
sed -i "s/x/\ 80/g" $filename
sed -i "s/\@/\ 100/g" $filename
sed -i "s/\*/\ 95/g" $filename
sed -i '1!G;h;$!d' $filename
gnuplot k.plot
