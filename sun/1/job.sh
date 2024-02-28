#! bin/bash

pro1='kansas'

pro2='perth-and-kansas'

#tleap -s -f $pro1.tleap.in&&

#echo "    "
#echo "start simulating protein 1 ......"

#pmemd.cuda -O -i $pro1.min1.in -o $pro1.min1.out -p $pro1.prmtop -c $pro1.inpcrd -inf $pro1.min1.info -r $pro1.min1.rst -ref $pro1.inpcrd&&

#pmemd.cuda -O -i min2.in -o $pro1.min2.out -p $pro1.prmtop -c $pro1.min1.rst -inf $pro1.min2.info -r $pro1.min2.rst&&

#pmemd.cuda -O -i $pro1.heat.in -o $pro1.heat.out -p $pro1.prmtop -c $pro1.min2.rst -inf $pro1.heat.info -r $pro1.heat.rst -x $pro1.heat.nc -ref $pro1.min2.rst&&

#pmemd.cuda -O -i $pro1.equil.in -o $pro1.equil.out -p $pro1.prmtop -c $pro1.heat.rst -inf $pro1.equil.info -r $pro1.equil.rst -x $pro1.equil.nc -ref $pro1.heat.rst&&

#pmemd.cuda -O -i equil2.in -o $pro1.equil2.out -p $pro1.prmtop -c $pro1.equil.rst -inf $pro1.equil2.info -r $pro1.equil2.rst -x $pro1.equil2.nc&&

#pmemd.cuda -O -i prod.in -o $pro1.prod.out -p $pro1.prmtop -c $pro1.equil2.rst -inf $pro1.prod.info -r $pro1.prod.rst -x $pro1.prod.nc&&

#echo " protein 1's simulation completed "

#tleap -s -f $pro2.tleap.in&&

#echo "    "
#echo "start simulating protein 2 ......"

#pmemd.cuda -O -i $pro2.min1.in -o $pro2.min1.out -p $pro2.prmtop -c $pro2.inpcrd -inf $pro2.min1.info -r $pro2.min1.rst -ref $pro2.inpcrd&&

#pmemd.cuda -O -i min2.in -o $pro2.min2.out -p $pro2.prmtop -c $pro2.min1.rst -inf $pro2.min2.info -r $pro2.min2.rst&&

#pmemd.cuda -O -i $pro2.heat.in -o $pro2.heat.out -p $pro2.prmtop -c $pro2.min2.rst -inf $pro2.heat.info -r $pro2.heat.rst -x $pro2.heat.nc -ref $pro2.min2.rst&&

#pmemd.cuda -O -i $pro2.equil.in -o $pro2.equil.out -p $pro2.prmtop -c $pro2.heat.rst -inf $pro2.equil.info -r $pro2.equil.rst -x $pro2.equil.nc -ref $pro2.heat.rst&&

pmemd.cuda -O -i equil2.in -o $pro2.equil2.out -p $pro2.prmtop -c $pro2.equil.rst -inf $pro2.equil2.info -r $pro2.equil2.rst -x $pro2.equil2.nc&&

pmemd.cuda -O -i prod.in -o $pro2.prod.out -p $pro2.prmtop -c $pro2.equil2.rst -inf $pro2.prod.info -r $pro2.prod.rst -x $pro2.prod.nc

echo " protein 2's simulation completed "
