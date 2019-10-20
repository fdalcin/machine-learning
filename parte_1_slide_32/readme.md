## Atividade

- Construir um sistema classificador para os dados do arquivo winequality. [Wine quality data](https://archive.ics.uci.edu/ml/datasets/wine+quality)

- Comparar SVM com outro método classificador e comparar as acurácias obtidas.

## Resultados

### SVM 

#### Kernel Linear

#### Confusion matrix

|  |  |  |
| :---: | :---: | :---: |
| 321 | 63 | 3 |
| 99 | 255 | 56 |
| 0 | 0 | 430 |

#### Classification report

|  | precision | recall | f1-score | support |
| :--- | :---: | :---: | :---: | :---: |
| A_WINE | 0.76 | 0.83 | 0.80 | 387 |
| B_WINE | 0.80 | 0.62 | 0.70 | 410 |
| C_WINE | 0.88 | 1.00 | 0.94 | 430 |
| accuracy |  |  | 0.82 | 1227 |
| macro avg | 0.82 | 0.82 | 0.81 | 1227 |
| weighted avg | 0.82 | 0.82 | 0.81 | 1227 |

#### Kernel RBF

#### Confusion matrix

|  |  |  |
| :---: | :---: | :---: |
| 301 | 79 | 31 |
| 83 | 248 | 61 |
| 0 | 143 | 280 |

#### Classification report

|  | precision | recall | f1-score | support |
| :--- | :---: | :---: | :---: | :---: |
| A_WINE | 0.78 | 0.73 | 0.76 | 411 |
| B_WINE | 0.53 | 0.63 | 0.57 | 393 |
| C_WINE | 0.75 | 0.66 | 0.70 | 423 |
| accuracy |  |  | 0.68 | 1227 |
| macro avg | 0.69 | 0.68 | 0.68 | 1227 |
| weighted avg | 0.69 | 0.68 | 0.68 | 1227 |

### Random Forest

#### Confusion matrix

|  |  |  |
| :---: | :---: | :---: |
| 376 | 0 | 0 |
| 24 | 368 | 4 |
| 0 | 0 | 455 |

#### Classification report

|  | precision | recall | f1-score | support |
| :--- | :---: | :---: | :---: | :---: |
| A_WINE | 0.94 | 1.00 | 0.97 | 376 |
| B_WINE | 1.00 | 0.93 | 0.96 | 396 |
| C_WINE | 0.99 | 1.00 | 1.00 | 444 |
| accuracy |  |  | 0.98 | 1227 |
| macro avg | 0.98 | 0.98 | 0.98 | 1227 |
| weighted avg | 0.98 | 0.98 | 0.98 | 1227 |
