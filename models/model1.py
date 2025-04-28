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
