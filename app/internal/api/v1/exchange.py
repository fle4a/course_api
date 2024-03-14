from fastapi import APIRouter
from internal.dependencies.exchange import exchangeDependency, exchangeServiceDependency
from internal.api.v1.schemas.response.exchange import CourseResponse


EXCHANGE_ROUTER = APIRouter()

@EXCHANGE_ROUTER.get("/courses")
async def get_course(
    request: exchangeDependency,
    service: exchangeServiceDependency,
) -> CourseResponse:
    data = await service.get_course(request.symbols)
    return CourseResponse(
        exchanger="COINGECKO",
        courses=data
    )
    