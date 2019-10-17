## Atividade

Construir um sistema classificador para os dados do arquivo diabetes.csv

- Qual algoritmo foi selecionado? Por que?

- Qual é a acurácia do modelo obtido?

## Resultados

### Decision Tree

#### Confusion matrix

|  |  |
| :---: | :---: |
| 114 | 24 |
| 40 | 53 |

#### Classification report

|  | precision | recall | f1-score | support |
| :--- | :---: | :---: | :---: | :---: |
| tested_negative | 0.74 | 0.83 | 0.78 | 138 |
| tested_positive | 0.69 | 0.57 | 0.62 | 93 |
| |
| accuracy |  |  | 0.72 | 231 |
| macro avg | 0.71 | 0.70 | 0.70 | 231 |
| weighted avg | 0.72 | 0.72 | 0.72 | 231 |

Model score: **93.07%**

Cross validation score  
Mean precision: **0.683399470899471**

Cross validate score  
Mean precision: **0.6925264550264552**

### Random Forest

#### Confusion matrix

|  |  |
| :---: | :---: |
| 126 | 14 |
| 32 | 58 |

#### Classification report

|  | precision | recall | f1-score | support |
| :--- | :---: | :---: | :---: | :---: |
| tested_negative | 0.80 | 0.89 | 0.84 | 141 |
| tested_positive | 0.79 | 0.64 | 0.71 | 90 |
| |
| accuracy |  |  | 0.80 | 231 |
| macro avg | 0.80 | 0.77 | 0.78 | 231 |
| weighted avg | 0.80 | 0.80 | 0.79 | 231 |

Model score: **93.93%**

Cross validation score  
Mean precision: **0.728968253968254**

Cross validate score  
Mean precision: **0.7188492063492065**

#### Algoritmo selecionado
Foi selecionado o modelo de **Regressão Logística** apresentado anteriormente - **[parte_1_slide_18](https://github.com/fdalcin/machine-learning/tree/master/parte_1_slide_18)**, uma vez que o mesmo apresentou uma melhor acurácia.

#### Acurácia do modelo
O modelo de **Regressão Logística** apresentou acurácia de **81%**. 
