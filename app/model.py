from .database import Base
from sqlalchemy import Column,Integer,String,ForeignKey,DateTime
from sqlalchemy.orm import relationship
class User(Base):
    __tablename__ = "users"
    id =Column(Integer,primary_key = True)
    username =Column(String)
    email = Column(String,unique = True)
    password = Column(String)

    posts = relationship(
        "Post",
        back_populates="owner"
    )

class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer,primary_key=True)
    title = Column(String)
    content = Column(String)

    owner_id = Column(Integer,
                    ForeignKey("users.id"))
    created_at = Column(DateTime)

    owner = relationship("User",
                        back_populates="posts")

