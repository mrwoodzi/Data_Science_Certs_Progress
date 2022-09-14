class Number:
    def __init__(self, value):
        self.value = value

    def add(self, new_value):
        return self.value + new_value

x = Number(4.0)
print(x)
x.add(2.0)
print(x.add(2.0))
print(Number.add(x, 2.0))