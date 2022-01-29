import math


class Square:
    def __init__(self, side):
        self.side = side

    # 正方形面積
    def area(self):
        return f'{self.side * self.side:.2f}'

    # 対角線の長さ
    def diagonal(self):
        return f'{math.sqrt((self.side ** 2) + (self.side ** 2)):.2f}'


# 実体化(インスタンス化)
square1 = Square(side=1.5)
square2 = Square(side=15)

print(square1.area())  # 2.25
print(square1.diagonal())  # 2.12

print(square2.area())  # 225
print(square2.diagonal())  # 21.21
