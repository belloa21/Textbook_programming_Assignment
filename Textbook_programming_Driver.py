#Alex Bello
#11/20/2019

from Textbook_programming_class import Textbook
from Textbook_programming_person_class import Person


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


choice = 0
while choice != 5:
    choice = menu()
    if choice == 1:
        # Create Textbook
        new_book()
        print()
    elif choice == 2:
        # Edit Textbook
        print('Which textbook would you like to edit?')
        Textbook.list_books()
        book_choice = int(input(': '))
        print()
        print('Would you like to (add) or (remove) from inventory?')
        edit_choice = input('/> ')
        print()
        print(f'How many to {edit_choice} to inventory?')
        amount = int(input(': '))
        if edit_choice == 'add':
            Textbook.books[book_choice].add_inventory(amount)
        elif edit_choice == 'remove':
            Textbook.books[book_choice].remove_inventory(amount)
        print()
    elif choice == 3:
        # Remove Textbook
        print('Which textbook would you like to remove?')
        Textbook.list_books()
        choice = int(input(': '))
        print()
        book = Textbook.books.pop(choice)
        print(f'"{book.title}" has been deleted.')
        print()
    elif choice == 4:
        # Show Textbooks
        Textbook.list_books(True)
        print()
