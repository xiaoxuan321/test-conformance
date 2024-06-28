import pm4py
import sys
if __name__ == "__main__":
    BPIC13_i = pm4py.read_xes('BPIC13_i.xes')
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


