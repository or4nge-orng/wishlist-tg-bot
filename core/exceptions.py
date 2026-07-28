class CoupleWishesException(Exception):
    pass

# ----- User Exception -----

class NoUserFoundError(CoupleWishesException):
    def __init__(self, username):
        super().__init__(username)
        self.user_id = username
    def __str__(self):
        return f"Пользователь {self.username} не найден"

class UserAlreadyExistsError(CoupleWishesException):
    def __str__(self):
        return "Такой пользователь уже существует"
    
class UserCreationError(CoupleWishesException):
    def __str__(self):
        return "Ошибка добавления нового пользователя"
    
class UserUpdateError(CoupleWishesException):
    def __str__(self):
        return "Ошибка обновления пользователя"
    
class UserDeleteError(CoupleWishesException):
    def __str__(self):
        return "Ошибка удаления пользователя"
    
# ----- Couple Exception -----
class NoCoupleFoundError(CoupleWishesException):
    def __str__(self):
        return "Пара не найдена"
    
class CoupleCreationError(CoupleWishesException):
    def __str__(self):
        return "Ошибка добавления новой пары"
    
class CoupleDeleteError(CoupleWishesException):
    def __str__(self):
        return "Ошибка удаления пары"
    
class CoupleUpdateError(CoupleWishesException):
    def __str__(self):
        return "Ошибка обновления пары"
    
# ----- Wish Exception -----
class WishCreationError(CoupleWishesException):
    def __str__(self):
        return "Ошибка добавления нового желания"

class NoWishFoundError(CoupleWishesException):
    def __str__(self):
        return "Желание не найдено"
    
class WishDeleteError(CoupleWishesException):
    def __init__(self, wish_id):
        super().__init__(wish_id)
        self.wish_id = wish_id
    def __str__(self):
        return f"Ошибка удаления желания {self.wish_id}"
    
class WishUpdateError(CoupleWishesException):
    def __init__(self, wish_id):
        super().__init__(wish_id)
        self.wish_id = wish_id
    def __str__(self):
        return f"Ошибка изменения желания {self.wish_id}"