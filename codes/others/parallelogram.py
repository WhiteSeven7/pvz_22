class Parallelogram:

    @classmethod
    def create(cls, pos_x, pos_y, x1, y1, x2, y2):
        if x1 * y2 - x2 * y1 > 0:
            return cls(pos_x, pos_y, x1, y1, x2, y2)
        else:
            return cls(pos_x, pos_y, x2, y2, x1, y1)

    def __init__(self, pos_x, pos_y, ix, iy, jx, jy):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.ix = ix
        self.iy = iy
        self.jx = jx
        self.jy = jy

    def area(self):
        return self.ix * self.jy - self.iy * self.jx

    def collide_point(self, x, y):
        x -= self.pos_x
        y -= self.pos_y
        s = self.area()
        a = x * self.jy - y * self.jx
        b = self.ix * y - self.iy * x
        return 0 <= a < s and 0 <= b < s
