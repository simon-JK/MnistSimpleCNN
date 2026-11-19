import numpy as np 

cnt = 1
best = 10000
curr = 10000
n_trials=5

for i in range(n_trials):
    for j in range(n_trials):
        for k in range(n_trials):
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
            print("%4d %4d %4d"%(cnt, curr, best))
            cnt += 1
