from abc import ABC, abstractmethod


class Abstract2DModel(ABC):

    @abstractmethod
    def train(self, x1, x2, y):
        pass

    @abstractmethod
    def predict(self, x1, x2):
        pass
