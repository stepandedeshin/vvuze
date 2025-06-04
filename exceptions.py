from fastapi import HTTPException, status


class APIException:
    
    NOT_FOUND = HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Страница не найдена")
    UNAUTHORIZED = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Пользователь не авторизован")
    FORBIDDEN = HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Доступ запрещен")
    BAD_REQUEST = HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Ошибка сервера")
    