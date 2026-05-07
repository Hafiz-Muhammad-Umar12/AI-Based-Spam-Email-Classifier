from fastapi import APIRouter
from app.services.analytics_service import analytics_service

router = APIRouter()

@router.get("/analytics")
async def get_system_analytics():
    """
    Get system-wide analytics, model performance, and AI insights.
    """
    return analytics_service.get_analytics()
