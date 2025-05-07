from sqlalchemy import  ForeignKey,Column,String,Integer,Boolean
from backend.database import Base


class ChatRoom(Base):
    __tablename__ = "chatrooms"
    id = Column("id",Integer, primary_key=True,autoincrement=True)
    name = Column("name",String)
    users = Column("users", ForeignKey("users.id"))
    messages = Column("messages",ForeignKey("messages.content"))

    def __init__(self,name):
        self.name = name