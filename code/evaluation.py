import os.path

import numpy as np

from random_ensemble import get_hetero_ensembles, get_level2_ensembles, get_level2_ensembles_best
from random_homo_ensemble import get_homo_ensembles


def get_log_metrics(file:str):
    val_acc = []
    for line in open(file, 'r'):
        line_values = line.split()
        if int(line_values[0]) < 50:
            continue
        val_acc.append(line_values[4])

    val_acc = np.array(val_acc).astype(np.float32)
    # print(val_acc)
    min_acc = val_acc.min()
    avg_acc = val_acc.mean()
    max_acc = val_acc.max()
    # print(min_acc, avg_acc, max_acc)
    return min_acc, avg_acc, max_acc


import scipy.stats

def mean_confidence_interval(data, confidence=0.95):
    a = 1.0 * np.array(data)
    n = len(a)
    m, se = np.mean(a), scipy.stats.sem(a)
    h = se * scipy.stats.t.ppf((1 + confidence) / 2., n-1)
    return m.round(4), h.round(4)


def eval_model_types(model_dir:str):
    min_list = []
    avg_list = []
    max_list = []
    for i in range(30):
        file = os.path.join(model_dir, "log%03d.out"%i)
        min_acc, avg_acc, max_acc = get_log_metrics(file)
        min_list.append(min_acc)
        avg_list.append(avg_acc)
        max_list.append(max_acc)
    min_mean, min_conf = mean_confidence_interval(min_list)
    avg_mean, avg_conf = mean_confidence_interval(avg_list)
    max_mean, max_conf = mean_confidence_interval(max_list)
    best = np.array(max_list).max()

    return min_mean, min_conf, avg_mean, avg_conf, max_mean, max_conf, best


def eval_individual_models():
    print('{0:5s}    {1:16s}    {2:16s}    {3:16s}    {4:7s}'.format("model", "min", "avg", "max", "best"))
    min_mean, min_conf, avg_mean, avg_conf, max_mean, max_conf, best = eval_model_types("../logs/modelM3")

    print('{0:5s}    {1:16s}    {2:16s}    {3:16s}    {4}'.format("M3",
                                                                  f"{min_mean:.4f} ± {min_conf:.4f}",
                                                                  f"{avg_mean:.4f} ± {avg_conf:.4f}",
                                                                  f"{max_mean:.4f} ± {max_conf:.4f}", f"{best:.2f}",))

    min_mean, min_conf, avg_mean, avg_conf, max_mean, max_conf, best = eval_model_types("../logs/modelM5")
    print('{0:5s}    {1:16s}    {2:16s}    {3:16s}    {4}'.format("M5",
                                                                  f"{min_mean:.4f} ± {min_conf:.4f}",
                                                                  f"{avg_mean:.4f} ± {avg_conf:.4f}",
                                                                  f"{max_mean:.4f} ± {max_conf:.4f}", f"{best:.2f}", ))

    min_mean, min_conf, avg_mean, avg_conf, max_mean, max_conf, best = eval_model_types("../logs/modelM7")
    print('{0:5s}    {1:16s}    {2:16s}    {3:16s}    {4}'.format("M7",
                                                                  f"{min_mean:.4f} ± {min_conf:.4f}",
                                                                  f"{avg_mean:.4f} ± {avg_conf:.4f}",
                                                                  f"{max_mean:.4f} ± {max_conf:.4f}", f"{best:.2f}", ))


def eval_level1_ensembles():
    print('{0:15s}    {1:20s}    {2:7s}'.format("configuration", "95% confidence range", "best"))

    acc_list, boards_m3, best = get_homo_ensembles(kernel_size=3)
    mean, mean_conf = mean_confidence_interval(acc_list)
    print('{0:15s}    {1:20s}    {2:7s}'.format("M3 + M3 + M3", f"{mean:.4f} ± {mean_conf:.4f}", f"{best:.2f}"))

    acc_list, boards_m5, best = get_homo_ensembles(kernel_size=5)
    mean, mean_conf = mean_confidence_interval(acc_list)
    print('{0:15s}    {1:20s}    {2:7s}'.format("M5 + M5 + M5", f"{mean:.4f} ± {mean_conf:.4f}", f"{best:.2f}"))

    acc_list, boards_m7, best = get_homo_ensembles(kernel_size=7)
    mean, mean_conf = mean_confidence_interval(acc_list)
    print('{0:15s}    {1:20s}    {2:7s}'.format("M7 + M7 + M7", f"{mean:.4f} ± {mean_conf:.4f}", f"{best:.2f}"))

    acc_list, best = get_hetero_ensembles()
    mean, mean_conf = mean_confidence_interval(acc_list)
    print('{0:15s}    {1:20s}    {2:7s}'.format("M3 + M5 + M7", f"{mean:.4f} ± {mean_conf:.4f}", f"{best:.2f}"))

    return boards_m3, boards_m5, boards_m7


def get_best_indices(best, all):
    indices = []
    for cur_best in best:
        for i, current in enumerate(all):
            if cur_best == current:
                indices.append(i)
    return indices



def eval_level2_ensembles(boards_m3, boards_m5, boards_m7):
    print('{0:30s}    {1:20s}    {2:7s}'.format("configuration", "95% confidence range", "best"))
    acc_list, best = get_level2_ensembles(boards_m3, boards_m5, boards_m7)
    mean, mean_conf = mean_confidence_interval(acc_list)
    print('{0:30s}    {1:20s}    {2:7s}'.format("ensemble of ensembles (random)", f"{mean:.4f} ± {mean_conf:.4f}", f"{best:.2f}"))

    # boards_m3_best = sorted(boards_m3, key=lambda x: len(x))[0:10]
    # print("indices of best m3: ", get_best_indices(boards_m3_best, boards_m3))
    # boards_m5_best = sorted(boards_m5, key=lambda x: len(x))[0:10]
    # print("indices of best m5: ", get_best_indices(boards_m5_best, boards_m5))
    # boards_m7_best = sorted(boards_m7, key=lambda x: len(x))[0:10]
    # print("indices of best m7: ", get_best_indices(boards_m7_best, boards_m7))

    print("using best ensembles from validation to test them on test set!-------------------------------")
    boards_m3_best = [boards_m3[i] for i in [429, 819, 93, 628, 416, 489, 93, 628, 670, 720, 895, 923]]

    boards_m5_best = [boards_m5[i] for i in [431, 878, 54, 82, 102, 364, 394, 488, 535, 548]]

    boards_m7_best = [boards_m7[i] for i in [12, 95, 260, 317, 327, 454, 521, 826, 8, 52, 219]]

    acc_list, best = get_level2_ensembles_best(boards_m3_best, boards_m5_best, boards_m7_best)
    mean, mean_conf = mean_confidence_interval(acc_list)
    print('{0:30s}    {1:20s}    {2:7s}'.format("ensemble of ensembles (best)", f"{mean:.4f} ± {mean_conf:.4f}", f"{best:.2f}"))


def eval_ensembles():
    boards_m3, boards_m5, boards_m7 = eval_level1_ensembles()
    eval_level2_ensembles(boards_m3, boards_m5, boards_m7)


def evalutate():
   eval_individual_models()
   eval_ensembles()


if __name__ == '__main__':
    evalutate()