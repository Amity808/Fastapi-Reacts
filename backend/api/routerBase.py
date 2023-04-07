from fastapi import APIRouter
from api.router import router_blog

api_router = APIRouter()

api_router.include_router(router_blog.router, prefix='/blog', tags=['user'])
