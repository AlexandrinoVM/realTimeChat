from backend.database import Base
from sqlalchemy import ForeignKey,Column,String,Integer,Boolean
from sqlalchemy.orm import relationship
from models.schemas_model import ChatRoomUser

class UserModel(Base):
    __tablename__ = "users"
    __table_args__ = {'extend_existing': True}
    id = Column("id",Integer,primary_key=True,autoincrement=True)
    user = Column("user",String)
    password = Column("password",String)

    chatrooms = relationship("ChatRoomModel", secondary=ChatRoomUser, back_populates="users")
    messages = relationship("MessageModel", back_populates="user_obj")

    def __init__(self,user,password):
        self.user = user
        self.password = password