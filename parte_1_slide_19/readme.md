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
| 2327 | 75 |
| 0 | 2363 |

#### Classification report
|  | precision | recall | f1-score | support |
| :--- | :---: | :---: | :---: | :---: |
| N | 1.00 | 0.97 | 0.98 | 2402 |
| Y |  0.97 | 1.00 | 0.98 | 2363 |
| accuracy |  |  | 0.98 | 4765 |
| macro avg | 0.98 | 0.98 | 0.98 | 4765 |
| weighted avg | 0.98 | 0.98 | 0.98 | 4765 |

cross_val_score
```json
{
  'accuracy': 0.9842646717352656, 
  'auc_roc': 0.9949060074490805
}
```