from fastapi import FastAPI,Depends,HTTPException
from .database import Base,engine,get_db
from .model import User,Post
from sqlalchemy.orm import Session
from .schemas import UserCreate, UserResponse,UserLogin,PostCreate,UserResponse,PostUpdate,PostResponse
from .utils import verify_password,hash_password
from .auth import create_access_token,get_current_user
from fastapi.security import OAuth2PasswordRequestForm

app =FastAPI()
Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message":"blog_api is running "}

@app.post("/users",response_model =UserResponse)
def create_user(user:UserCreate,db: Session = Depends(get_db)):
    new_user = User(username=user.username,
                    
                    email =user.email,
                    password = hash_password(user.password))
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

@app.get("/users")
def get_user(db:Session = Depends(get_db)):
    users = db.query(User).all()

    return users

@app.get("/user/{id}")
def get_user(id:int,db:Session = Depends(get_db)):
    user = db.query(User).filter(User.id==id).first()

    if user is None:
        raise HTTPException(status_code=404,detail = "user not found")


    return user

@app.delete("/user/{id}")
def user_delete(id:int,db:Session = Depends(get_db)):
    user = db.query(User).filter(User.id == id).first()
    
    if user is None :
        raise HTTPException (status_code=404,detail ="user not found")
    
    db.delete(user)
    db.commit()

    return {"message":"user deleted successfully"}

@app.post("/login")
def login(login_data:OAuth2PasswordRequestForm = Depends(),db:Session = Depends(get_db)):
    user = db.query(User).filter(User.email == login_data.username).first()

    if user is None :
        raise HTTPException(status_code = 401,detail="invalid credentials")
    
    if not verify_password(login_data.password ,user.password):
        raise HTTPException (status_code=401,detail = "invalid password")
    
    token = create_access_token(
    data={"user_id": user.id}
    )

    return {
    "access_token": token,
    "token_type": "bearer"
    }
@app.get("/profile")
def get_profile (current_user =Depends(get_current_user)):
    
    if current_user is None:
        raise HTTPException(status_code=401,detail="invalid credentials")
    

    return current_user
@app.post("/posts",response_model=UserResponse)
def Post_Create(post:PostCreate,current_user= Depends(get_current_user),db:Session =Depends(get_db)):
    #db:Session =Depends(get_db)
    new_post= Post(title=post.title,
                   content=post.content,
                   owner_id=current_user.id)
    
    db.add(new_post)
    db.commit()
    db.refresh(new_post)

    return new_post
    
@app.get("/posts",response_model=list[PostResponse])
def  post_get(db:Session = Depends(get_db)):
    posts =db.query(Post).all()

    return posts

@app.get("/post/{id}",response_model=PostResponse)
def posts_get_id(id:int,db:Session=Depends(get_db)):

    
    post = db.query(Post).filter(Post.id == id).first()
    if post is None:
        
        raise HTTPException(status_code=404,detail="post not found")


    return post

@app.put("/post/{id}")
def update_post(
    id: int,
    post_data: PostUpdate,
    current_user = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    post = db.query(Post).filter(Post.id == id).first()

    if post is None:
        raise HTTPException(
            status_code=404,
            detail="post not found"
        )

    if post.owner_id != current_user.id:
        raise HTTPException(
            status_code=403,
            detail="not authorized"
        )

    if post_data.title is not None:
        post.title = post_data.title

    if post_data.content is not None:
        post.content = post_data.content

    db.commit()
    db.refresh(post)

    return post




