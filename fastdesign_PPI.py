#根据PPI选择关键残基进行设计
def make_saturation_resfile(pdbfile, partner_chain, cutoff):
    init()
    pose = pose_from_pdb(pdbfile)
    group1 = ChainSelector(partner_chain)
    group2 = NotResidueSelector(group1)
    interface_seletor = InterGroupInterfaceByVectorSelector(group1, group2)
    interface_seletor.vector_dist_cut(float(cutoff))
    interface_seletor.nearby_atom_cut(6.0)
    designable_selector = AndResidueSelector(interface_seletor, group1)
    designable_selector_g2 = AndResidueSelector(interface_seletor, group2)
    selected_index = SelectedResiduesMetric(designable_selector)
    selected_index_g2 = SelectedResiduesMetric(designable_selector_g2)
    selected_index.set_output_in_rosetta_num(True)  # output as pose id.
    selected_index.apply(pose)
    sm_data = get_sm_data(pose)
    selected_pose_id_list = sm_data.get_string_metric_data()['selection']
    print(f"ppi residue: {selected_pose_id_list}")
    
    # get peptide start/end res:
    start_res = pose.chain_begin(pose.num_chains())
    end_res = pose.chain_end(pose.num_chains())
    for pose_id in selected_pose_id_list.split(','):
        if int(pose_id) in [start_res, end_res]:
            # 不允许突变:
            continue
        info = pose.pdb_info().pose2pdb(int(pose_id))
        pdb_num = info.split(' ')[0]
        chain_id = info.split(' ')[1]
        phi_angles = pose.phi(int(pose_id))
        native_residue = pose.residue(int(pose_id)).name3()
        #write_resfile(pdb_num, chain_id, native_residue, phi_angles, use_ncaa, cyclization_type, savedpath)
        print(pdb_num, chain_id, native_residue)