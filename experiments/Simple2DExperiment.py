from matplotlib import pyplot as plt

from data_providers.GeometricDataProvider2D import GeometricDataProvider2D


class Simple2DExperiment:
    def __init__(self, model, data_provider):
        self.data_provider: GeometricDataProvider2D = data_provider
        self.model = model


    def plot_contours(self):
        x1, x2, y = self.data_provider.get_distribution_contours()
        plt.contourf(x1, x2, y, alpha=0.1)

    def plot_samples(self):
        x1, x2, y = self.data_provider.get_random_sample_from_distribution()
        plt.scatter(x=x1, y=x2, c=y)

    def run_experiment(self):
        self.plot_contours()
        self.plot_samples()

        plt.show()


