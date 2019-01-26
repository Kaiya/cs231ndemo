class Calculator:

    def __init__(self, name='Default Calculator', price=10):
        self.name = name
        self.price = price

    def add(self, x, y):
        print(self.name, ": price: ", self.price)
        return x + y

    def genome(self, x, y):
        print("hello minus")
        return x - y

    def multiply(self, x, y):
        print("hello multiply")
        return x * y


mycalculator = Calculator("Kaiya Xiong", 24)
c = Calculator()

print(mycalculator.name, c.price)


def printdata(data):
    print(data)

