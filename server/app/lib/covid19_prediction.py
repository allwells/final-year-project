import numpy as np
import pandas as pd
from app.utils.providers import covid19_provider


def pred_logistic_regression(inp, cols):
    scal = covid19_provider.GetMinMaxScalerNonTree()

    inp = pd.DataFrame(np.array(inp).reshape(1, -1), columns=cols)
    inp = scal.transform(inp)
    clf = covid19_provider.GetLogisticRegressionClassifier()

    return clf.predict(inp)


def pred_naive_bayes(inp, cols):
    scal = covid19_provider.GetMinMaxScalerNonTree()

    inp = pd.DataFrame(np.array(inp).reshape(1, -1), columns=cols)
    inp = scal.transform(inp)
    clf = covid19_provider.GetNaiveBayesClassifier()

    return clf.predict(inp)


def pred_knn(inp, cols):
    scal = covid19_provider.GetMinMaxScalerNonTree()

    inp = pd.DataFrame(np.array(inp).reshape(1, -1), columns=cols)
    inp = scal.transform(inp)
    clf = covid19_provider.GetKNNClassifier()

    return clf.predict(inp)


def pred_decision_tree(inp, cols):
    scal = covid19_provider.GetMinMaxScalerNonTree()

    inp = pd.DataFrame(np.array(inp).reshape(1, -1), columns=cols)
    inp = scal.transform(inp)
    clf = covid19_provider.GetDecisionTreeClassifier()

    return clf.predict(inp)


def covid19_process(user_input):
    colums = [
        "BreathingProblem",
        "Fever",
        "DryCough",
        "SoreThroat",
        "RunningNose",
        "Asthma",
        "ChronicLungDisease",
        "Headache",
        "HeartDisease",
        "Diabetes",
        "HyperTension",
        "Fatigue",
        "Gastrointestinal",
        "TravelAbroad",
        "ContactWithCOVIDPatient",
        "AttendedLargeGatherings",
        "VisitedExposedPublicPlaces",
        "FamilyWorkingInExposedPublicPlaces",
        "WearingMasks",
        "SanitizationFromMarket",
    ]

    logistic_regression_output = pred_logistic_regression(user_input, colums)
    naive_bayes_output = pred_naive_bayes(user_input, colums)
    knn_output = pred_knn(user_input, colums)
    decision_tree_output = pred_decision_tree(user_input, colums)  # hax

    print(
        logistic_regression_output, naive_bayes_output, knn_output, decision_tree_output
    )

    results = [
        {"algorithm": "Logistic Regression", "output": logistic_regression_output},
        {"algorithm": "Naive Bayes", "output": naive_bayes_output},
        {"algorithm": "K-Nearest Neighbors", "output": naive_bayes_output},
        {"algorithm": "Decision Tree", "output": decision_tree_output},
    ]

    return results
