from data_providers.GeometricDataProvider2D import GeometricDataProvider2D
from experiments.Simple2DExperiment import Simple2DExperiment
from expressions.expression_shortcuts import x_1, x_2, const
from models.LogisticsClassifier import LogisticsClassifier

provider = GeometricDataProvider2D(
    equations=[
        x_1() ** 2 + x_2() ** 2 <= const(1)
    ],
    range_x1=(-2, 2),
    range_x2=(-2, 2),
    num_of_samples=100,
    plot_granularity=300
)

model = LogisticsClassifier()

Simple2DExperiment(
    model=model,
    data_provider=provider
).run_experiment()
