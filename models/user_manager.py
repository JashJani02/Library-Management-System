from models import User

class UserManager:

    def __init__(self):
        self.users = []

    def add_user(self, user:User):
        self.users.append(user)
        return user
    
    def remove_user(self,user_id):
        self.users = [user for user in self.users if user.user_id != user_id]
    
    def find_user(self,user_id):
        for user in self.users:

            if user.user_id == user_id:
                return user
            
        return None

    def find_by_email(self,email):
        for user in self.users:
           if user.email.lower() == email.lower():
               return user
        return None

    def list_users(self):
      return [str(user) for user in self.users]  # return all users (maybe as dicts)

    def count_users(self):
       return len(self.users) # return total number of users

    def list_all_borrowed_books(self, library):
        borrowed_books = {}

        for user in self.users:

            borrowed = user.list_borrow_book(library)
            borrowed_books[user.user_id] = [str(book) for book in borrowed]

        return borrowed_books