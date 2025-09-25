from models.user import User

def list_user(user_manager):
    return [user.to_dict() for user in user_manager.users]

def get_user(user_id:int, user_manager):
    user = user_manager.find_user(user_id)
    return user.to_dict() if user else None

def add_user(data:dict, user_manager):
    user = User(user_id=data.get("user_id"),name=data.get("name"),email=data.get("email"))
    user_manager.add_user(user)
    return user.to_dict()

def remove_user(user_id:int, user_manager):
    user = user_manager.find_user(user_id)
    if user:
        user_manager.remove_user(user_id)
        return True
    return False

def list_borrowed_books(user_id:int, user_manager, library):
    user = user_manager.find_user(user_id)

    if not user:
        return None
    return [book.to_dict() for book in user.list_borrow_book(library)]