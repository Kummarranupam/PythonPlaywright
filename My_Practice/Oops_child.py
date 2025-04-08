from My_Practice.oops import Calculator


class Childimpl(Calculator):
    num2 = 200

    def __init__(self):
        Calculator.__init__(self, 4,9)

    def getcomplete(self):
        return self.num + self.num2 +self.summation()

obj2 = Childimpl()
print(obj2.getcomplete())

