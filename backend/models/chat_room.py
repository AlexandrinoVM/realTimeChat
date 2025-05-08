from sqlalchemy import  ForeignKey,Column,String,Integer,Boolean
from sqlalchemy.orm import relationship
from backend.database import Base
from models.schemas_model import ChatRoomUser

class ChatRoomModel(Base):
    __tablename__ = "chatroom"
    __table_args__ = {'extend_existing': True}
    id = Column("id",Integer, primary_key=True,autoincrement=True)
    name = Column("name",String)
    
    users = relationship("UserModel",secondary=ChatRoomUser,back_populates="chatrooms")
    message = relationship("MessageModel",back_populates="chatrooms")

    def __init__(self,name):
        self.name = name