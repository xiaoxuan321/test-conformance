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
            net_inductive, im_inductive, fm_inductive = pm4py.discover_petri_net_inductive(BPIC13_i, activity_key='concept:name',
                                                             case_id_key='case:concept:name', timestamp_key='time:timestamp')
            tbr_diagnostics_inductive = pm4py.conformance_diagnostics_token_based_replay(BPIC13_i, net_inductive, im_inductive, fm_inductive,
                                                                               activity_key='concept:name',
                                                                               case_id_key='case:concept:name',
                                                                               timestamp_key='time:timestamp')

            net_alpha, im_alpha, fm_alpha = pm4py.discover_petri_net_alpha(BPIC13_i, activity_key='concept:name',
                                                             case_id_key='case:concept:name',timestamp_key='time:timestamp')
            tbr_diagnostics_alpha = pm4py.conformance_diagnostics_token_based_replay(BPIC13_i, net_alpha, im_alpha, fm_alpha,
                                                                               activity_key='concept:name',
                                                                               case_id_key='case:concept:name',
                                                                               timestamp_key='time:timestamp')

            net_alpha_plus, im_alpha_plus, fm_alpha_plus = pm4py.discover_petri_net_alpha_plus(BPIC13_i, activity_key='concept:name',
                                                                           case_id_key='case:concept:name',
                                                                           timestamp_key='time:timestamp')
            tbr_diagnostics_alpha_plus = pm4py.conformance_diagnostics_token_based_replay(BPIC13_i, net_alpha_plus, im_alpha_plus,
                                                                                     fm_alpha_plus,
                                                                                     activity_key='concept:name',
                                                                                     case_id_key='case:concept:name',
                                                                                     timestamp_key='time:timestamp')

            net_ilp, im_ilp, fm_ilp = pm4py.discover_petri_net_ilp(BPIC13_i, activity_key='concept:name',
                                                                           case_id_key='case:concept:name', timestamp_key='time:timestamp')
            tbr_diagnostics_ilp = pm4py.conformance_diagnostics_token_based_replay(BPIC13_i, net_ilp, im_ilp,
                                                                                     fm_ilp,
                                                                                     activity_key='concept:name',
                                                                                     case_id_key='case:concept:name',
                                                                                     timestamp_key='time:timestamp')

            net_heuristics, im_heuristics, fm_heuristics = pm4py.discover_petri_net_heuristics(BPIC13_i, activity_key='concept:name',
                                                                   case_id_key='case:concept:name',timestamp_key='time:timestamp')
            tbr_diagnostics_heuristics = pm4py.conformance_diagnostics_token_based_replay(BPIC13_i, net_heuristics, im_heuristics,
                                                                                   fm_heuristics,
                                                                                   activity_key='concept:name',
                                                                                   case_id_key='case:concept:name',
                                                                                   timestamp_key='time:timestamp')
        elif param == "alignments":
            # 基于对齐方法的合规性检查
            net_inductive, im_inductive, fm_inductive = pm4py.discover_petri_net_inductive(BPIC13_i,activity_key='concept:name',
                                                                                           case_id_key='case:concept:name',
                                                                                           timestamp_key='time:timestamp')
            alignments_diagnostics_inductive = pm4py.conformance_diagnostics_alignments(BPIC13_i, net_inductive,
                                                                                         im_inductive, fm_inductive,
                                                                                         activity_key='concept:name',
                                                                                         case_id_key='case:concept:name',
                                                                                         timestamp_key='time:timestamp')

            net_alpha, im_alpha, fm_alpha = pm4py.discover_petri_net_alpha(BPIC13_i, activity_key='concept:name',
                                                                           case_id_key='case:concept:name',
                                                                           timestamp_key='time:timestamp')
            alignments_diagnostics_alpha = pm4py.conformance_diagnostics_alignments(BPIC13_i, net_alpha, im_alpha,
                                                                                     fm_alpha,
                                                                                     activity_key='concept:name',
                                                                                     case_id_key='case:concept:name',
                                                                                     timestamp_key='time:timestamp')

            net_alpha_plus, im_alpha_plus, fm_alpha_plus = pm4py.discover_petri_net_alpha_plus(BPIC13_i,
                                                                                               activity_key='concept:name',
                                                                                               case_id_key='case:concept:name',
                                                                                               timestamp_key='time:timestamp')
            alignments_diagnostics_alpha_plus = pm4py.conformance_diagnostics_alignments(BPIC13_i, net_alpha_plus,
                                                                                          im_alpha_plus,
                                                                                          fm_alpha_plus,
                                                                                          activity_key='concept:name',
                                                                                          case_id_key='case:concept:name',
                                                                                          timestamp_key='time:timestamp')

            net_ilp, im_ilp, fm_ilp = pm4py.discover_petri_net_ilp(BPIC13_i, activity_key='concept:name',
                                                                   case_id_key='case:concept:name',
                                                                   timestamp_key='time:timestamp')
            alignments_diagnostics_ilp = pm4py.conformance_diagnostics_alignments(BPIC13_i, net_ilp, im_ilp,
                                                                                   fm_ilp,
                                                                                   activity_key='concept:name',
                                                                                   case_id_key='case:concept:name',
                                                                                   timestamp_key='time:timestamp')

            net_heuristics, im_heuristics, fm_heuristics = pm4py.discover_petri_net_heuristics(BPIC13_i,
                                                                                               activity_key='concept:name',
                                                                                               case_id_key='case:concept:name',
                                                                                               timestamp_key='time:timestamp')
            alignments_diagnostics_heuristics = pm4py.conformance_diagnostics_alignments(BPIC13_i, net_heuristics,
                                                                                          im_heuristics,
                                                                                          fm_heuristics,
                                                                                          activity_key='concept:name',
                                                                                          case_id_key='case:concept:name',
                                                                                          timestamp_key='time:timestamp')

    else:
        print("没有提供任何命令行参数")


