# This lesson is about dunder method in Python


class Book:

    def __init__(self, title: str, author: str, pages: int):
        self.title = title
        self.author = author
        self.pages = pages
    
    def __str__(self):
        return f'Title: {self.title}\nAuthor: {self.author}\nPages: {self.pages} pages'


book1 = Book("Crime and Punishment", "Feodor Dostoyevsky", 500)
book2 = Book("Lolita", "Wladimir Nabokov",400)

print(book1)
print(book2)