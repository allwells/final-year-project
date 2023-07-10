import os
import pickle
import joblib

config = {
    "KNN": "../models/lung_cancer/knn.pkl",
    "NaiveBayes": "../models/lung_cancer/naive_bayes.pkl",
    "DecisionTree": "../models/lung_cancer/decision_tree.pkl",
    "scalar_non_tree": "../models/lung_cancer/minmax_scaler_non_tree.pkl",
    "LogisticRegression": "../models/lung_cancer/logistic_regression.pkl",
}

dir = os.path.dirname(__file__)


def GetJobLibFile(filepath):
    if os.path.isfile(os.path.join(dir, filepath)):
        return joblib.load(os.path.join(dir, filepath))
    return None


def GetPickleFile(filepath):
    if os.path.isfile(os.path.join(dir, filepath)):
        return pickle.load(open(os.path.join(dir, filepath), "rb"))
    return None


def GetMinMaxScalerNonTree():
    return GetJobLibFile(config["scalar_non_tree"])


def GetLabelEncoderTree():
    return GetJobLibFile(config["label_encoder_tree"])


def GetOneHotEncoderNonTree():
    return GetJobLibFile(config["one_hot_encoder_nontree"])


def GetLogisticRegressionClassifier():
    return GetJobLibFile(config["LogisticRegression"])


def GetNaiveBayesClassifier():
    return GetJobLibFile(config["NaiveBayes"])


def GetDecisionTreeClassifier():
    return GetJobLibFile(config["DecisionTree"])


def GetKNNClassifier():
    return GetJobLibFile(config["KNN"])


def GetAllClassifiers():
    return (
        GetLogisticRegressionClassifier(),
        GetNaiveBayesClassifier(),
        GetDecisionTreeClassifier(),
        GetKNNClassifier(),
    )
