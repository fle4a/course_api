import asyncio

from internal.api.v1.schemas.response.exchange import CourseResponseItem

from internal.repositories.db._redis import RedisReposory
from internal.core.exceptions import ValidationError

class ExchangeService:
    def __init__(self, repo):
        self.repo = repo
    
    async def get_course(self, directions: str | None = None) -> list[CourseResponseItem]:
        tasks = []
        pairs = []
        result = []
        if directions is None:
            for pair, course in await self.repo.getall():
                result.append(CourseResponseItem(
                    direction=pair,
                    value=course,
                ))
            return result
        try:
            directions = directions.split(',')     
            for direction in directions:
                _from, _to = direction.split('to-')
                pair = _from+_to
                pairs.append(pair)
                tasks.append(self.repo.get(pair))
        
            for pair, course in zip(pairs, await asyncio.gather(*tasks)):
                result.append(CourseResponseItem(
                        direction=pair,
                        value=course,
                    ))
        except:
            raise ValidationError()
        return result
            
            