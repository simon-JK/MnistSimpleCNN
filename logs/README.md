Model logs directory

models trained with 50k samples and tested on 10k validation samples:
model    min                 avg                 max                 best   
M3       99.4793 ± 0.0279    99.6159 ± 0.0072    99.6847 ± 0.0081    99.72
M5       99.5077 ± 0.0146    99.6262 ± 0.0076    99.7043 ± 0.0093    99.76
M7       99.5013 ± 0.0162    99.6281 ± 0.0092    99.7053 ± 0.0096    99.76
configuration      95% confidence range    best   
M3 + M3 + M3       99.7125 ± 0.0012        99.78  
M5 + M5 + M5       99.7408 ± 0.0014        99.81  
M7 + M7 + M7       99.7310 ± 0.0014        99.79  
M3 + M5 + M7       99.7354 ± 0.0013        99.80  
configuration                     95% confidence range    best   
ensemble of ensembles (random)    99.7484 ± 0.0011        99.80  
ensemble of ensembles (best)      99.8054 ± 0.0008        99.84
indices of best m3:  [429, 819, 93, 628, 416, 489, 93, 628, 670, 720, 895, 923]
indices of best m5:  [431, 878, 54, 82, 102, 364, 394, 488, 535, 548]
indices of best m7:  [12, 95, 260, 317, 327, 454, 521, 826, 8, 52, 219]


eval on testset with best ensembles of val_set
model    min                 avg                 max                 best   
M3       99.4793 ± 0.0279    99.6159 ± 0.0072    99.6847 ± 0.0081    99.72      same because
M5       99.5077 ± 0.0146    99.6262 ± 0.0076    99.7043 ± 0.0093    99.76      logs were used
M7       99.5013 ± 0.0162    99.6281 ± 0.0092    99.7053 ± 0.0096    99.76      thus this are still val accs
configuration      95% confidence range    best   
M3 + M3 + M3       99.7075 ± 0.0017        99.79  
M5 + M5 + M5       99.7228 ± 0.0016        99.80  
M7 + M7 + M7       99.7309 ± 0.0017        99.81  
M3 + M5 + M7       99.7305 ± 0.0017        99.82  
configuration                     95% confidence range    best   
ensemble of ensembles (random)    99.7417 ± 0.0015        99.82  
using best ensembles from validation to test them on test set!-------------------------------
ensemble of ensembles (best)      99.7438 ± 0.0011        99.81  
that the best accs here are much more similar to the random ensemble shows that overfitting on val/test set took place 
by using "best" in the eval above and below, thus "best" ensembles are not very trustworthy in generalization



evaluation on test samples DIFFERENT BEST ENSEMBLES THEN USED IN VALSET OVERFITTING TO TESTSET POSSIBLE!!!!:
model    min                 avg                 max                 best   
M3       99.4793 ± 0.0279    99.6159 ± 0.0072    99.6847 ± 0.0081    99.72      same because
M5       99.5077 ± 0.0146    99.6262 ± 0.0076    99.7043 ± 0.0093    99.76      logs were used
M7       99.5013 ± 0.0162    99.6281 ± 0.0092    99.7053 ± 0.0096    99.76      thus this are still val accs
configuration      95% confidence range    best   
M3 + M3 + M3       99.7075 ± 0.0017        99.79  
M5 + M5 + M5       99.7228 ± 0.0016        99.80  
M7 + M7 + M7       99.7309 ± 0.0017        99.81  
M3 + M5 + M7       99.7305 ± 0.0017        99.82  
configuration                     95% confidence range    best   
ensemble of ensembles (random)    99.7417 ± 0.0015        99.82  
ensemble of ensembles (best)      99.8113 ± 0.0008        99.85  
indices of best m3:  [76, 237, 302, 848, 633, 692, 714, 829, 302, 848, 8, 39, 709]
indices of best m5:  [87, 629, 7, 319, 524, 642, 935, 222, 402, 423]
indices of best m7:  [118, 105, 937, 148, 252, 512, 539, 548, 597, 799, 815]
