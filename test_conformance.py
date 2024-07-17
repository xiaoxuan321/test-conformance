import pm4py
import sys
if __name__ == "__main__":
    BPIC12_output_file = '/app/data/BPIC12.xes'
    BPIC13_cp_output_file = '/app/data/BPIC13_cp.xes'
    BPIC13_i_output_file = '/app/data/BPIC13_i.xes'
    BPIC14_f_output_file = '/app/data/BPIC14_f.xes'
    BPIC15_1f_output_file = '/app/data/BPIC15_1f.xes'
    BPIC15_2f_output_file = '/app/data/BPIC15_2f.xes'
    BPIC15_3f_output_file = '/app/data/BPIC15_3f.xes'
    BPIC15_4f_output_file = '/app/data/BPIC15_4f.xes'
    BPIC15_5f_output_file = '/app/data/BPIC15_5f.xes'
    BPIC17_f_output_file = '/app/data/BPIC17_f.xes'
    RTFMP_output_file = '/app/data/RTFMP.xes'
    SEPSIS_output_file = '/app/data/SEPSIS.xes'
    # 加载解压后的 .xes 文件
    BPIC12 = pm4py.read_xes(BPIC12_output_file)
    BPIC13_cp = pm4py.read_xes(BPIC13_cp_output_file)
    BPIC13_i = pm4py.read_xes(BPIC13_i_output_file)
    BPIC14_f = pm4py.read_xes(BPIC14_f_output_file)
    BPIC15_1f = pm4py.read_xes(BPIC15_1f_output_file)
    BPIC15_2f = pm4py.read_xes(BPIC15_2f_output_file)
    BPIC15_3f = pm4py.read_xes(BPIC15_3f_output_file)
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
            net, im, fm = pm4py.discover_petri_net_inductive(BPIC13_i, activity_key='concept:name',
                                                             case_id_key='case:concept:name', timestamp_key='time:timestamp')
            tbr_diagnostics = pm4py.conformance_diagnostics_token_based_replay(BPIC13_i, net, im, fm,
                                                                               activity_key='concept:name',
                                                                               case_id_key='case:concept:name',
                                                                               timestamp_key='time:timestamp')
        elif param == "alignments":
            # 基于对齐方法的合规性检查

            net, im, fm = pm4py.discover_petri_net_inductive(BPIC13_i, activity_key='concept:name',
                                                             case_id_key='case:concept:name', timestamp_key='time:timestamp')
            alignments_diagnostics = pm4py.conformance_diagnostics_alignments(BPIC13_i, net, im, fm,
                                                                              activity_key='concept:name',
                                                                              case_id_key='case:concept:name',
                                                                              timestamp_key='time:timestamp')

        elif param == "declare":
            # Declare模型的一致性检查
            declare_model = pm4py.discover_declare(BPIC13_i)
            conf_result = pm4py.conformance_declare(BPIC13_i, declare_model)

        elif param == "skeleton":
            # 日志Skeleton的合规性检查
            log_skeleton = pm4py.discover_log_skeleton(BPIC13_i, noise_threshold=0.1, activity_key='concept:name',
                                                       case_id_key='case:concept:name', timestamp_key='time:timestamp')
            conformance_lsk = pm4py.conformance_log_skeleton(BPIC13_i, log_skeleton, activity_key='concept:name',
                                                             case_id_key='case:concept:name', timestamp_key='time:timestamp')
    else:
        print("没有提供任何命令行参数")


