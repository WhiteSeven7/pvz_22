from copy import copy

from .fpn import FPN3


class IntVector2:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'{self.__class__.__name__}({self.x}, {self.y})'

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __add__(self, other):
        return self.__class__(self.x + other.x, self.y + other.y)

    def __radd__(self, other):
        return self.__class__(self.x + other.x, self.y + other.y)

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self

    def __sub__(self, other):
        return self.__class__(self.x - other.x, self.y - other.y)

    def __isub__(self, other):
        self.x -= other.x
        self.y -= other.y
        return self

    def __mul__(self, other):
        return self.__class__(self.x * other, self.y * other)

    def __rmul__(self, other):
        return self.__class__(self.x * other, self.y * other)

    def __imul__(self, other):
        self.x *= other
        self.y *= other
        return self

    def __floordiv__(self, other):
        return self.__class__(self.x // other, self.y // other)

    def __ifloordiv__(self, other):
        self.x //= other
        self.y //= other
        return self

    def __mod__(self, other):
        return self.__class__(self.x % other, self.y % other)

    def __imod__(self, other):
        self.x %= other
        self.y %= other
        return self

    def __hash__(self):
        return hash((self.x, self.y))

    def __bool__(self):
        return bool(self.x) or bool(self.y)

    def __iter__(self):
        return iter((self.x, self.y))

    # 格式转换
    def tuple(self):
        return self.x, self.y

    @classmethod
    def from_tuple(cls, tuple_):
        return cls(tuple_[0], tuple_[1])


UP = IntVector2(0, -1)
DOWN = IntVector2(0, 1)
LEFT = IntVector2(-1, 0)
RIGHT = IntVector2(1, 0)
UP_LEFT = UL = UP + LEFT
UP_RIGHT = UR = UP + RIGHT
DOWN_LEFT = DL = DOWN + LEFT
DOWN_RIGHT = DR = DOWN + RIGHT
FOUR_FACE = {UP, DOWN, LEFT, RIGHT}
EIGHT_FACE = {UP, DOWN, LEFT, RIGHT, UP_LEFT, UP_RIGHT, DOWN_LEFT, DOWN_RIGHT}


class FPNVector2:
    def __init__(self, x=FPN3(), y=FPN3()):
        """复制量，无需担心改变"""
        self.x = copy(x)
        self.y = copy(y)

    def __repr__(self):
        return f'{self.__class__.__name__}({self.x}, {self.y})'

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __add__(self, other):
        return self.__class__(self.x + other.x, self.y + other.y)

    def __radd__(self, other):
        return self.__class__(self.x + other.x, self.y + other.y)

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self

    def __sub__(self, other):
        return self.__class__(self.x - other.x, self.y - other.y)

    def __isub__(self, other):
        self.x -= other.x
        self.y -= other.y
        return self

    def __mul__(self, other):
        return self.__class__(self.x * other, self.y * other)

    def __rmul__(self, other):
        return self.__class__(self.x * other, self.y * other)

    def __imul__(self, other):
        self.x *= other
        self.y *= other
        return self

    def __bool__(self):
        return bool(self.x) or bool(self.y)

    def __iter__(self):
        return iter((self.x, self.y))

    # 格式转换
    def int_vector2(self):
        return IntVector2(self.x.integer(), self.y.integer())

    def tuple(self):
        return self.x, self.y

    def int_tuple(self):
        return self.x.integer(), self.y.integer()

    @classmethod
    def from_int_vector2(cls, int_vector2):
        return cls(FPN3(int_vector2.x), FPN3(int_vector2.y))

    @classmethod
    def from_tuple(cls, tuple_):
        return cls(tuple_[0], tuple_[1])

    @classmethod
    def from_int_tuple(cls, int_tuple):
        return cls(FPN3(int_tuple[0]), FPN3(int_tuple[1]))
