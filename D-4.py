class MyCounterV1:
    def __init__(self, value):
        self.value = value

    def value(self):
        return self.value()

    def count_up(self):
        self.value = self.value + 1
        return ()


counter1 = MyCounterV1(value=0)

print(counter1.value)  # 0

counter1.count_up()
print(counter1.value)  # 1

counter1.count_up()
print(counter1.value)  # 2
