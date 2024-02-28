#!/bin/bash
         grep  -v '^.............H[^A]' mirrored_IL10R1-helix_11_1627977889_242519.pdb > mid
         grep  -v '^............H' mid > mirrored_IL10R1-helix_11_1627977889_242519_h.pdb
         grep   '^............HA' mirrored_IL10R1-helix_11_1627977889_242519.pdb >> mirrored_IL10R1-helix_11_1627977889_242519_h.pdb
         sed -i '/HA  GLY/d'  mirrored_IL10R1-helix_11_1627977889_242519_h.pdb
         tleap -f leap.in
         cat leap.log | grep "Total unperturbed charge:" | awk '{for (i=1;i<=NF;i++);print("IL10R1-helix_11_1627977889_242519,", $4)}' >> charge.csv  
         mkdir IL10R1-helix_11_1627977889_242519
         mv  IL10R1-helix_11_1627977889_242519_solvated.prmtop IL10R1-helix_11_1627977889_242519/cpx_solvated.prmtop
         mv IL10R1-helix_11_1627977889_242519_solvated.inpcrd  IL10R1-helix_11_1627977889_242519/cpx_solvated.inpcrd
         mv IL10R1-helix_11_1627977889_242519_solvated.pdb  IL10R1-helix_11_1627977889_242519/cpx_solvated.pdb
         rm mid leap.in leap.log mirror*.pdb 
         cp -r ctrl_in IL10R1-helix_11_1627977889_242519 
         mv md_analysis.sh rmsd.sh rmsf.sh dssp.sh cluster.sh  IL10R1-helix_11_1627977889_242519
         