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
2408 / (2408 + 9) = **0.9962** = **99.62%**

#### Especificidade
2348 / (2348 + 0) = **1.00** = **100%**

#### Acurácia do modelo de função logística
Accuracy **0.99**  

#### Confusion Matrix

##### Logistic Regression
|  |  |
| :---: | :---: |
| 2394 | 63 |
| 0 | 2308 |

##### Decision Tree
|  |  |
| :---: | :---: |
| 2408 | 9 |
| 0 | 2348 |