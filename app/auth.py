from jose import jwt
from datetime import datetime, timedelta
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from .database import get_db
from .model import User


SECRET_KEY = "mysecretkey"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data:dict):
    expire = datetime.utcnow()+ timedelta(minutes =ACCESS_TOKEN_EXPIRE_MINUTES)
    data["exp"] = expire
    token = jwt.encode(
        data,
        SECRET_KEY,
        algorithm=ALGORITHM)

    return token 
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")
def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
):
    payload = jwt.decode(
    token,
    SECRET_KEY,
    algorithms=[ALGORITHM]
)
    user_id = payload["user_id"]
    user = db.query(User).filter(User.id == user_id).first()
    
    return user