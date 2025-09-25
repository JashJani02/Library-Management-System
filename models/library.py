class Library:
    
    def __init__(self):
        self.books = []

    def add_book(self,book):
        self.books.append(book)

    def remove_book(self,isbn):
        self.books = [book for book in self.books if book.isbn != isbn]

    def find_book(self,isbn):
        for book in self.books:

            if book.isbn == isbn:
                return book
        
        return None
        
    def list_books(self):
        return [str(book) for book in self.books]
    
    def borrow_book(self,isbn):

        book = self.find_book(isbn)

        if book and book.available:
            book.available = False
            return True
        return False
    
    def return_book(self,isbn):

        book = self.find_book(isbn)

        if book and not book.available:
            book.available = True
            return True
        return False
    
    def find_by_author(self,author):
        return [book for book in self.books if book.author.lower() == author.lower()]
    
    def find_by_title(self,title):
        return [book for book in self.books if title.lower() in book.title.lower()]
    
    def get_available_books(self):
        return [book for book in self.books if book.available]
    
    def get_borrowed_books(self):
        return [book for book in self.books if not book.available]
    
    def count_available_books(self):
        return len(self.get_available_books())
    
    def count_borrowed_books(self):
        return len(self.get_borrowed_books())
    
    def count_total_books(self):
        return len(self.books)
    