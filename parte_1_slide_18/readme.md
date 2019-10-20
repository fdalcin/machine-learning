## Atividade

- Obter modelo de regressão logística utilizando o arquivo diabetes.csv

## Resultados

#### Confusion matrix

|  |  |
| :---: | :---: |
| 143 | 17 |
| 29 | 42 |

#### Classification report

|  | precision | recall | f1-score | support |
| :--- | :---: | :---: | :---: | :---: |
| tested_negative | 0.83 | 0.89 | 0.86 | 160 |
| tested_positive | 0.71 | 0.59 | 0.65 | 71 |
| accuracy |  |  | 0.80 | 231 |
| macro avg | 0.77 | 0.74 | 0.75 | 231 |
| weighted avg | 0.79 | 0.80 | 0.80 | 231 |

cross_val_score
```json
{
  'accuracy': 0.7706521739130434, 
  'auc_roc': 0.7887784002489886
}
```

