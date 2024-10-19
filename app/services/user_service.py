from sqlalchemy.orm import Session
from app.models.user import UserSQL, UserMongo
from app.schemas.user import UserCreate
from bson import ObjectId

# PostgreSQL User Service
def create_user_postgres(db: Session, user: UserCreate):
    db_user = UserSQL(name=user.name, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_postgres(db: Session, user_id: int):
    return db.query(UserSQL).filter(UserSQL.user_id == user_id).first()

# MongoDB User Service
async def create_user_mongo(db, user: UserCreate):
    user_id = ObjectId()
    user_data = UserMongo(user_id=user_id, name=user.name, email=user.email)
    await db.users.insert_one(user_data.__dict__)
    return user_data

async def get_user_mongo(db, user_id: str):
    return await db.users.find_one({"_id": ObjectId(user_id)})