from fastapi import HTTPException, status


class APIException:
    
    NOT_FOUND = HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, 
        detail="Страница не найдена"
    )
    
    UNAUTHORIZED = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED, 
        detail="Пользователь не авторизован"
    )
    
    FORBIDDEN = HTTPException(
        status_code=status.HTTP_403_FORBIDDEN, 
        detail="Доступ запрещен"
    )
    
    BAD_REQUEST = HTTPException(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
        detail="Ошибка сервера"
    )
    UserAlreadyExistsException = HTTPException(
        status_code=status.HTTP_409_CONFLICT,
        detail="Пользователь уже существует",
    )

    IncorrectEmailOrPasswordException = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Неверная почта или пароль",
    )

    TokenExpiredException = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Токен истек",
    )

    TokenAbsentException = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Токен отсутствует",
    )

    IncorrectTokenFormatException = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Неверный формат токена",
    )

    UserIsNotPresentException = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        )    

    UserAlreadyExistsException = HTTPException(
        status_code=status.HTTP_409_CONFLICT,
        detail="Пользователь уже существует",
    )

    AccessRightsException = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="У вас недостаточно прав",
    ) 

    RoomCannotBeBookedException = HTTPException(
        status_code=status.HTTP_409_CONFLICT,
        detail="Не осталось свободных номеров",
    ) 

    DateFromCannotBeAfterDateTo = HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="Дата заезда не может быть позже даты выезда",
    )

    CannotBookHotelForLongPeriod = HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="Невозможно забронировать отель сроком более месяца",
    )