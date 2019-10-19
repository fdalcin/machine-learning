## Atividade

- Obter modelo de regressão logística utilizando o arquivo diabetes.csv

## Resultados

#### Confusion matrix

|  |  |
| :---: | :---: |
| 142 | 9 |
| 32 | 48 |

#### Classification report

|  | precision | recall | f1-score | support |
| :--- | :---: | :---: | :---: | :---: |
| tested_negative | 0.82 | 0.94 | 0.87 | 151 |
| tested_positive | 0.84 | 0.60 | 0.70 | 80 |
| accuracy |  |  | 0.82 | 231 |
| macro avg | 0.83 | 0.77 | 0.79 | 231 |
| weighted avg | 0.83 | 0.82 | 0.81 | 231 |

cross_val_score
```json
{
  'accuracy': 0.7927248677248678, 
  'auc_roc': 0.8292592592592594
}
```

