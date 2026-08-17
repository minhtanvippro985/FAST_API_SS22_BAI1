from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from schemas.schemas import RegisterRequest, LoginRequest, TokenResponse
from services.user_handlers import register_handler, login_handler

router = APIRouter(prefix="/api", tags=["Auth"])

@router.post("/register")
def register(user_data: RegisterRequest, db: Session = Depends(get_db)):
    return register_handler(user_data, db)

@router.post("/login", response_model=TokenResponse)
def login(request: LoginRequest, db: Session = Depends(get_db)):
    return login_handler(request, db)