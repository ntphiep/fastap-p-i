from fastapi import APIRouter, Depends, HTTPException   


from app.schemas.user import UserCreate, UserUpdate
from app.services.user_service import UserService

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/", response_model=UserCreate)
def create_user(user: UserCreate, user_service: UserService = Depends()):
    return user_service.create_user(username=user.username, email=user.email)