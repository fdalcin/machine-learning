## Atividade

Construir um sistema classificador para os dados do arquivo diabetes.csv

- Qual algoritmo foi selecionado? Por que?

- Qual é a acurácia do modelo obtido?

## Resultados

### Decision Tree

#### Confusion matrix

|  |  |
| :---: | :---: |
| 83 | 17 |
| 17 | 37 |

#### Classification report

|  | precision | recall | f1-score | support |
| :--- | :---: | :---: | :---: | :---: |
| tested_negative | 0.83 | 0.83 | 0.83 | 100 |
| tested_positive | 0.69 | 0.69 | 0.69 | 54 |
| |
| accuracy |  |  | 0.78 | 154 |
| macro avg | 0.76 | 0.76 | 0.76 | 154 |
| weighted avg | 0.78 | 0.78 | 0.78 | 154 |

Model score: **94.81%**

Cross validation score diabetes_dt  
Mean precision: **0.7127777777777777**

Cross validate score diabetes_dt  
Mean precision: **0.7055555555555556**

### Random Forest

#### Confusion matrix

|  |  |
| :---: | :---: |
| 89 | 16 |
| 15 | 34 |

#### Classification report

|  | precision | recall | f1-score | support |
| :--- | :---: | :---: | :---: | :---: |
| tested_negative | 0.86 | 0.85 | 0.85 | 105 |
| tested_positive | 0.68 | 0.69 | 0.69 | 49 |
| |
| accuracy |  |  | 0.80 | 154 |
| macro avg | 0.77 | 0.77 | 0.77 | 154 |
| weighted avg | 0.80 | 0.80 | 0.80 | 154 |

Model score: **93.51%**

Cross validation score diabetes_rf  
Mean precision: **0.7326984126984127**

Cross validate score diabetes_rf  
Mean precision: **0.7182539682539684**

#### Algoritmo selecionado
Foi selecionado o modelo de **Regressão Logística** apresentado anteriormente (resultados na pasta **parte-1-slide-18**), uma vez que o mesmo apresentou uma melhor acurácia.

#### Acurácia do modelo
O modelo de **Regressão Logística** apresentou acurácia de **82%**. 
