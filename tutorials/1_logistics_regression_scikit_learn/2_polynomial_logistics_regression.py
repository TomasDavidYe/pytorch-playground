from data_providers.GeometricDataProvider2D import GeometricDataProvider2D
from experiments.Simple2DExperiment import Simple2DExperiment
from expressions.expression_shortcuts import x_1, x_2, const
from models.LogisticsClassifier2DScikitLearn import LogisticsClassifier2DScikitLearn


def feature_transform(x1, x2):
    return [
        x1,
        x2,
        x1 ** 2,
        x2 ** 2
    ]


provider = GeometricDataProvider2D(
    equations=[
        x_1() ** 2 - x_2() <= const(1),
        x_2() <= const(1)
    ],
    range_x1=(-2, 2),
    range_x2=(-2, 2),
    num_of_samples=50,
    plot_granularity=200
)

model = LogisticsClassifier2DScikitLearn(
    feature_transform=feature_transform
)

Simple2DExperiment(
    model=model,
    data_provider=provider
).run_experiment()
