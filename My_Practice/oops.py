class Calculator:
    num = 100

    def __init__(self, a, b):
        self.firstnum = a
        self.secondnum = b
        print("I am automatically called")

    def getData(self):

        print("This is the getData method")

    def summation(self):
        return self.firstnum + self.secondnum + Calculator.num

obj = Calculator(3, 4)
obj.getData()
print(obj.summation())

obj1 = Calculator(5, 6)
#obj1.getData()
print(obj1.summation())

