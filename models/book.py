class Book:

    def __init__(self,title:str,author:str,isbn:str,pages:int,release_date:str,price:float,available:bool=True):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.pages = pages
        self.release_date = release_date
        self.price = price
        self.available = available

    def __str__(self):
        return f"{self.title} by {self.author}, ISBN: {self.isbn}, Pages: {self.pages}, Released: {self.release_date}, Price: ${self.price:.2f}, Available: {'Yes' if self.available else 'No'}"
    
    def to_dict(self):
        return {
            'title':self.title,
            'author':self.author,
            'isbn':self.isbn,
            'pages':self.pages,
            'release_date':self.release_date,
            'price':self.price,
            'available':self.available
        }
    
    def update_info(self,**kwargs):
        for key,value in kwargs.items():
            if hasattr(self,key):
                setattr(self,key,value)