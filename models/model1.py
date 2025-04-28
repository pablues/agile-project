# models.py

class Author:
    def __init__(self, name, email, bio=""):
        self.name = name
        self.email = email
        self.bio = bio

    def __str__(self):
        return f"Author: {self.name}"

class Book:
    def __init__(self, title, description, published_date, author):
        self.title = title
        self.description = description
        self.published_date = published_date
        self.author = author  # Author nesnesi

    def __str__(self):
        return f"Book: {self.title} by {self.author.name}"
    
    class Library:
        def __init__(self):
            self.books = []
            self.authors = []

        def add_author(self, author):
            self.authors.append(author)

        def add_book(self, book):
            self.books.append(book)

        def list_books(self):
            for book in self.books:
                print(book)

        def list_authors(self):
            for author in self.authors:
                print(author)

        def find_books_by_author(self, author_name):
            return [book for book in self.books if book.author.name == author_name]
        
        def update_book(self, old_title, new_title=None, new_description=None, new_date=None):
            for book in self.books:
                if book.title == old_title:
                    if new_title:
                        book.title = new_title
                    if new_description:
                        book.description = new_description
                    if new_date:
                        book.published_date = new_date
                    print(f"Book '{old_title}' updated successfully.")
                    return
        print(f"Book" '{old_title}' "not found.")

# main.py

from models import Author, Book, Library
from datetime import date

# Kütüphane oluştur
library = Library()

# Yazar ve kitap ekle
author1 = Author(name="George Orwell", email="george@example.com")
library.add_author(author1)

book1 = Book(title="1984", description="Dystopian novel.", published_date=date(1949, 6, 8), author=author1)
book2 = Book(title="Animal Farm", description="Political satire.", published_date=date(1945, 8, 17), author=author1)

library.add_book(book1)
library.add_book(book2)

# Kitapları listele
print("\nTüm Kitaplar:")
library.list_books()

# Belirli yazara ait kitaplar
print("\nGeorge Orwell'ın Kitapları:")
books_by_orwell = library.find_books_by_author("George Orwell")
for book in books_by_orwell:
    print(book.title)


class Teacher:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
        self.courses = []

    def enroll(self, course):
        self.courses.append(course)

class Course:
    def __init__(self, name, teacher):
        self.name = name
        self.teacher = teacher

class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Waiter:
    def __init__(self, name):
        self.name = name

    def take_order(self, customer, item):
        customer.orders.append(item)

class Customer:
    def __init__(self, name):
        self.name = name
        self.orders = []

    def total_bill(self):
        return sum(item.price for item in self.orders)
    
    
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Customer:
    def __init__(self, name):
        self.name = name
        self.cart = []

    def add_to_cart(self, product):
        self.cart.append(product)

class Order:
    def __init__(self, customer):
        self.customer = customer
        self.products = customer.cart.copy()

    def total_price(self):
        return sum(product.price for product in self.products)

    
class Task:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Heyo:
    def __init__(self, customer):
        self.customer = customer
        self.products = customer.cart.copy()

    def total_price(self):
        return sum(product.price for product in self.products)
    
class Customer:
    def __init__(self, name):
        self.name = name
        self.cart = []

    def add_to_cart(self, product):
        self.cart.append(product)