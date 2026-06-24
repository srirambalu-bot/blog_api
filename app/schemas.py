from pydantic import BaseModel

class UserCreate (BaseModel):
    username : str
    email : str
    password : str
    
class UserResponse (BaseModel):
    id : int
    username : str
    email: str    

class UserLogin(BaseModel):
    email: str
    password: str

class PostCreate (BaseModel):
    title : str
    content : str

class UserPublic(BaseModel):

    username : str
    id : int

class PostResponse (BaseModel):
    id : int
    title : str
    content : str
    owner : UserPublic

    class Config:
        from_attributes = True

class PostUpdate(BaseModel):
    
    title: str | None = None
    content : str |None = None






