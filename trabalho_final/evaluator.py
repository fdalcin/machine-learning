import json
import config

def evaluate_best_model():
    filename = config.EVALUATE_PATH + 'results.json'

    best_model = 0
    with open(filename) as json_file:
        data = json.load(json_file)
        for p in data['results']:
            sum = p['acc']+p['sen']+p['spe']+p['roc']
            if sum > best_model:
                best_model = sum
                sel_model = p['model']
                name_model = p['inductor']

    return sel_model, name_model