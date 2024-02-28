cpptraj <<EOF
parm cpx_solvated.prmtop
trajin prod.nc
hbond :1-2000 out nhb.dat avgout avghb.dat
EOF

