import numpy as np
import pandas as pd


class GeometricDataProvider2D:
    def __init__(self, equations: list, range_x1: tuple, range_x2: tuple, num_of_points: int = 1000):
        self.range_x2 = range_x2
        self.range_x1 = range_x1
        self.equations = equations
        self.num_of_points = num_of_points

    def get_wrapper_df(self, x1, x2, y):
        wrapper_df = pd.DataFrame()
        wrapper_df['x_1'] = x1
        wrapper_df['x_2'] = x2
        wrapper_df['y'] = y

        return wrapper_df

    def evaluate_equations(self, x1, x2):
        wrapper_df = self.get_wrapper_df(x1, x2, 0)

        results = []
        for equation in self.equations:
            results.append(equation.evaluate(wrapper_df))

        result = results[0]
        for i in range(1, len(results)):
            result = result & results[i]

        return result

    def get_random_sample_from_distribution(self):
        x1 = self.range_x1[0] + np.random.random(self.num_of_points) * (self.range_x1[1] - self.range_x1[0])
        x2 = self.range_x2[0] + np.random.random(self.num_of_points) * (self.range_x2[1] - self.range_x1[0])
        y = self.evaluate_equations(x1, x2)

        return x1, x2, y

    def get_distribution_contours(self):
        step_x1 = (self.range_x1[1] - self.range_x1[0]) / self.num_of_points
        step_x2 = (self.range_x2[1] - self.range_x2[0]) / self.num_of_points

        x_1 = np.arange(self.range_x1[0], self.range_x1[1], step_x1)
        x_2 = np.arange(self.range_x2[0], self.range_x2[1], step_x2)
        xx1, xx2 = np.meshgrid(x_1, x_2)

        input_df = pd.DataFrame()
        input_df['x_1'] = xx1.ravel()
        input_df['x_2'] = xx2.ravel()

        yy = self.evaluate_equations(
            x1=xx1.ravel(),
            x2=xx2.ravel()
        ).to_numpy().reshape(xx1.shape)

        return xx1, xx2, yy
