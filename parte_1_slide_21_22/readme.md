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
Model score **99.98%**

#### Função gerada pelo modelo
Foi utilizado o modelo de **Decision Tree**

#### Sensibilidade
2362 / (2362 + 8) = **0.9966** = **99.6%**

#### Especificidade
2395 / (2395 + 0) = **1.00** = **100%**

#### Acurácia do modelo de função logística
Accuracy **0.98**  
Model score **98.70%**

#### Confusion Matrix

##### Logistic Regression
|  |  |
| :---: | :---: |
| 2323 | 73 |
| 0 | 2369 |

##### Decision Tree
|  |  |
| :---: | :---: |
| 2362 | 8 |
| 0 | 2395 |