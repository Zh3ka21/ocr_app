from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from auth.models import User
from database import SessionLocal
from src.auth.service import authenticate_user, create_access_token, get_password_hash
from src.auth.schemas import Token, UserCreate, UserOut
from datetime import timedelta
from src.auth.config import settings

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/token", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    
    access_token = create_access_token(
        data={"sub": user.username},
        expires_delta=timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    )
    return {"access_token": access_token, "token_type": "bearer"}


@router.post("/register", response_model=UserOut)
def register(user_in: UserCreate):
    db = SessionLocal()
    existing = db.query(User).filter(User.username == user_in.username).first()
    if existing:
        db.close()
        raise HTTPException(status_code=400, detail="Username already exists")

    hashed_pw = get_password_hash(user_in.password)
    user = User(
        username=user_in.username,
        email=user_in.email,
        hashed_password=hashed_pw,
        full_name=user_in.full_name
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    db.close()
    return user


@router.post("/logout")
def logout():
    return {"msg": "Successfully logged out (client must discard the token)"}
