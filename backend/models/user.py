from backend.database import Base
from sqlalchemy import ForeignKey,Column,String,Integer,Boolean

class User(Base):
    __tablename__ = "users"
    id = Column("id",Integer,primary_key=True,autoincrement=True)
    name = Column("name",String)
    user = Column("user",String)
    password = Column("password",String)

    def __init__(self,name,user,password):
        self.name = name
        self.user = user
        self.password = password