from fastapi import Depends
from typing import Annotated
from internal.api.v1.schemas.request.exchange import CourseRequest
from internal.services.exchange import ExchangeService
from internal.repositories.db._redis import RedisReposory
repo = RedisReposory()
exchangeDependency = Annotated[CourseRequest, Depends(CourseRequest)]
def serv():
    return ExchangeService(repo)

exchangeServiceDependency = Annotated[ExchangeService, Depends(serv)]


    