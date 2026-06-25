from jose import jwt
from datetime import datetime, timedelta
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from .database import get_db
from .model import User
import os
from dotenv import load_dotenv

load_dotenv()





SECRET_KEY =  os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))

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