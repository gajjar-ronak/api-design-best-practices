from sqlalchemy import Column, Integer, String
from app.core.database import Base


# PostgreSQL User Model
class UserSQL(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)


# MongoDB User Model
class UserMongo:
    def __init__(self, user_id, name, email):
        self.user_id = user_id
        self.name = name
        self.email = email