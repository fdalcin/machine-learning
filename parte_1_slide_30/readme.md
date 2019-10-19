## Atividade

Construir um sistema classificador para os dados do arquivo diabetes.csv

- Qual algoritmo foi selecionado? Por que?

- Qual é a acurácia do modelo obtido?

## Resultados

### Decision Tree

#### Confusion matrix

|  |  |
| :---: | :---: |
| 122 | 34 |
| 37 | 38 |

#### Classification report

|  | precision | recall | f1-score | support |
| :--- | :---: | :---: | :---: | :---: |
| tested_negative | 0.77 | 0.78 | 0.77 | 156 |
| tested_positive | 0.53 | 0.51 | 0.52 | 75 |
| |
| accuracy |  |  | 0.69 | 231 |
| macro avg | 0.65 | 0.64 | 0.65 | 231 |
| weighted avg | 0.69 | 0.69 | 0.69 | 231 |

```json
{
  'accuracy': 0.6884259259259261, 
  'auc_roc': 0.667222222222222
}
```

### Random Forest

#### Confusion matrix

|  |  |
| :---: | :---: |
| 131 | 24 |
| 38 | 38 |

#### Classification report

|  | precision | recall | f1-score | support |
| :--- | :---: | :---: | :---: | :---: |
| tested_negative | 0.78 | 0.85 | 0.81 | 155 |
| tested_positive | 0.61 | 0.50 | 0.55 | 76 |
| |
| accuracy |  |  | 0.73 | 231 |
| macro avg | 0.69 | 0.67 | 0.68 | 231 |
| weighted avg | 0.72 | 0.73 | 0.72 | 231 |

```json
{
  'accuracy': 0.7546296296296298, 
  'auc_roc': 0.7788888888888889
}
```

#### Algoritmo selecionado
Foi selecionado o modelo de **Regressão Logística** apresentado anteriormente - **[parte_1_slide_18](https://github.com/fdalcin/machine-learning/tree/master/parte_1_slide_18)**, uma vez que o mesmo apresentou uma melhor acurácia.

#### Acurácia do modelo
O modelo de **Regressão Logística** apresentou acurácia de **82%**. 
