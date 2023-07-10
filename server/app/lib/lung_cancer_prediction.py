import numpy as np
import pandas as pd
from app.utils.providers import lung_cancer_provider


def pred_logistic_regression(inp, cols):
    scal = lung_cancer_provider.GetMinMaxScalerNonTree()

    inp = pd.DataFrame(np.array(inp).reshape(1, -1), columns=cols)
    inp = scal.transform(inp)
    clf = lung_cancer_provider.GetLogisticRegressionClassifier()

    return clf.predict(inp)


def pred_naive_bayes(inp, cols):
    scal = lung_cancer_provider.GetMinMaxScalerNonTree()

    inp = pd.DataFrame(np.array(inp).reshape(1, -1), columns=cols)
    inp = scal.transform(inp)
    clf = lung_cancer_provider.GetNaiveBayesClassifier()

    return clf.predict(inp)


def pred_knn(inp, cols):
    scal = lung_cancer_provider.GetMinMaxScalerNonTree()

    inp = pd.DataFrame(np.array(inp).reshape(1, -1), columns=cols)
    inp = scal.transform(inp)
    clf = lung_cancer_provider.GetKNNClassifier()

    return clf.predict(inp)


def pred_decision_tree(inp, cols):
    scal = lung_cancer_provider.GetMinMaxScalerNonTree()

    inp = pd.DataFrame(np.array(inp).reshape(1, -1), columns=cols)
    inp = scal.transform(inp)
    clf = lung_cancer_provider.GetDecisionTreeClassifier()

    return clf.predict(inp)


def lung_cancer_process(user_input):
    colums = [
        "Gender",
        "Age",
        "Smoking",
        "YellowFingers",
        "Anxiety",
        "PeerPressure",
        "ChronicDisease",
        "Fatigue",
        "Allergy",
        "Wheezing",
        "AlcoholConsuming",
        "Coughing",
        "ShotnessOfBreath",
        "Swallowing_Difficulty",
        "ChestPain",
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
