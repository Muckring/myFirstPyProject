# This lesson is about dunder method in Python


class Book:

    def __init__(self, title: str, author: str, pages: int) -> None:

        self.title = title
        self.author = author
        self.pages = pages
    
    # THIS METHOD HELPS CUSTOMIZE THE STRING REPRESENTATION OF AN OBJECT

    def __str__(self) -> str:
        
        return f'Title: {self.title}\nAuthor: {self.author}\nPages: {self.pages} pages'
    
    # THIS METHOD HELPS CHECKS IF TWO OBJECTS ARE EQUAL. IT IS ALSO CUSTOMIZABLE

    def __eq__(self, other) -> bool:
        return self.title == other.title and self.author == other.author

    # BELOW ARE TWO MAGIC METHODS THAT CHECK IF AN OBJECT IS GREATER OR LESS
    # THAN ANOTHER OBJECT

    def __lt__(self, other) -> bool:
        return self.pages < other.pages

    def __gt__(self, other) -> bool:
        return  self.pages > other.pages

    # THIS METHOD ADDS OBJECT PROPERTIES THAT CAN BE ADDED

    def __add__(self, other) -> int:
        return self.pages + other.pages

    # THIS METHOD CHECKS IF A CERTAIN KEYWORD EXISTS IN ONE OF AN OBJECT'S PROPERTIES

    def __contains__(self, keyword) -> bool:
        return keyword in self.title or keyword in self.author
    
    # THIS METHOD CHECKS IF A CERTAIN KEY EXISTS IN AN OBJECT AND RETURNS 
    # ITS VALUE

    def __getitem__(self, key) -> bool:
        
        if key == "title":
            return self.title
        if key == "author":
            return self.author
        if key == "pages":
            return self.pages


book1 = Book("Crime and Punishment", "Feodor Dostoyevsky", 500)
book2 = Book("Lolita", "Wladimir Nabokov",400)
book3 = Book("Hobbit", "Tolkien", 2999)
book4 = Book("Lolita", "Wladimir Nabokov",699)

""" print(book1)
print(book2 == book4)
print(book2 < book4)
print(book2 > book4) """

print(f"Total amount of pages: {book1 + book2} pages")
print("Lolita" in book4)
print(book1["title"])
print(book2["author"])
print(book3["pages"])