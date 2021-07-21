import pandas as pd
from sklearn.linear_model import LogisticRegression

from models.Models2D.Abstract2DModel import Abstract2DModel


class LogisticsClassifier2DScikitLearn(Abstract2DModel):
    def __init__(self, feature_transform):
        self.feature_transform = feature_transform
        self.model = LogisticRegression(random_state=0)

    def train(self, x1, x2, y):
        X = pd.DataFrame(self.feature_transform(x1, x2)).transpose()
        self.model.fit(X, y)

    def predict(self, x1, x2):
        X = pd.DataFrame(self.feature_transform(x1, x2)).transpose()
        return self.model.predict(X)
