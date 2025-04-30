# What is Inheritance and Super Keyword

class Parent():

    def greet(self):
        return "Hello from Parent"


class Child(Parent):


    def __init__(self, tittle):
        self.tittle = tittle


    def greet (self):
        return super().greet()+self.tittle+"Hello from child"

c=Child("Anupam Kumar")
c.greet()

