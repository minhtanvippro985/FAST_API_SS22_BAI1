from datetime import datetime, timezone, timedelta
import jwt
import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY", "default_secret_key_change_me")
ALGORITHM = os.getenv("ALGORITHM", "HS256")

def generate_access_token(username: str) -> str:
    now = datetime.now(timezone.utc)
    expire_time = now + timedelta(minutes=30)

    payload = {
        "sub": username,
        "iat": int(now.timestamp()),
        "exp": expire_time
    }

    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return token

def decode_access_token(token: str) -> dict:
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    return payload