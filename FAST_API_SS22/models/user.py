from database import Base
from sqlalchemy import Column , Integer , String


class UserModel(Base):
    __tablename__ = "user_table"
    id = Column(Integer , primary_key=True , index=True)
    username = Column(String(100) , nullable=True, unique=True )
    hash_password = Column(String(255), nullable=False ,)