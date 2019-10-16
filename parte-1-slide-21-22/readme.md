## Atividade

- Obter o modelo preditivo 

Determine:

- Qual é a acurácia do modelo?

- Qual é a função gerada pelo modelo?

- Sensibilidade: Capacidade de prever verdadeiros positivos  
NVP / (NVP + NFN)

- Especificidade: Capacidade de prever verdadeiros negativos  
NVN / (NVN + NFP)

- Qual é a acurácia do modelo obtido com função logística?

- Confusion Matrix

## Resultados

#### Acurácia do modelo
Accuracy **1.00**
Model score **99.94%**

#### Função gerada pelo modelo
Foi utilizado o modelo de **Decision Tree**

#### Sensibilidade
1600 / (1600 + 8) = **0.9950** = **99.5%**

#### Especificidade
1569 / (1569 + 0) = **1.00** = **100%**

#### Acurácia do modelo de função logística
Accuracy **0.99**
Model score **98.39%**

#### Confusion Matrix

##### Logistic Regression
|  |  |
| :---: | :---: |
| 1556 | 46 |
| 0 | 1575 |

##### Decision Tree
|  |  |
| :---: | :---: |
| 1600 | 8 |
| 0 | 1569 |