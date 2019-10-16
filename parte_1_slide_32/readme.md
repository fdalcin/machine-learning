## Atividade

- Construir um sistema classificador para os dados do arquivo winequality. [Wine quality data](https://archive.ics.uci.edu/ml/datasets/wine+quality)

- Comparar SVM com outro método classificador e comparar as acurácias obtidas.

## Resultados

### SVM 

#### Kernel Linear

#### Confusion matrix

|  |  |  |
| :---: | :---: | :---: |
| 322 | 72 | 1 |
| 111 | 285 | 44 |
| 0 | 0 | 392 |

#### Classification report

|  | precision | recall | f1-score | support |
| :--- | :---: | :---: | :---: | :---: |
| A_WINE | 0.74 | 0.82 | 0.78 | 395 |
| B_WINE | 0.80 | 0.65 | 0.72 | 440 |
| C_WINE | 0.90 | 1.00 | 0.95 | 392 |
| accuracy |  |  | 0.81 | 1227 |
| macro avg | 0.81 | 0.82 | 0.81 | 1227 |
| weighted avg | 0.81 | 0.81 | 0.81 | 1227 |

Model score: **83.05%**

Cross validation score  
Mean precision: **0.8190135948062778**

Cross validate score  
Mean precision: **0.8190135948062778**

#### Kernel RBF

#### Confusion matrix

|  |  |  |
| :---: | :---: | :---: |
| 256 | 94 | 65 |
| 92 | 239 | 63 |
| 0 | 134 | 284 |

#### Classification report

|  | precision | recall | f1-score | support |
| :--- | :---: | :---: | :---: | :---: |
| A_WINE | 0.74 | 0.62 | 0.67 | 415 |
| B_WINE | 0.51 | 0.61 | 0.56 | 394 |
| C_WINE | 0.69 | 0.68 | 0.68 | 418 |
| accuracy |  |  | 0.63 | 1227 |
| macro avg | 0.65 | 0.63 | 0.64 | 1227 |
| weighted avg | 0.65 | 0.63 | 0.64 | 1227 |

Model score: **64.38%**

Cross validation score  
Mean precision: **0.5918733850129198**

Cross validate score  
Mean precision: **0.5918733850129198**

### Random Forest

#### Confusion matrix

|  |  |  |
| :---: | :---: | :---: |
| 418 | 0 | 0 |
| 21 | 381 | 3 |
| 0 | 0 | 404 |

#### Classification report

|  | precision | recall | f1-score | support |
| :--- | :---: | :---: | :---: | :---: |
| A_WINE | 0.95 | 1.00 | 0.98 | 418 |
| B_WINE | 1.00 | 0.94 | 0.97 | 405 |
| C_WINE | 0.99 | 1.00 | 1.00 | 404 |
| accuracy |  |  | 0.98 | 1227 |
| macro avg | 0.98 | 0.98 | 0.98 | 1227 |
| weighted avg | 0.98 | 0.98 | 0.98 | 1227 |

Model score: **99.43%**

Cross validation score  
Mean precision: **0.9479908573811013**

Cross validate score  
Mean precision: **0.94717784925102**