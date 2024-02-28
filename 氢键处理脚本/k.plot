set title "Close Contact of LZ1 of Wile Type System"
set key off
set terminal png transparent nocrop size 800, 500
set output 'test.png'
set tic scale 0.4
set cbrange [0:100]
set cblabel "Percentage"
unset cbtics

set xrange [0:49]
set yrange [0:7]
set xtics nomirror
unset xtics
set ytics nomirror
unset ytics
set view map
set palette rgbformulae 22,13,-31 #-7, 2, -7(green-white)
splot 'cdj4_h.dat' matrix with image
