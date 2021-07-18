from matplotlib import pyplot as plt


class Simple2DExperiment:
    def __init__(self, model, data_provider):
        self.data_provider = data_provider
        self.model = model

    def run_experiment(self):
        x1, x2, y = self.data_provider.get_data()

        plt.contourf(x1, x2, y, alpha=0.4)
        plt.show()
