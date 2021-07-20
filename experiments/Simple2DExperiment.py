from data_providers.GeometricDataProvider2D import GeometricDataProvider2D
from visualisation.Visualizer2D import Visualizer2D


class Simple2DExperiment:
    def __init__(self, model, data_provider):
        self.data_provider: GeometricDataProvider2D = data_provider
        self.model = model
        self.visualizer = Visualizer2D(
            range_x1=self.data_provider.range_x1,
            range_x2=self.data_provider.range_x2,
            plot_granularity=self.data_provider.plot_granularity
        )


    def run_experiment(self):
        # Generating the training set of the experiment
        train_x1, train_x2, train_y = self.data_provider.get_random_sample_from_distribution()

        # Visualisation of the original distribution which generated the dataset
        self.visualizer.plot_experiment(
            x1=train_x1,
            x2=train_x2,
            y_true=train_y,
            label='REAL DISTRIBUTION',
            classifier=self.data_provider.evaluate_equations
        )

        # Training the model
        self.model.train(train_x1, train_x2, train_y)

        # Visualisation of the predicted distribution
        self.visualizer.plot_experiment(
            x1=train_x1,
            x2=train_x2,
            y_true=train_y,
            label='PREDICTED DISTRIBUTION',
            classifier=self.model.predict
        )








