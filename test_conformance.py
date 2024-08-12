import pm4py
import sys
if __name__ == "__main__":
    # 加载 .xes 文件
    BPIC13_cp = pm4py.read_xes('BPIC13_cp.xes')
    BPIC13_i = pm4py.read_xes('BPIC13_i.xes')
    BPIC15_1f = pm4py.read_xes("BPIC15_1f.xes")
    BPIC15_2f = pm4py.read_xes("BPIC15_2f.xes")
    BPIC15_4f = pm4py.read_xes("BPIC15_4f.xes")
    BPIC15_5f = pm4py.read_xes("BPIC15_5f.xes")


    if len(sys.argv) > 1:
        # 获取第一个命令行参数
        param = sys.argv[1]
        print(f"第一个命令行参数是: {param}")
        if param == "token":
            # 基于Token重演方法的合规性检查
            net_inductive_t1, im_inductive_t1, fm_inductive_t1 = pm4py.discover_petri_net_inductive(BPIC13_i,
                                                                                                 activity_key='concept:name',
                                                                                                 case_id_key='case:concept:name',
                                                                                                 timestamp_key='time:timestamp')
            tbr_diagnostics_inductive = pm4py.conformance_diagnostics_token_based_replay(BPIC13_i, net_inductive_t1,
                                                                                         im_inductive_t1, fm_inductive_t1,
                                                                                         activity_key='concept:name',
                                                                                         case_id_key='case:concept:name',
                                                                                         timestamp_key='time:timestamp')
            net_inductive_t2, im_inductive_t2, fm_inductive_t2 = pm4py.discover_petri_net_inductive(BPIC13_cp,
                                                                                                 activity_key='concept:name',
                                                                                                 case_id_key='case:concept:name',
                                                                                                 timestamp_key='time:timestamp')
            tbr_diagnostics_inductive = pm4py.conformance_diagnostics_token_based_replay(BPIC13_cp, net_inductive_t2,
                                                                                         im_inductive_t2, fm_inductive_t2,
                                                                                         activity_key='concept:name',
                                                                                         case_id_key='case:concept:name',
                                                                                         timestamp_key='time:timestamp')
            net_inductive_t3, im_inductive_t3, fm_inductive_t3 = pm4py.discover_petri_net_inductive(BPIC15_1f,
                                                                                                 activity_key='concept:name',
                                                                                                 case_id_key='case:concept:name',
                                                                                                 timestamp_key='time:timestamp')
            tbr_diagnostics_inductive = pm4py.conformance_diagnostics_token_based_replay(BPIC15_1f, net_inductive_t3,
                                                                                         im_inductive_t3, fm_inductive_t3,
                                                                                         activity_key='concept:name',
                                                                                         case_id_key='case:concept:name',
                                                                                         timestamp_key='time:timestamp')
            net_inductive_t4, im_inductive_t4, fm_inductive_t4 = pm4py.discover_petri_net_inductive(BPIC15_2f,
                                                                                                 activity_key='concept:name',
                                                                                                 case_id_key='case:concept:name',
                                                                                                 timestamp_key='time:timestamp')
            tbr_diagnostics_inductive = pm4py.conformance_diagnostics_token_based_replay(BPIC15_2f, net_inductive_t4,
                                                                                         im_inductive_t4, fm_inductive_t4,
                                                                                         activity_key='concept:name',
                                                                                         case_id_key='case:concept:name',
                                                                                         timestamp_key='time:timestamp')

            net_inductive_t5, im_inductive_t5, fm_inductive_t5 = pm4py.discover_petri_net_inductive(BPIC15_4f,
                                                                                                 activity_key='concept:name',
                                                                                                 case_id_key='case:concept:name',
                                                                                                 timestamp_key='time:timestamp')
            tbr_diagnostics_inductive = pm4py.conformance_diagnostics_token_based_replay(BPIC15_4f, net_inductive_t5,
                                                                                         im_inductive_t5, fm_inductive_t5,
                                                                                         activity_key='concept:name',
                                                                                         case_id_key='case:concept:name',
                                                                                         timestamp_key='time:timestamp')
            net_inductive_t6, im_inductive_t6, fm_inductive_t6 = pm4py.discover_petri_net_inductive(BPIC15_5f,
                                                                                                 activity_key='concept:name',
                                                                                                 case_id_key='case:concept:name',
                                                                                                 timestamp_key='time:timestamp')
            tbr_diagnostics_inductive = pm4py.conformance_diagnostics_token_based_replay(BPIC15_5f, net_inductive_t6,
                                                                                         im_inductive_t6, fm_inductive_t6,
                                                                                         activity_key='concept:name',
                                                                                         case_id_key='case:concept:name',
                                                                                         timestamp_key='time:timestamp')


        elif param == "alignments":
            # 基于对齐方法的合规性检查

            net_inductive_a1, im_inductive_a1, fm_inductive_a1 = pm4py.discover_petri_net_inductive(BPIC13_cp,
                                                                                                 activity_key='concept:name',
                                                                                                 case_id_key='case:concept:name',
                                                                                                 timestamp_key='time:timestamp')
            tbr_diagnostics_inductive = pm4py.conformance_diagnostics_alignments(BPIC13_cp, net_inductive_a1,
                                                                                         im_inductive_a1, fm_inductive_a1,
                                                                                         activity_key='concept:name',
                                                                                         case_id_key='case:concept:name',
                                                                                         timestamp_key='time:timestamp')
            net_inductive_a2, im_inductive_a2, fm_inductive_a2 = pm4py.discover_petri_net_inductive(BPIC13_i,
                                                                                                 activity_key='concept:name',
                                                                                                 case_id_key='case:concept:name',
                                                                                                 timestamp_key='time:timestamp')
            tbr_diagnostics_inductive = pm4py.conformance_diagnostics_alignments(BPIC13_i, net_inductive_a2,
                                                                                         im_inductive_a2, fm_inductive_a2,
                                                                                         activity_key='concept:name',
                                                                                         case_id_key='case:concept:name',
                                                                                         timestamp_key='time:timestamp')

            net_inductive_a3, im_inductive_a3, fm_inductive_a3 = pm4py.discover_petri_net_inductive(BPIC15_1f,
                                                                                                 activity_key='concept:name',
                                                                                                 case_id_key='case:concept:name',
                                                                                                 timestamp_key='time:timestamp')
            tbr_diagnostics_inductive = pm4py.conformance_diagnostics_alignments(BPIC15_1f, net_inductive_a3,
                                                                                         im_inductive_a3, fm_inductive_a3,
                                                                                         activity_key='concept:name',
                                                                                         case_id_key='case:concept:name',
                                                                                         timestamp_key='time:timestamp')
            net_inductive_a4, im_inductive_a4, fm_inductive_a4 = pm4py.discover_petri_net_inductive(BPIC15_2f,
                                                                                                 activity_key='concept:name',
                                                                                                 case_id_key='case:concept:name',
                                                                                                 timestamp_key='time:timestamp')
            tbr_diagnostics_inductive = pm4py.conformance_diagnostics_alignments(BPIC15_2f, net_inductive_a4,
                                                                                         im_inductive_a4, fm_inductive_a4,
                                                                                         activity_key='concept:name',
                                                                                         case_id_key='case:concept:name',
                                                                                         timestamp_key='time:timestamp')
            net_inductive_a5, im_inductive_a5, fm_inductive_a5 = pm4py.discover_petri_net_inductive(BPIC15_4f,
                                                                                                 activity_key='concept:name',
                                                                                                 case_id_key='case:concept:name',
                                                                                                 timestamp_key='time:timestamp')
            tbr_diagnostics_inductive = pm4py.conformance_diagnostics_alignments(BPIC15_4f, net_inductive_a5,
                                                                                         im_inductive_a5, fm_inductive_a5,
                                                                                         activity_key='concept:name',
                                                                                         case_id_key='case:concept:name',
                                                                                         timestamp_key='time:timestamp')
            net_inductive_a6, im_inductive_a6, fm_inductive_a6 = pm4py.discover_petri_net_inductive(BPIC15_5f,
                                                                                                 activity_key='concept:name',
                                                                                                 case_id_key='case:concept:name',
                                                                                                 timestamp_key='time:timestamp')
            tbr_diagnostics_inductive = pm4py.conformance_diagnostics_alignments(BPIC15_5f, net_inductive_a6,
                                                                                         im_inductive_a6, fm_inductive_a6,
                                                                                         activity_key='concept:name',
                                                                                         case_id_key='case:concept:name',
                                                                                         timestamp_key='time:timestamp')

    else:
        print("没有提供任何命令行参数")


