import numpy as np
import pandas as pd

from expressions.Expression import Expression




class GeometricDataProvider2D:
    def __init__(self, equations: list, range_x1: tuple, range_x2: tuple, granularity: int = 1000):
        self.granularity = granularity
        self.x1, self.x2, self.y = self.build_df(equations, range_x1, range_x2)

    def get_data(self):
        return self.x1, self.x2, self.y


    def build_df(self, equations, range_x1, range_x2):
        equation: Expression = equations[0]
        step_x1 = (range_x1[1] - range_x1[0]) / self.granularity
        step_x2 = (range_x2[1] - range_x2[0]) / self.granularity

        x_1 = np.arange(range_x1[0], range_x1[1], step_x1)
        x_2 = np.arange(range_x2[0], range_x2[1], step_x2)
        xx1, xx2 = np.meshgrid(x_1, x_2)

        result = pd.DataFrame()
        result['x_1'] = xx1.ravel()
        result['x_2'] = xx2.ravel()

        yy = equation.evaluate(result).to_numpy().reshape(xx1.shape)

        return xx1, xx2, yy

