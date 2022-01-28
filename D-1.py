import math

# クラス(データ型)の定義


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return f'{self.radius * self.radius * math.pi:.2f}'

    def perimeter(self):
        return f'{self.radius * 2 * math.pi:.2f}'


circle1 = Circle(radius=1)
print(circle1.area())  # 3.14
print(circle1.perimeter())  # 6.28


circle3 = Circle(radius=3)
print(circle3.area())  # 28.27
print(circle3.perimeter())  # 18.85
