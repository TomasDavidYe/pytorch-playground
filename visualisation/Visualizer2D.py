import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


class Visualizer2D:
    def __init__(self, range_x1, range_x2, plot_granularity):
        self.range_x1 = range_x1
        self.range_x2 = range_x2
        self.plot_granularity = plot_granularity


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

    def plot_experiment(self, x1, x2, y_true, label: str, classifier):
        xx1, xx2, yy = self.get_contours(classifier)
        plt.contourf(xx1, xx2, yy, alpha=0.1)
        plt.scatter(x=x1, y=x2, c=y_true)
        plt.title(label)
        plt.show()
