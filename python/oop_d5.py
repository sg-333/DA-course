# TASK: Add remove_book method and update using File Handling and Exception Handling

# book objects with title, author, pages
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

# ebook subclass with file_size
class EBook(Book):
    def __init__(self, title, author, pages, file_size):
        super().__init__(title, author, pages) # Call parent constructor
        self.file_size = file_size

# Sample book and ebook objects
book1 = Book("Art of War", "Sun Tzu", 180)
book2 = Book("To Kill a Mockingbird", "Harper Lee", 281)
book3 = EBook("Digital Fortress", "Dan Brown", 356, "1.5MB")
book4 = EBook("1984", "George Orwell", 328, "2MB") 

# Library Management System
class LMS:
    def __init__(self): # Initialize the books list
        self.books = []

    def add_book(self, book): # Add book to the list and save to file
        self.books.append(book)
        self.save_books_to_file()

    def search_book(self): # Search for a book by title
        book_name = input("Enter book name: ")
        for i in self.books:
            if i.title == book_name:
                print("Book found in the Library.")
                break
        else:
            print("Book not found.")
    
    def remove_book(self): # Remove a book by title
        book_name = input("Enter book name to remove: ")
        for i in self.books:
            if i.title == book_name:
                self.books.remove(i) # remove method for list
                print(f"Book '{book_name}' removed from the Library.")
                self.save_books_to_file() # Update file after removal
                break
        else:
            print("Book not found. Cannot remove.")

    def display_books(self): # Display all books added in the library
        for i in self.books:
            print(i.title)
            print(i.author)
            print(i.pages)
            if isinstance(i, EBook): # Check if "i" is an EBook
                print(i.file_size)
            print("----------------")

    def save_books_to_file(self): # Save current books to a file 
        try:
            file = open("oopd5.txt", "w")
            for i in self.books:
                if isinstance(i, EBook):
                    file.write(f"EBook: {i.title}, {i.author}, {i.pages}, {i.file_size}\n")
                else:
                    file.write(f"Book: {i.title}, {i.author}, {i.pages}\n")
            file.close()
        except Exception as e:
            print(e)


lms = LMS()
lms.add_book(book1)
lms.add_book(book2)
lms.add_book(book3)
lms.add_book(book4)
lms.display_books()

# lms.search_book()
# lms.remove_book()
# lms.display_books()