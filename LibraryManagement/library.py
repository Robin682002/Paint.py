from book import Book
from member import Member, Student, Teacher
import csv

class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)

    def add_member(self, member):
        self.members.append(member)

    def find_book_by_isbn(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None

    def find_member_by_id(self, member_id):
        for member in self.members:
            if member.member_id == member_id:
                return member
        return None

    def borrow_book(self, member_id, isbn):
        member = self.find_member_by_id(member_id)
        book = self.find_book_by_isbn(isbn)
        if member and book:
            return member.borrow_book(book)
        return False

    def return_book(self, member_id, isbn):
        member = self.find_member_by_id(member_id)
        book = self.find_book_by_isbn(isbn)
        if member and book:
            return member.return_book(book)
        return False

    def display_books(self):
        print("Books in the library:")
        for book in self.books:
            print(book)

    def display_members(self):
        print("Members of the library:")
        for member in self.members:
            print(member)

    def save_books_to_csv(self, filename):
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Title", "Author", "ISBN", "Copies"])
            for book in self.books:
                writer.writerow([book.title, book.author, book.isbn, book.copies])

    def save_members_to_csv(self, filename):
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Member ID", "Name", "Type", "Grade/Subject"])
            for member in self.members:
                if isinstance(member, Student):
                    writer.writerow([member.member_id, member.name, "Student", member.grade])
                elif isinstance(member, Teacher):
                    writer.writerow([member.member_id, member.name, "Teacher", member.subject])
                else:
                    writer.writerow([member.member_id, member.name, "Unknown", ""])