import json
import config


def evaluate_best_model():
    filename = config.EVALUATE_PATH + 'results.json'

    best_score = 0
    with open(filename) as json_file:
        data = json.load(json_file)

        for result in data['results']:
            score = result['acc'] + result['sen'] + result['spe'] + result['roc']

            if score > best_score:
                best_score = score
                model = result['model']
                inductor = result['inductor']

    return model, inductor
