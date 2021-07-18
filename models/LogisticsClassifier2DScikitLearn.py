import pandas as pd
from sklearn.linear_model import LogisticRegression


class LogisticsClassifier2DScikitLearn:
    def __init__(self):
        self.model = LogisticRegression(random_state=0)

    def train(self, x1, x2, y):
        X = pd.DataFrame([x1, x2]).transpose()
        self.model.fit(X, y)

    def predict(self, x1, x2):
        X = pd.DataFrame([x1, x2]).transpose()
        return self.model.predict(X)
