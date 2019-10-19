import joblib
import numpy
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier

import config


def execute_model(model_name, params):
    model = joblib.load(config.MODEL_PATH + model_name + '.sav')

    return model.predict(params)


def probability(model_name, params):
    model = joblib.load(config.MODEL_PATH + model_name + '.sav')

    return model.predict_proba(params)


def validate_model(model_name, x_testing, y_testing, categorical=False):
    model = joblib.load(config.MODEL_PATH + model_name + '.sav')

    acc = cross_val_score(model, x_testing, y_testing, cv=30, scoring='accuracy')

    response = dict()

    response['accuracy'] = acc.mean()

    if not categorical:
        roc = cross_val_score(model, x_testing, y_testing, cv=30, scoring='roc_auc')

        response['auc_roc'] = roc.mean()

    return response


def accuracy(matrix):
    tp = numpy.diag(matrix)
    fp = numpy.sum(matrix, axis=0) - tp

    true_positive = numpy.sum(tp)
    false_positive = numpy.sum(fp)

    return round(true_positive / (true_positive + false_positive), 2)


def sensitivity(matrix):
    true_positive = matrix[0][0]
    false_negative = matrix[0][1]

    return true_positive / (true_positive + false_negative)


def specificity(matrix):
    true_negative = matrix[1][1]
    false_positive = matrix[1][0]

    return true_negative / (true_negative + false_positive)


def _confusion_matrix(y_testing, y_predict):
    matrix = confusion_matrix(y_testing, y_predict)

    print("\nConfusion matrix")
    print(matrix)

    return matrix


def _classification_report(y_testing, y_predict):
    report = classification_report(y_testing, y_predict)

    print("\nClassification report")
    print(report)

    return report


def _roc_values(y_testing, y_predict):
    auc_roc = roc_auc_score(y_testing, numpy.where(y_predict == 'Y', 1, 0))

    print("\nRoc Score")
    print(auc_roc)

    return auc_roc


class MachineLearning:
    def __init__(self, test_size=0.30, solver='liblinear'):
        self.solver = solver
        self.test_size = test_size

    def train_test_split(self, attributes, classes):
        x_training, x_testing, y_training, y_testing = train_test_split(
            attributes, classes, test_size=self.test_size
        )

        return x_training, x_testing, y_training, y_testing

    def generate_random_forest(self, x_training, x_testing, y_training, y_testing, output_filename):
        rf = RandomForestClassifier(n_estimators=100)
        rf.fit(x_training, y_training)

        y_predict = rf.predict(x_testing)

        auc_roc = _roc_values(y_testing, y_predict)

        matrix = _confusion_matrix(y_testing, y_predict)

        _classification_report(y_testing, y_predict)

        filename = config.MODEL_PATH + output_filename + '.sav'
        message = "Model '{}' created with {}% training set size."

        joblib.dump(rf, filename)

        return message.format(filename, self.test_size * 100), matrix, auc_roc

    def generate_decision_tree(self, x_training, x_testing, y_training, y_testing, output_filename):
        dt = DecisionTreeClassifier()
        dt.fit(x_training, y_training)

        y_predict = dt.predict(x_testing)

        auc_roc = _roc_values(y_testing, y_predict)

        matrix = _confusion_matrix(y_testing, y_predict)

        _classification_report(y_testing, y_predict)

        filename = config.MODEL_PATH + output_filename + '.sav'
        message = "Model '{}' created with {}% training set size."

        joblib.dump(dt, filename)

        return message.format(filename, self.test_size * 100), matrix, auc_roc

    def generate_logistic_regression(self, x_training, x_testing, y_training, y_testing, output_filename):
        lr = LogisticRegression(solver=self.solver)
        lr.fit(x_training, y_training)

        y_predict = lr.predict(x_testing)

        auc_roc = _roc_values(y_testing, y_predict)

        matrix = _confusion_matrix(y_testing, y_predict)

        _classification_report(y_testing, y_predict)

        filename = config.MODEL_PATH + output_filename + '.sav'
        message = "Model '{}' created using {} with {}% training set size."

        joblib.dump(lr, filename)

        return message.format(filename, self.solver, self.test_size * 100), matrix, auc_roc

    def generate_svm(self, x_training, x_testing, y_training, y_testing, output_filename, kernel='linear'):
        svm = SVC(gamma='scale', kernel=kernel, cache_size=1000)
        svm.fit(x_training, y_training)

        y_predict = svm.predict(x_testing)

        auc_roc = _roc_values(y_testing, y_predict)

        matrix = _confusion_matrix(y_testing, y_predict)

        _classification_report(y_testing, y_predict)

        filename = config.MODEL_PATH + output_filename + '.sav'
        message = "Model '{}' with Kernel {} created using {}% training set size."

        joblib.dump(svm, filename)

        return message.format(filename, kernel, self.test_size * 100), matrix, auc_roc
