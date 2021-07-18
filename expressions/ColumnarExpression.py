import pandas as pd

from expressions.Expression import Expression


class ColumnarExpression(Expression):
    def __init__(self, column_name):
        super().__init__()
        self.column_name = column_name

    def evaluate(self, df: pd.DataFrame) -> pd.Series:
        return df[self.column_name]


