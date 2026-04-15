from fastapi import APIRouter
from datetime import datetime, timezone
from src.config import settings

router = APIRouter(
    prefix="/system",
    tags=["System"]
)

@router.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "project": settings.PROJECT_NAME,
        "version": settings.VERSION,
        "timestamp": datetime.now(timezone.utc).isoformat()
    }

@router.get("/info")
async def system_info():
    return {
        "project_name": settings.PROJECT_NAME,
        "version": settings.VERSION,
        "debug_mode": settings.DEBUG,
        "description": "UniMarket - платформа для студенческой торговли",
        "documentation": "/docs",
        "endpoints": {
            "health": f"{router.prefix}/health",
            "info": f"{router.prefix}/info"
        }
    }
