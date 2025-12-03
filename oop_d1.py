# Create a Simple Book Class
# Objective: Design a class to represent a book, including its title, author, and a method to display the book's information

class Book:
    def book_info(self, title, author):
        self.title = title
        self.author = author
    
    def display_info(self):
        print(f"Title: {self.title}, Author: {self.author}")

book1 = Book()
book1.book_info("The Art of War", "Sun Tzu")
book1.display_info()