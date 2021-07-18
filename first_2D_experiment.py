from data_providers.GeometricDataProvider2D import GeometricDataProvider2D
from experiments.Simple2DExperiment import Simple2DExperiment
from models.LogisticsClassifier import LogisticsClassifier

provider = GeometricDataProvider2D(
    equations=[
        x_1 ^ 2 + x_2 ^ 2 <= 1
    ],
    range_x1=(-2, 2),
    range_x2=(-2, 2)
)

model = LogisticsClassifier()

Simple2DExperiment(
    model=model,
    data_provider=provider
).run_experiment()
