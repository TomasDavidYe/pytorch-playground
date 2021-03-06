import numpy as np
import torch
from torch.nn import Sigmoid

from models.Models2D.Abstract2DModel import Abstract2DModel


class LogisticsRegression2DPytorch(Abstract2DModel):
    def __init__(self, feature_transform, n_epochs=100, learning_rate=1e-3):
        self.__feature_transform = feature_transform
        self.__input_size = self.determine_input_size()
        self.__learning_rate = learning_rate
        self.__n_epochs = n_epochs
        self.__weights = torch.tensor([0.0 for _ in range(self.__input_size)], requires_grad=True)
        self.__bias = torch.tensor([0.0], requires_grad=True)
        self.__sigmoid = Sigmoid()


    def determine_input_size(self):
        return len(self.__feature_transform(np.array([1, 1]), np.array([1, 2])))

    def get_weights(self):
        return self.__weights

    def get_bias(self):
        return self.__bias

    def forward(self, x):
        return self.__sigmoid(self.__weights.matmul(x) + self.__bias)

    def transform(self, x1, x2):
        return self.tensorify(self.__feature_transform(x1, x2))

    def tensorify(self, x):
        return torch.tensor(x).float()

    def predict(self, x1, x2):
        x = self.transform(x1, x2)
        prob = self.forward(x)
        return (prob >= 0.5).float()

    def train(self, x1, x2, _y):
        x = self.transform(x1, x2)
        y = self.tensorify(_y)

        optimizer = torch.optim.SGD([self.__weights, self.__bias], self.__learning_rate)
        loss_fn = torch.nn.BCELoss()

        for epoch in range(1, self.__n_epochs + 1):
            optimizer.zero_grad()

            # Forward pass
            y_pred = self.forward(x)

            # Compute Loss
            loss = loss_fn(y_pred, y)

            print('Epoch {}: train loss: {}'.format(epoch, loss.item()))

            # Backward pass
            loss.backward()
            optimizer.step()
