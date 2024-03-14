import asyncio

from redis.asyncio import Redis

import config


keys = ["ETH-RUB","ETH-USD",
    "USDTTRC-USD",
    "BTC-USD",
    "USDTERC-USD",
    "USDTTRC-RUB",
    "USDTERC-RUB",
    "BTC-RUB"]

class RedisReposory:
    def __init__(self):
        self.conn = Redis(host=config.REDIS_HOST,
                          port=config.REDIS_PORT,
                          db=config.REDIS_DB,
                          )
    async def get(self, pair: str):
        return await self.conn.get(pair)
    
    async def set(self, pair: str, value: int):
        return await self.conn.set(pair, value)
    async def getall(self) -> list[tuple[str, float]]:
        return zip(keys, await asyncio.gather(*[self.get(key) for key in keys]))