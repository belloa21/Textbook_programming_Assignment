#Alex Bello
#11/20/2019
#Defines the Person class and its functions


class Person():
    count = 0

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = int(age)
        Person.count += 1

    def __del__(self):
        Person.count -= 1

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def all_data(self):
        return {'first_name':self.first_name, 'last_name':self.last_name, 'age':self.age}


