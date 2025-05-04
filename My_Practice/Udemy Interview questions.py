# What is Inheritance and Super Keyword
# import pytest
#
#
# class Parent():
#
#     def greet(self):
#         return "Hello from Parent"
#
#
# class Child(Parent):
#
#
#     def __init__(self, tittle):
#         self.tittle = tittle
#
#
#     def greet (self):
#         return super().greet()+self.tittle+"Hello from child"
#
# c=Child("Anupam Kumar")
# c.greet()
# import pytest
#
#
# # Fixtures
#
# @pytest.fixture
# def sample_data():
#     print("\nSetup : Creating Test Data")
#     data = {"name" :"Alice", "Age" : 30}
#     yield data
#     print("Closing the setup")
#
#
# def test_example(sample_data):
#     assert sample_data["name"]=="Alice"
#     assert sample_data["Age"]==30
#     print("Test executed successfuly")

# import asyncio
# import time
#
#
# def task(name):
#     print(f"starting {name}")
#     time.sleep(2)
#     print(f"finished {name}")
#
# task("Anupam")
# task("Kumar")
#
# async def task(name):
#     print(f"starting {name}")
#     await asyncio.sleep(2)
#     print(f"finished {name}")
#
#
# async def main():
#     await asyncio.gather( task("Manav"), task("Sanav") )
# asyncio.run(main())



# class person :
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def greet(self):
#         return f"Hello, my name is {self.name} and I am {self.age} years old"
#
# persu = person("chandan", 30)
# person()



class Myclass:
    @classmethod
    def class_method(cls):
        return "Class"

    def instance_method(self):
        return "Instance"

obj = Myclass()
print(obj.instance_method())
print(Myclass.class_method())



