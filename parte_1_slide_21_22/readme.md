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

#### Função gerada pelo modelo
Foi utilizado o modelo de **Decision Tree**

#### Sensibilidade
2338 / (2338 + 15) = **0.9936** = **99.36%**

#### Especificidade
2412 / (2412 + 0) = **1.00** = **100%**

#### Acurácia do modelo de função logística
Accuracy **0.98**  

#### Confusion Matrix

##### Logistic Regression
|  |  |
| :---: | :---: |
| 2327 | 75 |
| 0 | 2363 |

##### Decision Tree
|  |  |
| :---: | :---: |
| 2338 | 15 |
| 0 | 2412 |