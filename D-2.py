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

# 結果-長方形面積
print(rectangle1.area())  # 30.00

# 結果-対角線の長さ
print(rectangle1.diagonal())  # 7.81
