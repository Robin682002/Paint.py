class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def __str__(self):
        return f"Member ID: {self.member_id}, Name: {self.name}"

    def borrow_book(self, book):
        if book.borrow_book():
            self.borrowed_books.append(book)
            return True
        return False

    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
            return True
        return False

class Student(Member):
    def __init__(self, member_id, name, grade):
        super().__init__(member_id, name)
        self.grade = grade

    def __str__(self):
        return f"Student - {super().__str__()}, Grade: {self.grade}"

class Teacher(Member):
    def __init__(self, member_id, name, subject):
        super().__init__(member_id, name)
        self.subject = subject

    def __str__(self):
        return f"Teacher - {super().__str__()}, Subject: {self.subject}"