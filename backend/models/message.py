from backend.database import Base
from sqlalchemy import ForeignKey,String,Column,Integer,Boolean

class Message(Base):
    __tablename__ = "messages"
    id = Column("id",Integer,primary_key=True,autoincrement=True)
    room = Column("room", ForeignKey("chatrooms.id"))
    user = Column("usuario",ForeignKey("users.id"))
    content = Column("content",String)

    def __init__(self,content):
        self.content = content