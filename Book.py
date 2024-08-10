class LibraryItem:
    def __init__(self, author, genre, isbn):
        self.author = author
        self.genre = genre
        self.isbn = isbn

    def get_details(self):
          pass

class Book(LibraryItem):
    def __init__(self, author, genre, isbn, title):
        super().__init__(author, genre, isbn)
        self.title = title
        self.availability = True  

    def ReturnBook(self,genre,isbn,title):
        book3 = Book(author=Author, genre=genre, isbn=isbn, title=title)
        records.append(book3)
        print("RETURNED")

    def checkout(self):
        if self.availability:
            self.availability = False
            return "Book checked out"
        else:
            return "Book is not available"

    def get_details(self):
        return {
            'author': self.author,
            'genre': self.genre,
            'isbn': self.isbn,
            'title': self.title,
            'availability': self.availability
        }
    def Add_to_library(author,genre,isbn):
        book2=Book(author=Author, genre=genre, isbn=isbn, title=title)
        records.append(book2)



        

records = []
print("Enter the book details")
Author=input("Enter author name:")
genre=input("Enter the genre:")
title=input("Enter book title:")
isbn=input("Enter isbn:")
book1 = Book(author=Author, genre=genre, isbn=isbn, title=title)
records.append(book1)
checkout_message = book1.checkout()
Add_to_library=book1.Add_to_library(Author,genre,title,isbn)
return_book=book1.ReturnBook(genre,isbn,title)
print(return_book)
print(checkout_message)
details = book1.get_details()
print(details)

            





    
