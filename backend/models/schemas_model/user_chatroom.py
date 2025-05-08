from sqlalchemy import Column,ForeignKey,Table,Integer
from backend.database import Base

ChatRoomUser = Table(
    'chatroom_user',
    Base.metadata,
    Column('chatroom_id',Integer,ForeignKey('chatroom.id')),
    Column('user_id',Integer,ForeignKey('users.id'))
)