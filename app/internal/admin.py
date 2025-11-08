from fastapi import APIRouter

router = APIRouter(prefix="/admin", tags=["admin"])

@router.get("/dashboard")
async def get_admin_dashboard():
    return {"message": "Welcome to the Admin Dashboard"}    