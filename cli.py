from database import SessionLocal
from models.author import Author
from models.book import Book

class LibraryCLI:
    def __init__(self):
        self.session = SessionLocal()


    def display_menu(self):
        print("Welcome to Library Management System")
        print("1. Add Author")
        print("2. Add Book")
        print("3. List Authors")
        print("4. List Books")
        print("5. Delete Author")
        print("6. Delete Book")
        print("7. Exit")

    def add_author(self):
        name = input("Enter author name: ")
        author = Author(name=name)
        self.session.add(author)
        self.session.commit()
        print("Author added successfully!")

    def add_book(self):
        title = input("Enter book title: ")
        author_id = input("Enter author ID: ")
        author = self.session.query(Author).filter_by(id=author_id).first()
        if author:
            book = Book(title=title, author_id=author_id)
            self.session.add(book)
            self.session.commit()
            print("Book added successfully!")
        else:
            print("Author not found!")

    def list_authors(self):
        authors = self.session.query(Author).all()
        for author in authors:
            print(f"{author.id}. {author.name}")

    def list_books(self):
        books = self.session.query(Book).all()
        if books:
            print("Books:")
            for book in books:
                print(f"{book.id}. {book.title} - {book.author.name}")
        else:
            print("No books found.")

    def delete_book(self):
        self.list_books()  # Display all books with their IDs
        book_id = input("Enter book ID to delete: ")
        book = self.session.query(Book).filter_by(id=book_id).first()
        if book:
            self.session.delete(book)
            self.session.commit()
            print("Book deleted successfully!")
        else:
            print("Book not found!")

    def delete_author(self):
        author_id = input("Enter author ID to delete: ")
        author = self.session.query(Author).filter_by(id=author_id).first()
        if author:
            books = self.session.query(Book).filter_by(author_id=author_id).all()
            if books:
                print("Cannot delete author because there are books associated with this author:")
                for book in books:
                    print(f"- {book.title}")
            else:
                self.session.delete(author)
                self.session.commit()
                print("Author deleted successfully!")
        else:
            print("Author not found!")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")
            if choice == '1':
                self.add_author()
            elif choice == '2':
                self.add_book()
            elif choice == '3':
                self.list_authors()
            elif choice == '4':
                self.list_books()
            elif choice == '5':
                self.delete_author()
            elif choice == '6':
                self.delete_book()
            elif choice == '7':
                print("Exiting...")
                break
            else:
                print("Invalid choice!")

    
if __name__ == "__main__":
    cli = LibraryCLI()
    cli.run()
