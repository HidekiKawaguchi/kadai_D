import math


class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    # 長方形面積
    def area(self):
        return f'{self.height * self.width:.2f}'

    # 対角線の長さ
    def diagonal(self):
        return f'{math.sqrt(self.height ** 2 + self.width ** 2):.2f}'


# 実体化(インスタンス化)
rectangle1 = Rectangle(height=5, width=6)
rectangle2 = Rectangle(height=3, width=3)

# rectangle1結果-長方形面積
print(rectangle1.area())  # 30.00

# rectangle1結果-対角線の長さ
print(rectangle1.diagonal())  # 7.81

# rectangle2結果-長方形面積
print(rectangle2.area())  # 9.00

# rectangle2結果-対角線の長さ
print(rectangle2.diagonal())  # 4.24
