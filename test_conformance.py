import pm4py
import sys
if __name__ == "__main__":
    BPIC13_cp_output_file = '/app/data/BPIC13_cp.xes'
    BPIC13_i_output_file = '/app/data/BPIC13_i.xes'
    # BPIC14_f_output_file = '/app/data/BPIC14_f.xes'
    BPIC15_1f_output_file = '/app/data/BPIC15_1f.xes'
    BPIC15_2f_output_file = '/app/data/BPIC15_2f.xes'
    BPIC15_4f_output_file = '/app/data/BPIC15_4f.xes'
    BPIC15_5f_output_file = '/app/data/BPIC15_5f.xes'
    BPIC17_f_output_file = '/app/data/BPIC17_f.xes'
    RTFMP_output_file = '/app/data/RTFMP.xes'
    SEPSIS_output_file = '/app/data/SEPSIS.xes'
    # 加载解压后的 .xes 文件
    BPIC13_cp = pm4py.read_xes(BPIC13_cp_output_file)
    BPIC13_i = pm4py.read_xes(BPIC13_i_output_file)
    # BPIC14_f = pm4py.read_xes(BPIC14_f_output_file)
    BPIC15_1f = pm4py.read_xes(BPIC15_1f_output_file)
    BPIC15_2f = pm4py.read_xes(BPIC15_2f_output_file)
    BPIC15_4f = pm4py.read_xes(BPIC15_4f_output_file)
    BPIC15_5f = pm4py.read_xes(BPIC15_5f_output_file)
    BPIC17_f = pm4py.read_xes(BPIC17_f_output_file)
    RTFMP = pm4py.read_xes(RTFMP_output_file)
    SEPSIS = pm4py.read_xes(SEPSIS_output_file)


    if len(sys.argv) > 1:
        # 获取第一个命令行参数
        param = sys.argv[1]
        print(f"第一个命令行参数是: {param}")
        if param == "token":
            # 基于Token重演方法的合规性检查
            net_inductive_t2, im_inductive_t2, fm_inductive_t2 = pm4py.discover_petri_net_inductive(BPIC13_cp,
                                                                                                 activity_key='concept:name',
                                                                                                 case_id_key='case:concept:name',
                                                                                                 timestamp_key='time:timestamp')
            tbr_diagnostics_inductive = pm4py.conformance_diagnostics_token_based_replay(BPIC13_cp, net_inductive_t2,
                                                                                         im_inductive_t2, fm_inductive_t2,
                                                                                         activity_key='concept:name',
                                                                                         case_id_key='case:concept:name',
                                                                                         timestamp_key='time:timestamp')
            net_inductive_t3, im_inductive_t3, fm_inductive_t3 = pm4py.discover_petri_net_inductive(BPIC13_i,
                                                                                                 activity_key='concept:name',
                                                                                                 case_id_key='case:concept:name',
                                                                                                 timestamp_key='time:timestamp')
            tbr_diagnostics_inductive = pm4py.conformance_diagnostics_token_based_replay(BPIC13_i, net_inductive_t3,
                                                                                         im_inductive_t3, fm_inductive_t3,
                                                                                         activity_key='concept:name',
                                                                                         case_id_key='case:concept:name',
                                                                                         timestamp_key='time:timestamp')
            # net_inductive_t4, im_inductive_t4, fm_inductive_t4 = pm4py.discover_petri_net_inductive(BPIC14_f,
            #                                                                                      activity_key='concept:name',
            #                                                                                      case_id_key='case:concept:name',
            #                                                                                      timestamp_key='time:timestamp')
            # tbr_diagnostics_inductive = pm4py.conformance_diagnostics_token_based_replay(BPIC14_f, net_inductive_t4,
            #                                                                              im_inductive_t4, fm_inductive_t4,
            #                                                                              activity_key='concept:name',
            #                                                                              case_id_key='case:concept:name',
            #                                                                              timestamp_key='time:timestamp')
            net_inductive_t5, im_inductive_t5, fm_inductive_t5 = pm4py.discover_petri_net_inductive(BPIC15_1f,
                                                                                                 activity_key='concept:name',
                                                                                                 case_id_key='case:concept:name',
                                                                                                 timestamp_key='time:timestamp')
            tbr_diagnostics_inductive = pm4py.conformance_diagnostics_token_based_replay(BPIC15_1f, net_inductive_t5,
                                                                                         im_inductive_t5, fm_inductive_t5,
                                                                                         activity_key='concept:name',
                                                                                         case_id_key='case:concept:name',
                                                                                         timestamp_key='time:timestamp')
            net_inductive_t6, im_inductive_t6, fm_inductive_t6 = pm4py.discover_petri_net_inductive(BPIC15_2f,
                                                                                                 activity_key='concept:name',
                                                                                                 case_id_key='case:concept:name',
                                                                                                 timestamp_key='time:timestamp')
            tbr_diagnostics_inductive = pm4py.conformance_diagnostics_token_based_replay(BPIC15_2f, net_inductive_t6,
                                                                                         im_inductive_t6, fm_inductive_t6,
                                                                                         activity_key='concept:name',
                                                                                         case_id_key='case:concept:name',
                                                                                         timestamp_key='time:timestamp')

            net_inductive_t8, im_inductive_t8, fm_inductive_t8 = pm4py.discover_petri_net_inductive(BPIC15_4f,
                                                                                                 activity_key='concept:name',
                                                                                                 case_id_key='case:concept:name',
                                                                                                 timestamp_key='time:timestamp')
            tbr_diagnostics_inductive = pm4py.conformance_diagnostics_token_based_replay(BPIC15_4f, net_inductive_t8,
                                                                                         im_inductive_t8, fm_inductive_t8,
                                                                                         activity_key='concept:name',
                                                                                         case_id_key='case:concept:name',
                                                                                         timestamp_key='time:timestamp')
            net_inductive_t9, im_inductive_t9, fm_inductive_t9 = pm4py.discover_petri_net_inductive(BPIC15_5f,
                                                                                                 activity_key='concept:name',
                                                                                                 case_id_key='case:concept:name',
                                                                                                 timestamp_key='time:timestamp')
            tbr_diagnostics_inductive = pm4py.conformance_diagnostics_token_based_replay(BPIC15_5f, net_inductive_t9,
                                                                                         im_inductive_t9, fm_inductive_t9,
                                                                                         activity_key='concept:name',
                                                                                         case_id_key='case:concept:name',
                                                                                         timestamp_key='time:timestamp')
            # net_inductive_t10, im_inductive_t10, fm_inductive_t10 = pm4py.discover_petri_net_inductive(BPIC17_f,
            #                                                                                      activity_key='concept:name',
            #                                                                                      case_id_key='case:concept:name',
            #                                                                                      timestamp_key='time:timestamp')
            # tbr_diagnostics_inductive = pm4py.conformance_diagnostics_token_based_replay(BPIC17_f, net_inductive_t10,
            #                                                                              im_inductive_t10, fm_inductive_t10,
            #                                                                              activity_key='concept:name',
            #                                                                              case_id_key='case:concept:name',
            #                                                                              timestamp_key='time:timestamp')
            net_inductive_t11, im_inductive_t11, fm_inductive_t11 = pm4py.discover_petri_net_inductive(RTFMP,
                                                                                                 activity_key='concept:name',
                                                                                                 case_id_key='case:concept:name',
                                                                                                 timestamp_key='time:timestamp')
            tbr_diagnostics_inductive = pm4py.conformance_diagnostics_token_based_replay(RTFMP, net_inductive_t11,
                                                                                         im_inductive_t11, fm_inductive_t11,
                                                                                         activity_key='concept:name',
                                                                                         case_id_key='case:concept:name',
                                                                                         timestamp_key='time:timestamp')

            net_inductive_t12, im_inductive_t12, fm_inductive_t12 = pm4py.discover_petri_net_inductive(SEPSIS,
                                                                                                    activity_key='concept:name',
                                                                                                    case_id_key='case:concept:name',
                                                                                                    timestamp_key='time:timestamp')
            tbr_diagnostics_inductive = pm4py.conformance_diagnostics_token_based_replay(SEPSIS,
                                                                                         net_inductive_t12,
                                                                                         im_inductive_t12, fm_inductive_t12,
                                                                                         activity_key='concept:name',
                                                                                         case_id_key='case:concept:name',
                                                                                         timestamp_key='time:timestamp')



        elif param == "alignments":
            # 基于对齐方法的合规性检查

            net_inductive_a2, im_inductive_a2, fm_inductive_a2 = pm4py.discover_petri_net_inductive(BPIC13_cp,
                                                                                                 activity_key='concept:name',
                                                                                                 case_id_key='case:concept:name',
                                                                                                 timestamp_key='time:timestamp')
            tbr_diagnostics_inductive = pm4py.conformance_diagnostics_alignments(BPIC13_cp, net_inductive_a2,
                                                                                         im_inductive_a2, fm_inductive_a2,
                                                                                         activity_key='concept:name',
                                                                                         case_id_key='case:concept:name',
                                                                                         timestamp_key='time:timestamp')
            net_inductive_a3, im_inductive_a3, fm_inductive_a3 = pm4py.discover_petri_net_inductive(BPIC13_i,
                                                                                                 activity_key='concept:name',
                                                                                                 case_id_key='case:concept:name',
                                                                                                 timestamp_key='time:timestamp')
            tbr_diagnostics_inductive = pm4py.conformance_diagnostics_alignments(BPIC13_i, net_inductive_a3,
                                                                                         im_inductive_a3, fm_inductive_a3,
                                                                                         activity_key='concept:name',
                                                                                         case_id_key='case:concept:name',
                                                                                         timestamp_key='time:timestamp')
            # net_inductive_a4, im_inductive_a4, fm_inductive_a4 = pm4py.discover_petri_net_inductive(BPIC14_f,
            #                                                                                      activity_key='concept:name',
            #                                                                                      case_id_key='case:concept:name',
            #                                                                                      timestamp_key='time:timestamp')
            # tbr_diagnostics_inductive = pm4py.conformance_diagnostics_alignments(BPIC14_f, net_inductive_a4,
            #                                                                              im_inductive_a4, fm_inductive_a4,
            #                                                                              activity_key='concept:name',
            #                                                                              case_id_key='case:concept:name',
            #                                                                              timestamp_key='time:timestamp')
            net_inductive_a5, im_inductive_a5, fm_inductive_a5 = pm4py.discover_petri_net_inductive(BPIC15_1f,
                                                                                                 activity_key='concept:name',
                                                                                                 case_id_key='case:concept:name',
                                                                                                 timestamp_key='time:timestamp')
            tbr_diagnostics_inductive = pm4py.conformance_diagnostics_alignments(BPIC15_1f, net_inductive_a5,
                                                                                         im_inductive_a5, fm_inductive_a5,
                                                                                         activity_key='concept:name',
                                                                                         case_id_key='case:concept:name',
                                                                                         timestamp_key='time:timestamp')
            net_inductive_a6, im_inductive_a6, fm_inductive_a6 = pm4py.discover_petri_net_inductive(BPIC15_2f,
                                                                                                 activity_key='concept:name',
                                                                                                 case_id_key='case:concept:name',
                                                                                                 timestamp_key='time:timestamp')
            tbr_diagnostics_inductive = pm4py.conformance_diagnostics_alignments(BPIC15_2f, net_inductive_a6,
                                                                                         im_inductive_a6, fm_inductive_a6,
                                                                                         activity_key='concept:name',
                                                                                         case_id_key='case:concept:name',
                                                                                         timestamp_key='time:timestamp')
            net_inductive_a8, im_inductive_a8, fm_inductive_a8 = pm4py.discover_petri_net_inductive(BPIC15_4f,
                                                                                                 activity_key='concept:name',
                                                                                                 case_id_key='case:concept:name',
                                                                                                 timestamp_key='time:timestamp')
            tbr_diagnostics_inductive = pm4py.conformance_diagnostics_alignments(BPIC15_4f, net_inductive_a8,
                                                                                         im_inductive_a8, fm_inductive_a8,
                                                                                         activity_key='concept:name',
                                                                                         case_id_key='case:concept:name',
                                                                                         timestamp_key='time:timestamp')
            net_inductive_a9, im_inductive_a9, fm_inductive_a9 = pm4py.discover_petri_net_inductive(BPIC15_5f,
                                                                                                 activity_key='concept:name',
                                                                                                 case_id_key='case:concept:name',
                                                                                                 timestamp_key='time:timestamp')
            tbr_diagnostics_inductive = pm4py.conformance_diagnostics_alignments(BPIC15_5f, net_inductive_a9,
                                                                                         im_inductive_a9, fm_inductive_a9,
                                                                                         activity_key='concept:name',
                                                                                         case_id_key='case:concept:name',
                                                                                         timestamp_key='time:timestamp')
            # net_inductive_a10, im_inductive_a10, fm_inductive_a10 = pm4py.discover_petri_net_inductive(BPIC17_f,
            #                                                                                         activity_key='concept:name',
            #                                                                                         case_id_key='case:concept:name',
            #                                                                                         timestamp_key='time:timestamp')
            # tbr_diagnostics_inductive = pm4py.conformance_diagnostics_alignments(BPIC17_f, net_inductive_a10,
            #                                                                              im_inductive_a10,
            #                                                                              fm_inductive_a10,
            #                                                                              activity_key='concept:name',
            #                                                                              case_id_key='case:concept:name',
            #                                                                              timestamp_key='time:timestamp')
            net_inductive_a11, im_inductive_a11, fm_inductive_a11 = pm4py.discover_petri_net_inductive(RTFMP,
                                                                                                    activity_key='concept:name',
                                                                                                    case_id_key='case:concept:name',
                                                                                                    timestamp_key='time:timestamp')
            tbr_diagnostics_inductive = pm4py.conformance_diagnostics_alignments(RTFMP, net_inductive_a11,
                                                                                         im_inductive_a11,
                                                                                         fm_inductive_a11,
                                                                                         activity_key='concept:name',
                                                                                         case_id_key='case:concept:name',
                                                                                         timestamp_key='time:timestamp')

            net_inductive_a12, im_inductive_a12, fm_inductive_a12 = pm4py.discover_petri_net_inductive(SEPSIS,
                                                                                                    activity_key='concept:name',
                                                                                                    case_id_key='case:concept:name',
                                                                                                    timestamp_key='time:timestamp')
            tbr_diagnostics_inductive = pm4py.conformance_diagnostics_alignments(SEPSIS,net_inductive_a12,
                                                                                         im_inductive_a12,
                                                                                         fm_inductive_a12,
                                                                                         activity_key='concept:name',
                                                                                         case_id_key='case:concept:name',
                                                                                         timestamp_key='time:timestamp')

    else:
        print("没有提供任何命令行参数")


