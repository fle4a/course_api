import asyncio
from internal.repositories.db._redis import RedisReposory
from external.utils import CourseHandler, names



async def main():
    repo = RedisReposory()
    async with CourseHandler() as handler:
        while True:
            try:
                data, trx_price, rub_price, etx_price = await asyncio.gather(handler.get_price(),
                                                                            handler.get_trx_usdt_price(),
                                                                            handler.get_usd_rub_price(),
                                                                            handler.get_eth_usdt_price(),
                                                                            )
                tasks = []
                if data.get('status') is not None:
                    await asyncio.sleep(10)
                    print("BLOCKED")
                    continue
                for token, courses in data.items():
                    if token == "tron":
                        tasks.append(repo.set("USDTTRC"+"-USD", courses["usd"]/trx_price))
                        tasks.append(repo.set("USDTTRC"+ "-RUB", courses["usd"]/trx_price*rub_price))
                    elif token == "ethereum":
                        tasks.append(repo.set("USDTERC"+"-USD", courses["usd"]/etx_price))
                        tasks.append(repo.set("USDTERC"+"-RUB", courses["usd"]/etx_price*rub_price))
                        tasks.append(repo.set(names[token]+"-RUB", courses["rub"]))
                        tasks.append(repo.set(names[token]+"-USD", courses["usd"]))
                    elif token == "bitcoin":
                        tasks.append(repo.set(names[token]+"-RUB", courses["rub"]))
                        tasks.append(repo.set(names[token]+"-USD", courses["usd"]))
                await asyncio.gather(*tasks)
                print("UPDATE")
                await asyncio.sleep(5)
            except:
                continue

if __name__ == "__main__":
    asyncio.run(main())