from data_providers.GeometricDataProvider2D import GeometricDataProvider2D
from experiments.Simple2DExperiment import Simple2DExperiment
from expressions.expression_shortcuts import x_1, x_2, const
from models.LogisticsClassifier import LogisticsClassifier

provider = GeometricDataProvider2D(
    equations=[
        x_1() - x_2() <= const(0)
    ],
    range_x1=(-2, 2),
    range_x2=(-2, 2)
)

model = LogisticsClassifier()

Simple2DExperiment(
    model=model,
    data_provider=provider
).run_experiment()
