from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.core.mongodb import get_mongo_db
from app.schemas.user import UserCreate, UserResponse
from app.services.user_service import (
    create_user_postgres, get_user_postgres,
    create_user_mongo, get_user_mongo
)

router = APIRouter()


@router.post("/", response_model=UserResponse)
async def create_user_api(user: UserCreate, db: Session = Depends(get_db), mongo_db=Depends(get_mongo_db)):
    # Use PostgreSQL
    user_data_postgres = create_user_postgres(db, user)

    # Use MongoDB
    user_data_mongo = await create_user_mongo(mongo_db, user)

    return {
        "user_id": user_data_postgres.user_id,
        "name": user_data_postgres.name,
        "email": user_data_postgres.email
    }


@router.get("/{user_id}", response_model=UserResponse)
async def get_user_api(user_id: int, db: Session = Depends(get_db), mongo_db=Depends(get_mongo_db)):
    # Fetch from PostgreSQL
    user_data_postgres = get_user_postgres(db, user_id)
    if not user_data_postgres:
        raise HTTPException(status_code=404, detail="User not found in PostgreSQL")

    # Fetch from MongoDB (if needed)
    user_data_mongo = await get_user_mongo(mongo_db, str(user_data_postgres.user_id))

    return {
        "user_id": user_data_postgres.user_id,
        "name": user_data_postgres.name,
        "email": user_data_postgres.email
    }