from fastapi import HTTPException, status

class BaseAPIException(HTTPException):
    def __init__(self, status_code: int, error: str, message: str, data=None):
        detail = {
            "status": "error",
            "message": message,
            "code": status_code,
            "data": data if data is not None else None
        }
        super().__init__(status_code=status_code, detail=detail)


class DataNotFoundError(BaseAPIException):
    def __init__(self, message: str = "Requested data not found"):
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            error="DataNotFoundError",
            message=message,
            data=None
        )


class AuthenticationError(BaseAPIException):
    def __init__(self, message: str = "Invalid credentials provided"):
        super().__init__(
            status_code=status.HTTP_401_UNAUTHORIZED,
            error="AuthenticationError",
            message=message,
            data=None
        )


class PermissionDeniedError(BaseAPIException):
    def __init__(self, message: str = "Permission denied"):
        super().__init__(
            status_code=status.HTTP_403_FORBIDDEN,
            error="PermissionDeniedError",
            message=message,
            data=None
        )


class ConflictError(BaseAPIException):
    def __init__(self, message: str = "Conflict error"):
        super().__init__(
            status_code=status.HTTP_409_CONFLICT,
            error="ConflictError",
            message=message,
            data=None
        )


class ValidationError(BaseAPIException):
    def __init__(self, message: str = "Validation failed", errors=None):
        data = {"errors": errors} if errors else None
        super().__init__(
            status_code=status.HTTP_400_BAD_REQUEST,
            error="ValidationError",
            message=message,
            data=data
        )
