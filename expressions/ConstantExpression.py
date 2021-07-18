import pandas as pd

from expressions.Expression import Expression


class ConstantExpression(Expression):
    def __init__(self, value):
        super().__init__()
        self.value = value


    def evaluate(self, df: pd.DataFrame):
        return pd.Series([1 for x in range(len(df.index))])


