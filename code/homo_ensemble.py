import numpy as np 
import argparse

cnt = 1
best = 10000
curr = 10000
n_trials = 20

p = argparse.ArgumentParser()
p.add_argument("--kernel_size", default=5, type=int)
args = p.parse_args()
KERNEL_SIZE = args.kernel_size
acc_list = []

for i in range(n_trials):
    for j in range(i+1,n_trials):
        for k in range(j+1,n_trials):
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
            acc_list.append(curr)
            cnt += 1

acc_list = np.array(acc_list)
mean_acc = acc_list.mean()
print(f"mean: {mean_acc}")
