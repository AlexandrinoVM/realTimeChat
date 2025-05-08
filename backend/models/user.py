from backend.database import Base
from sqlalchemy import ForeignKey,Column,String,Integer,Boolean

class UserModel(Base):
    __tablename__ = "users"
    id = Column("id",Integer,primary_key=True,autoincrement=True)
    user = Column("user",String)
    password = Column("password",String)

    def __init__(self,user,password):
        self.user = user
        self.password = password