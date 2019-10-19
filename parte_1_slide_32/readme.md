## Atividade

- Construir um sistema classificador para os dados do arquivo winequality. [Wine quality data](https://archive.ics.uci.edu/ml/datasets/wine+quality)

- Comparar SVM com outro método classificador e comparar as acurácias obtidas.

## Resultados

### SVM 

#### Kernel Linear

#### Confusion matrix

|  |  |  |
| :---: | :---: | :---: |
| 348 | 64 | 4 |
| 114 | 269 | 36 |
| 0 | 0 | 392 |

#### Classification report

|  | precision | recall | f1-score | support |
| :--- | :---: | :---: | :---: | :---: |
| A_WINE | 0.75 | 0.84 | 0.79 | 416 |
| B_WINE | 0.81 | 0.64 | 0.72 | 419 |
| C_WINE | 0.91 | 1.00 | 0.95 | 392 |
| accuracy |  |  | 0.82 | 1227 |
| macro avg | 0.82 | 0.83 | 0.82 | 1227 |
| weighted avg | 0.82 | 0.82 | 0.82 | 1227 |

#### Kernel RBF

#### Confusion matrix

|  |  |  |
| :---: | :---: | :---: |
| 264 | 79 | 53 |
| 85 | 258 | 70 |
| 0 | 128 | 290 |

#### Classification report

|  | precision | recall | f1-score | support |
| :--- | :---: | :---: | :---: | :---: |
| A_WINE | 0.76 | 0.67 | 0.71 | 396 |
| B_WINE | 0.55 | 0.62 | 0.59 | 413 |
| C_WINE | 0.70 | 0.69 | 0.70 | 418 |
| accuracy |  |  | 0.66 | 1227 |
| macro avg | 0.67 | 0.66 | 0.66 | 1227 |
| weighted avg | 0.67 | 0.66 | 0.66 | 1227 |

### Random Forest

#### Confusion matrix

|  |  |  |
| :---: | :---: | :---: |
| 418 | 4 | 0 |
| 28 | 354 | 1 |
| 0 | 0 | 422 |

#### Classification report

|  | precision | recall | f1-score | support |
| :--- | :---: | :---: | :---: | :---: |
| A_WINE | 0.94 | 0.99 | 0.96 | 422 |
| B_WINE | 0.99 | 0.92 | 0.96 | 383 |
| C_WINE | 1.00 | 1.00 | 1.00 | 422 |
| accuracy |  |  | 0.97 | 1227 |
| macro avg | 0.97 | 0.97 | 0.97 | 1227 |
| weighted avg | 0.97 | 0.97 | 0.97 | 1227 |
