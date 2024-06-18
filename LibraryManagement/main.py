from library import Library
from book import Book
from member import Student, Teacher

def main():
    library = Library()

    while True:
        print("\n===== Library Management System Menu =====")
        print("1. Add Book")
        print("2. Add Member")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Display Books")
        print("6. Display Members")
        print("7. Save Books to CSV")
        print("8. Save Members to CSV")
        print("9. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            isbn = input("Enter book ISBN: ")
            copies = int(input("Enter number of copies: "))
            book = Book(title, author, isbn, copies)
            library.add_book(book)
            print(f"Added '{title}' to the library.")

        elif choice == "2":
            member_type = input("Enter member type (Student/Teacher): ").lower()
            member_id = input("Enter member ID: ")
            name = input("Enter member name: ")

            if member_type == "student":
                grade = input("Enter student grade: ")
                member = Student(member_id, name, grade)
            elif member_type == "teacher":
                subject = input("Enter teacher subject: ")
                member = Teacher(member_id, name, subject)
            else:
                print("Invalid member type. Please enter either 'Student' or 'Teacher'.")
                continue

            library.add_member(member)
            print(f"Added {member_type} '{name}' to the library.")

        elif choice == "3":
            member_id = input("Enter member ID: ")
            isbn = input("Enter book ISBN to borrow: ")
            if library.borrow_book(member_id, isbn):
                print(f"Book with ISBN {isbn} borrowed successfully.")
            else:
                print("Failed to borrow the book. Please check member ID or book availability.")

        elif choice == "4":
            member_id = input("Enter member ID: ")
            isbn = input("Enter book ISBN to return: ")
            if library.return_book(member_id, isbn):
                print(f"Book with ISBN {isbn} returned successfully.")
            else:
                print("Failed to return the book. Please check member ID or book status.")

        elif choice == "5":
            library.display_books()

        elif choice == "6":
            library.display_members()

        elif choice == "7":
            filename = input("Enter filename to save books (e.g., books.csv): ")
            library.save_books_to_csv(filename)
            print(f"Books saved to '{filename}'.")

        elif choice == "8":
            filename = input("Enter filename to save members (e.g., members.csv): ")
            library.save_members_to_csv(filename)
            print(f"Members saved to '{filename}'.")

        elif choice == "9":
            print("Exiting Library Management System. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 9.")

if __name__ == "__main__":
    main()