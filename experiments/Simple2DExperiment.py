import pandas as pd
from matplotlib import pyplot as plt

from data_providers.GeometricDataProvider2D import GeometricDataProvider2D


class Simple2DExperiment:
    def __init__(self, model, data_provider):
        self.data_provider: GeometricDataProvider2D = data_provider
        self.model = model


    def plot_contours(self, classifier):
        x1, x2, y = self.data_provider.get_contours(classifier)
        plt.contourf(x1, x2, y, alpha=0.1)

    def plot_samples(self, x1, x2, y, label: str):
        plt.scatter(x=x1, y=x2, c=y)
        plt.title(label)

    def run_experiment(self):
        train_x1, train_x2, train_y = self.data_provider.get_random_sample_from_distribution()

        # Plotting real distribution
        self.plot_contours(self.data_provider.evaluate_equations)
        self.plot_samples(
            x1=train_x1,
            x2=train_x2,
            y=train_y,
            label='REAL DISTRIBUTION'
        )
        plt.show()

        # This is where the model runs
        self.model.train(train_x1, train_x2, train_y)
        predicted_train_y = self.model.predict(train_x1, train_x2)

        # Plotting predicted distribution
        self.plot_contours(self.model.predict)
        self.plot_samples(
            x1=train_x1,
            x2=train_x2,
            y=predicted_train_y,
            label='PREDICTED DISTRIBUTION'
        )
        plt.show()








