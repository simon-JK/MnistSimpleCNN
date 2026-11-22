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