from fastapi import Request, HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from src.exceptions import AuthenticationError, PermissionDeniedError
from src.user.jwt_handler import decodeJWT

class JWTBearer(HTTPBearer):
    def __init__(self, required_role: str = None, auto_error: bool = True):
        super(JWTBearer, self).__init__(auto_error=auto_error)
        self.required_role = required_role

    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super(JWTBearer, self).__call__(request)
        if credentials:
            if credentials.scheme != "Bearer":
                raise PermissionDeniedError("Invalid authentication scheme")
            payload = self.verify_jwt(credentials.credentials)
            if not payload:
                raise AuthenticationError("Invalid credentials provided")

            # Check if the role matches the required role
            user_role = payload.get("role")
            if self.required_role and user_role != self.required_role:
                raise PermissionDeniedError(f"Access denied. Requires {self.required_role} role.")
            return credentials.credentials
        raise AuthenticationError("No credentials provided.")

    def verify_jwt(self, jwtoken: str) -> dict:
        payload = decodeJWT(jwtoken)
        return payload if payload else None
