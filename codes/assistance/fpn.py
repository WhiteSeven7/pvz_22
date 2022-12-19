def signedfloor(dividend, divisor):
    """
    别用，有待改进
    返回有符号整除商，如-7//3=-2...-1，而不是-7//3=-3...2
    :param dividend: 被除数
    :param divisor: 除数
    :return: 有余数的商
    """
    return dividend // divisor if dividend > 0 else -(-dividend // divisor)


class FPN3:
    def __init__(self, integer=0, decimal=0):
        """
        3位定点数
        :param integer: 整数部分（可带符号）
        :param decimal: 小数部分（不可带符号）应在0～99之间，多出会溢出到整数部分
        """
        self.__number = integer * 1000 + decimal if integer >= 0 \
            else integer * 1000 - decimal

    def __repr__(self):
        return f'{self.__class__.__name__}({self.__number})'

    def __int__(self):
        return self.__number // 1000

    def __str__(self):
        return f'{self.__number / 1000}'

    def __float__(self):
        return self.__number / 1000

    def __add__(self, other):
        return self.frombigint(self.__number + other.__number)

    def __radd__(self, other):
        return self.frombigint(self.__number + other.__number)

    def __iadd__(self, other):
        self.__number += other.__number
        return self

    def __sub__(self, other):
        return self.frombigint(self.__number - other.__number)

    def __rsub__(self, other):
        return self.frombigint(self.__number - other.__number)

    def __isub__(self, other):
        self.__number -= other.__number
        return self

    def __mul__(self, other):
        return self.frombigint(self.__number * other.__number // 1000)

    def __rmul__(self, other):
        return self.frombigint(self.__number * other.__number // 1000)

    def __imul__(self, other):
        self.__number = self.__number * other.__number // 1000
        return self

    def __gt__(self, other):
        return self.__number > other.__number

    def __lt__(self, other):
        return self.__number < other.__number

    def __ge__(self, other):
        return self.__number >= other.__number

    def __le__(self, other):
        return self.__number <= other.__number

    def __bool__(self):
        return bool(self.__number)

    def integer(self):
        return self.__number // 1000

    def decimal(self):
        return self.__number % 1000

    def bigint(self):
        return self.__number

    @classmethod
    def frombigint(cls, bigint):
        integer, decimal = divmod(bigint, 1000)
        return cls(integer, decimal)
