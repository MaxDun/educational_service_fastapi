from fastapi import FastAPI
import uvicorn
from fastapi.routing import APIRouter

from api.handlers import user_router
# BLOCK WITH API ROUTES

app = FastAPI(title="education_service")


main_api_router = APIRouter()

main_api_router.include_router(user_router, prefix="/user", tags=["user"])
app.include_router(main_api_router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
