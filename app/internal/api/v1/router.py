from fastapi import APIRouter
from internal.api.v1.exchange import EXCHANGE_ROUTER

V1_ROUTER = APIRouter(prefix='/v1')
V1_ROUTER.include_router(EXCHANGE_ROUTER)