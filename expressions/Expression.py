import pandas as pd


class Expression:
    def __init__(self):
        pass

    def evaluate(self, df: pd.DataFrame) -> pd.Series:
        pass

    def __add__(self, other):
        result = Expression()
        result.evaluate = lambda df: self.evaluate(df) + other.evaluate(df)
        result.__repr__ = lambda: f'( {self.__repr__()} + {other.__repr__()} )'
        return result

    def __sub__(self, other):
        result = Expression()
        result.evaluate = lambda df: self.evaluate(df) - other.evaluate(df)
        result.__repr__ = lambda: f'( {self.__repr__()} - {other.__repr__()} )'
        return result

    def __mul__(self, other):
        result = Expression()
        result.evaluate = lambda df: self.evaluate(df) * other.evaluate(df)
        result.__repr__ = lambda: f'( {self.__repr__()} * {other.__repr__()} )'
        return result

    def __pow__(self, power):
        result = Expression()
        result.evaluate = lambda df: self.evaluate(df) ** power
        result.__repr__ = lambda: f'{self.__repr__()}^{power} )'
        return result


    def __truediv__(self, other):
        result = Expression()
        result.evaluate = lambda df: self.evaluate(df) / other.evaluate(df)
        result.__repr__ = lambda: f'( {self.__repr__()} / {other.__repr__()} )'
        return result

    def __lt__(self, other):
        result = Expression()
        result.evaluate = lambda df: self.evaluate(df) < other.evaluate(df)
        result.__repr__ = lambda: f'( {self.__repr__()} < {other.__repr__()} )'
        return result


    def __le__(self, other):
        result = Expression()
        result.evaluate = lambda df: self.evaluate(df) <= other.evaluate(df)
        result.__repr__ = lambda: f'( {self.__repr__()} <= {other.__repr__()} )'
        return result


    def __eq__(self, other):
        result = Expression()
        result.evaluate = lambda df: self.evaluate(df) == other.evaluate(df)
        result.__repr__ = lambda: f'( {self.__repr__()} == {other.__repr__()} )'
        return result


    def __contains__(self, key):
        result = Expression()
        result.evaluate = lambda df: key.evaluate(df) in self.evaluate(df)
        result.__repr__ = lambda: f'( {key.__repr__()} in {self.__repr__()} )'
        return result


    def __ne__(self, other):
        result = Expression()
        result.evaluate = lambda df: self.evaluate(df) != other.evaluate(df)
        result.__repr__ = lambda: f'( {self.__repr__()} != {other.__repr__()} )'
        return result


    def __gt__(self, other):
        result = Expression()
        result.evaluate = lambda df: self.evaluate(df) > other.evaluate(df)
        result.__repr__ = lambda: f'( {self.__repr__()} > {other.__repr__()} )'
        return result


    def __ge__(self, other):
        result = Expression()
        result.evaluate = lambda df: self.evaluate(df) >= other.evaluate(df)
        result.__repr__ = lambda: f'( {self.__repr__()} >= {other.__repr__()} )'
        return result





