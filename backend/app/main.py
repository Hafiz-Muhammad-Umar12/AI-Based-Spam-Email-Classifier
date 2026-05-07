from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1.endpoints import upload, train, predict, analytics
from app.core.config import settings
from app.models.schemas import HealthCheck

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    debug=settings.DEBUG
)

# Set all CORS enabled origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify actual origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Health Check
@app.get("/health", response_model=HealthCheck, tags=["Health"])
async def health_check():
    return {"status": "healthy", "version": "1.0.0"}

# Include Routers
app.include_router(upload.router, prefix=settings.API_V1_STR, tags=["Upload"])
app.include_router(train.router, prefix=settings.API_V1_STR, tags=["Train"])
app.include_router(predict.router, prefix=settings.API_V1_STR, tags=["Predict"])
app.include_router(analytics.router, prefix=settings.API_V1_STR, tags=["Analytics"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
