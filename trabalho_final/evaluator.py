from pandas.io.json import json_normalize
import json
import config


def evaluate_best_model():
    filename = config.EVALUATE_PATH + 'results.json'

    best_score = 0
    with open(filename) as json_file:
        data = json.load(json_file)

        results = json_normalize(data['results'])
        results = results.sort_values(['acc', 'roc', 'sen', 'spe'], ascending=False)
        best_models = results[:2]

    return best_models.values
