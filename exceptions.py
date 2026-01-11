class CoupleWishesException(Exception):
    pass

# ----- User Exception -----

class NoUserFoundError(CoupleWishesException):
    def __init__(self, user_id):
        super().__init__(user_id)
        self.user_id = user_id
    def __str__(self):
        return f"Пользователь {self.user_id} не найден"

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

class NoWishFoundError(CoupleWishesException):
    def __str__(self):
        return "Желание не найдено"