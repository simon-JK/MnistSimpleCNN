# MNIST Evaluation Results

I forked this project from https://github.com/ansh941/MnistSimpleCNN/tree/master 
and read their paper (https://arxiv.org/abs/2008.10400)
because I wanted to check if I get the same results when I use my custom data split with
50k training, 10k validation and 10k the original test data.
And I also checked if the best ensembles selected for the val data are 
still as good on the original test data or if they overfit.


## 1. Individual Models

Models trained with 50k samples and evaluated on 10k validation samples.

| Model | Min Accuracy | Avg Accuracy | Max Accuracy | Best |
|:------|-------------:|-------------:|-------------:|-----:|
| M3 | 99.4793 ± 0.0279 | 99.6159 ± 0.0072 | 99.6847 ± 0.0081 | **99.72** |
| M5 | 99.5077 ± 0.0146 | 99.6262 ± 0.0076 | 99.7043 ± 0.0093 | **99.76** |
| M7 | 99.5013 ± 0.0162 | 99.6281 ± 0.0092 | 99.7053 ± 0.0096 | **99.76** |

## 2. Ensemble Evaluation on Validation Set

| Configuration | 95% Confidence Range | Best |
|:--------------|---------------------:|-----:|
| M3 + M3 + M3 | 99.7125 ± 0.0012 | **99.78** |
| M5 + M5 + M5 | 99.7408 ± 0.0014 | **99.81** |
| M7 + M7 + M7 | 99.7310 ± 0.0014 | **99.79** |
| M3 + M5 + M7 | 99.7354 ± 0.0013 | **99.80** |

### Ensemble of Ensembles

| Configuration | 95% Confidence Range | Best |
|:--------------|---------------------:|-----:|
| Random | 99.7484 ± 0.0011 | **99.80** |
| Best | **99.8054 ± 0.0008** | **99.84** |

### Selected Model Indices

```python
indices_best_m3 = [429, 819, 93, 628, 416, 489, 93, 628, 670, 720, 895, 923]
indices_best_m5 = [431, 878, 54, 82, 102, 364, 394, 488, 535, 548]
indices_best_m7 = [12, 95, 260, 317, 327, 454, 521, 826, 8, 52, 219]
```

---

## 3. Evaluation on Test Set Using Best Validation Ensembles

The best ensembles selected on the validation set are evaluated on the test set.

**Important:** The individual model results below are still validation accuracies because the original logs were reused.

### Individual Models

| Model | Min Accuracy | Avg Accuracy | Max Accuracy | Best |
|:------|-------------:|-------------:|-------------:|-----:|
| M3 | 99.4793 ± 0.0279 | 99.6159 ± 0.0072 | 99.6847 ± 0.0081 | 99.72 |
| M5 | 99.5077 ± 0.0146 | 99.6262 ± 0.0076 | 99.7043 ± 0.0093 | 99.76 |
| M7 | 99.5013 ± 0.0162 | 99.6281 ± 0.0092 | 99.7053 ± 0.0096 | 99.76 |

### Ensemble Results

| Configuration | 95% Confidence Range | Best |
|:--------------|---------------------:|-----:|
| M3 + M3 + M3 | 99.7075 ± 0.0017 | 99.79 |
| M5 + M5 + M5 | 99.7228 ± 0.0016 | 99.80 |
| M7 + M7 + M7 | 99.7309 ± 0.0017 | 99.81 |
| M3 + M5 + M7 | 99.7305 ± 0.0017 | 99.82 |

### Ensemble of Ensembles

| Configuration | 95% Confidence Range | Best |
|:--------------|---------------------:|-----:|
| Random | 99.7417 ± 0.0015 | **99.82** |
| Best | 99.7438 ± 0.0011 | 99.81 |

**Observation:**

The best ensemble performs similarly to the random ensemble when evaluated on the test set. This suggests that selecting the best ensembles based on validation performance may have caused overfitting to the validation set.

Consequently, the best validation results should not be considered reliable indicators of generalization performance.

---

## 4. Evaluation on Test Set Using Different Best Ensembles

In this experiment, different best ensembles are selected for the test set instead of reusing the ensembles selected on the validation set.

**Warning:** Selecting the best ensembles directly based on test-set performance introduces the possibility of overfitting to the test set. These results should therefore not be interpreted as unbiased estimates of generalization performance.

### Individual Models

The individual model results are unchanged because the original validation logs were reused.

| Model | Min Accuracy | Avg Accuracy | Max Accuracy | Best |
|:------|-------------:|-------------:|-------------:|-----:|
| M3 | 99.4793 ± 0.0279 | 99.6159 ± 0.0072 | 99.6847 ± 0.0081 | 99.72 |
| M5 | 99.5077 ± 0.0146 | 99.6262 ± 0.0076 | 99.7043 ± 0.0093 | 99.76 |
| M7 | 99.5013 ± 0.0162 | 99.6281 ± 0.0092 | 99.7053 ± 0.0096 | 99.76 |

### Ensemble Results

| Configuration | 95% Confidence Range | Best |
|:--------------|---------------------:|-----:|
| M3 + M3 + M3 | 99.7075 ± 0.0017 | 99.79 |
| M5 + M5 + M5 | 99.7228 ± 0.0016 | 99.80 |
| M7 + M7 + M7 | 99.7309 ± 0.0017 | 99.81 |
| M3 + M5 + M7 | 99.7305 ± 0.0017 | 99.82 |

### Ensemble of Ensembles

| Configuration | 95% Confidence Range | Best |
|:--------------|---------------------:|-----:|
| Random | 99.7417 ± 0.0015 | 99.82 |
| Best | **99.8113 ± 0.0008** | **99.85** |

### Selected Model Indices

```python
indices_best_m3 = [76, 237, 302, 848, 633, 692, 714, 829, 302, 848, 8, 39, 709]
indices_best_m5 = [87, 629, 7, 319, 524, 642, 935, 222, 402, 423]
indices_best_m7 = [118, 105, 937, 148, 252, 512, 539, 548, 597, 799, 815]
```

**Observation:**

The best ensemble achieves 99.8113% average accuracy when selected directly on the test set, compared to 99.7438% when using the validation-selected ensemble.

This difference further illustrates the risk of overfitting when selecting ensembles based on the evaluation dataset itself. The 99.85% best result should therefore not be interpreted as an unbiased test accuracy.