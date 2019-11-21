#Alex Bello
#11/20/2019
#Defines the Person class and its functions


class Person:
    def __init__(self,first_name,last_name,age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def description(self):
        print(f"The author's first name is {self.first_name} and their last name is {self.last_name}. They are {self.age} years old. ")

