# Define the Book class
class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def displayInfo(self):
        return f"Book Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}"


# Define the ReferenceBook class inheriting from Book
class ReferenceBook(Book):
    def __init__(self, title, author, isbn, subject):
        super().__init__(title, author, isbn)
        self.subject = subject

    def displayInfo(self):
        return f"Reference Book Title: {self.title}, Subject: {self.subject}, Author: {self.author}, ISBN: {self.isbn}"


# Demonstration
# Creating a regular book object
book1 = Book("Python Programming", "John Doe", "1234567890")

# Creating a reference book object
ref_book1 = ReferenceBook("Advanced Algorithms", "Jane Smith", "0987654321", "Computer Science")

# Display information
print(book1.displayInfo())  # Polymorphism: Book display
print(ref_book1.displayInfo())  # Polymorphism: ReferenceBook display


# Encapsulation: Attributes like title, author, and isbn are encapsulated within the Book and ReferenceBook classes.
# Inheritance: ReferenceBook extends the Book class by adding a subject attribute.
# Polymorphism: The displayInfo() method is overridden in ReferenceBook to provide a customized display format.