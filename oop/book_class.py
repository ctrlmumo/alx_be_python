# oop/book_class.py

class Book:
    # Constructor
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    # String representation (user-friendly)
    def __str__(self):
        return f"{self.title} by {self.author}, published in {self.year}"

    # Official representation (developer-friendly)
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.year})"

    # Destructor
    def __del__(self):
        print(f"Deleting {self.title}")
