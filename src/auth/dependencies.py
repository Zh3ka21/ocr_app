from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from src.auth.service import verify_access_token
from src.auth.schemas import User

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token")

def get_current_user(token: str = Depends(oauth2_scheme)) -> User:
    payload = verify_access_token(token)
    if not payload:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return User(**payload)
