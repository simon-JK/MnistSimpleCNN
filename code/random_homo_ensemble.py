import random

import numpy as np
import argparse


def get_homo_ensembles(kernel_size:int):
    cnt = 1
    best = 10000
    curr = 10000
    n_trials = 30
    trial_list = [i for i in range(n_trials)]
    random.seed(42)

    KERNEL_SIZE = kernel_size
    acc_list = []
    boards = []

    for _ in range(1000):

        i, j, k = random.sample(trial_list, 3)

        w1 = np.loadtxt("../logs/modelM%d/wrong%03d.txt"%(KERNEL_SIZE, i)).astype(np.int64)
        w2 = np.loadtxt("../logs/modelM%d/wrong%03d.txt"%(KERNEL_SIZE, j)).astype(np.int64)
        w3 = np.loadtxt("../logs/modelM%d/wrong%03d.txt"%(KERNEL_SIZE, k)).astype(np.int64)

        board = np.zeros((10000))
        board[w1] += 1
        board[w2] += 1
        board[w3] += 1
        board = board // 2
        curr = np.sum(board)
        if curr < best:
            best = curr
        print("%4d %4d %4d %4d %4d %4d"%(cnt, len(w1), len(w2), len(w3), curr, best))
        acc_list.append((10000-curr)*0.01)
        boards.append(board)
        cnt += 1

    return acc_list, boards, (10000-best)*0.01