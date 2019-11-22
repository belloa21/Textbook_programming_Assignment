#Alex Bello
#11/20/2019
#Defines the Book class and its functions


from Textbook_programming_person_class import Person


class Textbook:
    books = []

    def __init__(self, title, author, edition, ISBN, publisher, year_published, quantity, price):
        self.title = title
        self.author = author
        self.edition = edition
        self.ISBN = ISBN
        self.publisher = publisher
        self.year_published = year_published
        self.quantity = quantity
        self.price = price
        Textbook.books.append(self)

    def __str__(self):
        return f'{self.title}, {self.edition} edition, by {self.author}: ${self.price}({self.quantity} left)'

    def all_data(self):
        return {'title':self.title, 'author':self.author.all_data(), 'edition':self.edition, 'ISBN':self.ISBN,
                'publisher':self.publisher, 'year_published':self.year_published, 'quantity':self.quantity, 'price':self.price}

    def add_inventory(self, amount_to_add):
        self.quantity += amount_to_add

    def remove_inventory(self, amount_to_remove):
        if self.quantity < amount_to_remove:
            print()
            print('Error!  Not enough inventory available.')
        elif self.quantity - amount_to_remove < 5:
            print()
            print(f'Warning!  Inventory is below 5.  {self.quantity} remaining.')
        else:
            self.quantity -= amount_to_remove

    @classmethod
    def list_books(cls, all_data=False):
        i = 0
        for book in cls.books:
            if all_data:
                print(book.all_data())
            else:
                print(f'{i}) {book}')


def menu():
    print('--- Hartwick College Textbook Management System ---')
    print()
    print('1) Create new textbook.')
    print('2) Edit current textbook inventory.')
    print('3) Remove a textbook.')
    print('4) Show all textbooks.')
    print('5) EXIT PROGRAM')
    print()
    return int(input('/> '))


def new_person():
    first_name = input('Enter first name: ')
    last_name = input('Enter last name: ')
    age = int(input('Enter age: '))
    return Person(first_name, last_name, age)


def new_book():
    title = input('Enter title: ')
    print('--- Author Information ---')
    author = new_person()
    print('-' * len('--- Author Information ---'))
    edition = input('Enter edition: ')
    ISBN = input('Enter ISBN number: ')
    publisher = input('Enter textbook publisher: ')
    year_published = input('Enter year published: ')
    quantity = int(input('Enter quantity available: '))
    price = float(input('Enter textbook price: '))
    print()
    return Textbook(title, author, edition, ISBN, publisher, year_published, quantity, price)



