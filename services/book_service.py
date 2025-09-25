from models.book import Book

def list_books(library):
    return [book.to_dict() for book in library.books]

def get_book(isbn:str, library):
    book = library.find_book(isbn)
    return book.to_dict() if book else None

def add_book(data:dict, library):
    book = Book(title=data.get("title"),author=data.get("author"),isbn=("isbn"),
                pages=data.get("pages", 0),release_date=data.get("release_date"),price=data.get("price",0.0),available=True)

def remove_book(isbn:str, library):
    book = library.find_book(isbn)
    if book:
        library.remove_book(isbn)
        return True
    return False

def borrow_book(isbn:str, user_id:int, library, user_manager):
    user = user_manager.find_user(user_id)
    if not user:
        return {"error":"User not found"}, False
    
    if user.borrow_book(library,isbn):
        return {"message":f"User {user_id} borrowed {isbn}."}, True
    
    return {"error":"Book not available"}, False

def return_book(isbn:str, user_id:int, library, user_manager):
    user = user_manager.find_user(user_id)

    if not user:
        return {"error":"User not found"}, False
    
    if user.return_book(library,isbn):
        return {"message":f"User {user_id} returned {isbn}."}, True
    
    return {"error":"Book was not borrowed"}, False