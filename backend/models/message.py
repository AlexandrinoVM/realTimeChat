from backend.database import Base
from sqlalchemy import ForeignKey,String,Column,Integer,Boolean
from sqlalchemy.orm import relationship
class MessageModel(Base):
    __tablename__ = "messages"
    __table_args__ = {'extend_existing': True}
    id = Column("id",Integer,primary_key=True,autoincrement=True)
    room = Column("room", ForeignKey("chatroom.id"))
    user = Column("usuario",ForeignKey("users.id"))
    content = Column("content",String)

    room_obj = relationship("ChatRoomModel", back_populates="messages")
    user_obj = relationship("UserModel", back_populates="messages")

    #def __init__(self,content):
      #  self.content = content