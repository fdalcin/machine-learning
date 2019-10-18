from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score, roc_curve
from sklearn.model_selection import cross_validate, cross_val_score
from sklearn.svm import SVC
import numpy
import config
import joblib


def execute_model(model_name, params):
    model = joblib.load(config.MODEL_PATH + model_name + '.sav')

    return model.predict(params)


def probability(model_name, params):
    model = joblib.load(config.MODEL_PATH + model_name + '.sav')

    return model.predict_proba(params)


def _confusion_matrix(test, evaluation):
    matrix = confusion_matrix(test, evaluation)

    print("\nConfusion matrix")
    print(matrix)

    return matrix

def _roc_values(testing, evaluation):
    auc_roc = roc_auc_score(testing, numpy.where(evaluation == 'Y', 1, 0))

    print("\nRoc Score")
    print(auc_roc)

    return auc_roc


def _classification_report(test, evaluation):
    report = classification_report(test, evaluation)

    print("\nClassification report")
    print(report)

    return report


class MachineLearning:
    def __init__(self, test_size=0.30, solver='liblinear'):
        self.solver = solver
        self.test_size = test_size

    def _train_test_split(self, attributes, classes):
        x_training, x_testing, y_training, y_testing = train_test_split(
            attributes, classes, test_size=self.test_size
        )

        return x_training, x_testing, y_training, y_testing

    def generate_random_forest(self, attributes, classes, output_filename):
        x_training, x_testing, y_training, y_testing = self._train_test_split(attributes, classes)

        rf = RandomForestClassifier(n_estimators=100)
        rf.fit(x_training, y_training)

        y_evaluation = rf.predict(x_testing)

        _roc_values(y_testing, y_evaluation)

        _confusion_matrix(y_testing, y_evaluation)

        _classification_report(y_testing, y_evaluation)

        filename = config.MODEL_PATH + output_filename + '.sav'
        message = "Model '{}' created with {}% training set size."

        joblib.dump(rf, filename)

        return message.format(filename, self.test_size * 100)

    def generate_decision_tree(self, attributes, classes, output_filename):
        x_training, x_testing, y_training, y_testing = self._train_test_split(attributes, classes)

        dt = DecisionTreeClassifier()
        dt.fit(x_training, y_training)

        y_evaluation = dt.predict(x_testing)

        _roc_values(y_testing, y_evaluation)

        _confusion_matrix(y_testing, y_evaluation)

        _classification_report(y_testing, y_evaluation)

        filename = config.MODEL_PATH + output_filename + '.sav'
        message = "Model '{}' created with {}% training set size."

        joblib.dump(dt, filename)

        return message.format(filename, self.test_size * 100)

    def generate_logistic_regression(self, attributes, classes, output_filename):
        x_training, x_testing, y_training, y_testing = self._train_test_split(attributes, classes)

        lr = LogisticRegression(solver=self.solver)
        lr.fit(x_training, y_training)

        y_evaluation = lr.predict(x_testing)

        _roc_values(y_testing, y_evaluation)

        _confusion_matrix(y_testing, y_evaluation)

        _classification_report(y_testing, y_evaluation)

        filename = config.MODEL_PATH + output_filename + '.sav'
        message = "Model '{}' created using {} with {}% training set size."

        joblib.dump(lr, filename)

        return message.format(filename, self.solver, self.test_size * 100)

    def generate_svm(self, attributes, classes, output_filename, kernel='linear'):
        x_training, x_testing, y_training, y_testing = self._train_test_split(attributes, classes)

        svm = SVC(gamma='scale', kernel=kernel, probability=True)
        svm.fit(x_training, y_training)

        y_evaluation = svm.predict(x_testing)

        _roc_values(y_testing, y_evaluation)

        _confusion_matrix(y_testing, y_evaluation)

        _classification_report(y_testing, y_evaluation)

        filename = config.MODEL_PATH + output_filename + '.sav'
        message = "Model '{}' with Kernel {} created using {}% training set size."

        joblib.dump(svm, filename)

        return message.format(filename, kernel, self.test_size * 100)

    def validate_model(self, model_name, attributes, classes):
        model = joblib.load(config.MODEL_PATH + model_name + '.sav')

        x_training, x_testing, y_training, y_testing = self._train_test_split(attributes, classes)

        accuracy = model.score(x_testing, y_testing) * 100
        scores = cross_val_score(model, x_testing, y_testing, cv=30)

        print("\nModel score: {0:.2f}%".format(accuracy))

        print("\nCross validation score " + model_name)
        print("Mean precision: ", scores.mean())

        scores_ = cross_validate(model, x_testing, y_testing, cv=30)

        print("\nCross validate score " + model_name)
        print("Mean precision: ", scores_['test_score'].mean())

        response = dict()

        response['model_score'] = accuracy
        response['cross_val_score'] = scores.mean()
        response['cross_validate'] = scores_['test_score'].mean()

        return response
