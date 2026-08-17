from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
import jwt
from security.jwt import decode_access_token

router = APIRouter(prefix="/api", tags=["User Profile"])

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/login")

@router.get("/profile")
def get_profile(token: str = Depends(oauth2_scheme)):
    try:
        payload = decode_access_token(token)
        username: str = payload.get("sub")
        
        if username is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token không hợp lệ"
            )
            
        return {"message": f"Welcome, {username}!"}

    except jwt.ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token đã hết hạn, vui lòng đăng nhập lại"
        )
    except jwt.PyJWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token không hợp lệ"
        )