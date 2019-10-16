## Atividade

Contexto: A artrodese de coluna é um tratamento reparador da instabilidade das vértebras, mediante a fusão. É uma resposta eficiente quando a instabilidade de vértebras está instalada, mas gera um paciente com déficit de motilidade (em diferentes graus), tendendo a realizar terapias recuperadoras por toda a vida.

Portanto, trata-se de um tratamento caro e de longo prazo e prever o risco de realização de Artrodese permite a elaboração de tratamentos de manutenção.

- Utilize o arquivo ortopedia.csv

- Obter um modelo preditivo que indique se o paciente possui indicativo de Artrodese ou não.

## Resultados

### Logistic Regression

#### Confusion matrix
|  |  |
| :---: | :---: |
| 1556 | 46 |
| 0 | 1575 |

#### Classification report
|  | precision | recall | f1-score | support |
| :--- | :---: | :---: | :---: | :---: |
| N | 1.00 | 0.97 | 0.99 | 1602 |
| Y |  0.97 | 1.00 | 0.99 | 1575 |
|  |
| accuracy |  |  | 0.99 | 3177 |
| macro avg | 0.99 | 0.99 | 0.99 | 3177 |
| weighted avg | 0.99 | 0.99 | 0.99 | 3177 |

Model score: **98.39%**

Cross validation score orthopedics_lr  
Mean precision: **0.9817518536245392**

Cross validate score orthopedics_lr  
Mean precision: **0.9817518536245392**