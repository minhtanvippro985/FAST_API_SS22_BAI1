from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from models.user import UserModel
from schemas.schemas import RegisterRequest, LoginRequest
from security.password import hash_password, verify_password
from security.jwt import generate_access_token

def register_handler(user_create: RegisterRequest, db: Session):
    check_duplicate_user = db.query(UserModel).filter(UserModel.username == user_create.username).first()

    if check_duplicate_user:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Username already exists")

    hashed_pass = hash_password(user_create.password)
    user = UserModel(
        username=user_create.username,
        hash_password=hashed_pass
    )
    try:
        db.add(user)
        db.commit()
        db.refresh(user)
        return {
            "message": "user account created",
            "username": user_create.username
        }
    except Exception:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="error")

def login_handler(request: LoginRequest, db: Session):
    user = db.query(UserModel).filter(UserModel.username == request.username).first()

    if not user or not verify_password(request.password, user.hash_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="invalid user or password"
        )

    token = generate_access_token(user.username)
    return {"access_token": token, "token_type": "bearer"}