class User:

    def __init__(self,user_id:int,name:str,email:str,borrowed_books=None):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.borrowed_books = borrowed_books if borrowed_books is not None else []

    def __str__(self):
        return f"User: {self.name}, Email: {self.email}, User id: {self.user_id}, Borrowed Books: {len(self.borrowed_books)}"
    
    def to_dict(self):
        return {
            'user_id':self.user_id,
            'name':self.name,
            'email':self.email,
            'borrowed_books':self.borrowed_books
        }
    
    def borrow_book(self,library,isbn:str):
        borrowed = library.borrow_book(isbn)

        if borrowed:
            self.borrowed_books.append(isbn)
            return True
        return False

    def return_book(self,library,isbn:str):
        returned = library.return_book(isbn)

        if returned and isbn in self.borrowed_books:
            self.borrowed_books.remove(isbn)
            return True
        return False

    def list_borrow_book(self,library):
        return [library.find_book(isbn) for isbn in self.borrowed_books if library.find_book(isbn)]

    def count_borrow_book(self):
        return len(self.borrowed_books)