from sqlalchemy import Column, Integer, String, ForeignKey, BIGINT
from database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)


class Message(Base):
    __tablename__ = "messages"
    id = Column(BIGINT, primary_key=True, index=True)
    content = Column(String)
    sender_id = Column(Integer)
