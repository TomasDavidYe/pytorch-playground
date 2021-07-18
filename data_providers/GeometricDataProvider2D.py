import numpy as np
import pandas as pd


class GeometricDataProvider2D:
    def __init__(self, equations: list, range_x1: tuple, range_x2: tuple, num_of_samples: int = 100,
                 plot_granularity: int = 1000):
        self.range_x2 = range_x2
        self.range_x1 = range_x1
        self.equations = equations
        self.num_of_samples = num_of_samples
        self.plot_granularity = plot_granularity

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

        return result.to_numpy()

    def get_random_sample_from_distribution(self):
        max_points = 100 * self.num_of_samples
        x1 = self.range_x1[0] + np.random.random(max_points) * (self.range_x1[1] - self.range_x1[0])
        x2 = self.range_x2[0] + np.random.random(max_points) * (self.range_x2[1] - self.range_x1[0])
        y = self.evaluate_equations(x1, x2)

        index_set_positive = y.nonzero()[0][:100]
        index_set_negative = (y == False).nonzero()[0][:100]
        index_set = np.concatenate([index_set_positive, index_set_negative])

        print('num of positive examples = ', len(index_set_positive))
        print('num of negative examples = ', len(index_set_negative))

        return x1[index_set], x2[index_set], y[index_set]


    def get_distribution_contours(self):
        self.get_contours(classifier=self.evaluate_equations)

    def get_contours(self, classifier):
        step_x1 = (self.range_x1[1] - self.range_x1[0]) / self.plot_granularity
        step_x2 = (self.range_x2[1] - self.range_x2[0]) / self.plot_granularity

        x_1 = np.arange(self.range_x1[0], self.range_x1[1], step_x1)
        x_2 = np.arange(self.range_x2[0], self.range_x2[1], step_x2)
        xx1, xx2 = np.meshgrid(x_1, x_2)

        input_df = pd.DataFrame()
        input_df['x_1'] = xx1.ravel()
        input_df['x_2'] = xx2.ravel()

        yy = classifier(
            x1=xx1.ravel(),
            x2=xx2.ravel()
        ).reshape(xx1.shape)

        return xx1, xx2, yy
