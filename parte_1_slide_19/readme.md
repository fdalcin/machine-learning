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
| 2323 | 73 |
| 0 | 2369 |

#### Classification report
|  | precision | recall | f1-score | support |
| :--- | :---: | :---: | :---: | :---: |
| N | 1.00 | 0.97 | 0.99 | 2396 |
| Y |  0.97 | 1.00 | 0.98 | 2369 |
| accuracy |  |  | 0.98 | 4765 |
| macro avg | 0.99 | 0.98 | 0.98 | 4765 |
| weighted avg | 0.99 | 0.98 | 0.98 | 4765 |

Model score: **98.70%**

Cross validation score  
Mean precision: **0.9855198464824988**

Cross validate score  
Mean precision: **0.9855198464824988**