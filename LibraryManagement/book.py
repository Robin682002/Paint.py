class Book:
    def __init__(self, title, author, isbn, copies):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.copies = copies

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Copies: {self.copies}"

    def borrow_book(self):
        if self.copies > 0:
            self.copies -= 1
            return True
        return False

    def return_book(self):
        self.copies += 1