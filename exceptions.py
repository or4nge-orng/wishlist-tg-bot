class CoupleWishesException(Exception):
    pass


class NoUserFoundError(CoupleWishesException):
    def __str__(self):
        return "Пользователь не найден"


class UserAlreadyExistsError(CoupleWishesException):
    def __str__(self):
        return "Такой пользователь уже существует"