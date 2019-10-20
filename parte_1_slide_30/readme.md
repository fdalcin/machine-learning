## Atividade

Construir um sistema classificador para os dados do arquivo diabetes.csv

- Qual algoritmo foi selecionado? Por que?

- Qual é a acurácia do modelo obtido?

## Resultados

### Decision Tree

#### Confusion matrix

|  |  |
| :---: | :---: |
| 121 | 34 |
| 28 | 48 |

#### Classification report

|  | precision | recall | f1-score | support |
| :--- | :---: | :---: | :---: | :---: |
| tested_negative | 0.81 | 0.78 | 0.80 | 155 |
| tested_positive | 0.59 | 0.63 | 0.61 | 76 |
| |
| accuracy |  |  | 0.73 | 231 |
| macro avg | 0.70 | 0.71 | 0.70 | 231 |
| weighted avg | 0.74 | 0.73 | 0.73 | 231 |

```json
{
  'accuracy': 0.6835144927536232, 
  'auc_roc': 0.6589661677761522
}
```

### Random Forest

#### Confusion matrix

|  |  |
| :---: | :---: |
| 117 | 26 |
| 36 | 52 |

#### Classification report

|  | precision | recall | f1-score | support |
| :--- | :---: | :---: | :---: | :---: |
| tested_negative | 0.76 | 0.82 | 0.79 | 143 |
| tested_positive | 0.67 | 0.59 | 0.63 | 88 |
| |
| accuracy |  |  | 0.73 | 231 |
| macro avg | 0.72 | 0.70 | 0.71 | 231 |
| weighted avg | 0.73 | 0.73 | 0.73 | 231 |

```json
{
  'accuracy': 0.7063405797101449, 
  'auc_roc': 0.8085557416439771
}
```

#### Algoritmo selecionado
Foi selecionado o modelo de **Regressão Logística** apresentado anteriormente - **[parte_1_slide_18](https://github.com/fdalcin/machine-learning/tree/master/parte_1_slide_18)**, uma vez que o mesmo apresentou uma melhor acurácia.

#### Acurácia do modelo
O modelo de **Regressão Logística** apresentou acurácia de **80%**. 
