from fastapi import HTTPException, status

UserAlreadyExistsException = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail="Пользователь уже существует",
)

IncorrectEmailOrPasswordException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Некорректная почта или пароль",
)

TokenExpireException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Токен истек",
)

TokenAbsentException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Токен отсутствует",
)

IncorrectTokenFormatException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Неккоректный формат токена",
)

UserIsNotPresentException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Пользователь не найден",
)

TaskNotFoundException = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
     detail="Задача не найдена"
)

GroupNotFoundException = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
     detail="Группа не найдена"
)
