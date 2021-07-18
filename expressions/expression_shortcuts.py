from expressions.ColumnarExpression import ColumnarExpression
from expressions.ConstantExpression import ConstantExpression
from expressions.Expression import Expression


def const(value) -> Expression:
    return ConstantExpression(value=value)


def x_1() -> Expression:
    return ColumnarExpression(column_name='x_1')


def x_2() -> Expression:
    return ColumnarExpression(column_name='x_2')
