import random

import numpy as np


def get_hetero_ensembles():
    cnt = 1
    best = 10000
    curr = 10000
    n_trials=30

    random.seed(42)

    acc_list = []

    for _ in range(1000):
        i = random.randint(0, 29)
        j = random.randint(0, 29)
        k = random.randint(0, 29)
        # w1 = np.loadtxt("../logs/modela1/wrong%03d.txt"%(301+i)).astype(np.int64)
        # w2 = np.loadtxt("../logs/modela3/wrong%03d.txt"%(301+j)).astype(np.int64)
        # w3 = np.loadtxt("../logs/modela4/wrong%03d.txt"%(301+k)).astype(np.int64)
        w1 = np.loadtxt("../logs/modelM%d/wrong%03d.txt" % (3, i)).astype(np.int64)
        w2 = np.loadtxt("../logs/modelM%d/wrong%03d.txt" % (5, j)).astype(np.int64)
        w3 = np.loadtxt("../logs/modelM%d/wrong%03d.txt" % (7, k)).astype(np.int64)

        board = np.zeros((10000))
        board[w1] += 1
        board[w2] += 1
        board[w3] += 1
        board = board // 2
        curr = np.sum(board)
        if curr < best:
            best = curr
        #print("%4d %4d %4d"%(cnt, curr, best))
        acc_list.append((10000-curr)*0.01)
        cnt += 1

    return acc_list, (10000-best)*0.01


def get_level2_ensembles(boards_m3, boards_m5, boards_m7):
    cnt = 1
    best = 10000
    curr = 10000

    random.seed(42)

    acc_list = []

    for _ in range(1000):
        i = random.randint(0, len(boards_m3)-1)
        j = random.randint(0, len(boards_m5)-1)
        k = random.randint(0, len(boards_m7)-1)

        w1 = boards_m3[i]
        w2 = boards_m5[j]
        w3 = boards_m7[k]

        board = np.zeros((10000))
        board[w1] += 1
        board[w2] += 1
        board[w3] += 1
        board = board // 2
        curr = np.sum(board)
        if curr < best:
            best = curr
        # print("%4d %4d %4d"%(cnt, curr, best))
        acc_list.append((10000 - curr) * 0.01)
        cnt += 1

    return acc_list, (10000-best)*0.01


def get_level2_ensembles_best(boards_m3, boards_m5, boards_m7):
    cnt = 1
    best = 10000
    curr = 10000

    random.seed(42)

    acc_list = []

    for i in range(len(boards_m3)):
        for j in range(len(boards_m5)):
            for k in range(len(boards_m7)):

                w1 = boards_m3[i]
                w2 = boards_m5[j]
                w3 = boards_m7[k]

                board = np.zeros((10000))
                board[w1] += 1
                board[w2] += 1
                board[w3] += 1
                board = board // 2
                curr = np.sum(board)
                if curr < best:
                    best = curr
                # print("%4d %4d %4d"%(cnt, curr, best))
                acc_list.append((10000 - curr) * 0.01)
                cnt += 1

    return acc_list, (10000-best)*0.01