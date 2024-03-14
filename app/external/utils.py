from httpx import AsyncClient

import config


names = {
    "bitcoin" : "BTC",
    "ethereum" : "ETH",
    "tron": "TRX"
}


class CourseHandler:
    async def __aenter__(self) -> "CourseHandler":
        self.conn = AsyncClient()
        return self
        
    async def get_price(self) -> dict[str, dict]:
        resp = await self.conn.get(config.COIN_GECKO_URL, params={
                "ids": ','.join(names.keys()),
                "vs_currencies": "usd,rub"
        })
        return resp.json()
            
    async def get_trx_usdt_price(self) -> float:
        resp = await self.conn.get(config.BINANCE_URL, params={"symbol":"TRXUSDT"})
        return float(resp.json()['price'])

    async def get_eth_usdt_price(self) -> float:
        resp = await self.conn.get(config.BINANCE_URL, params={"symbol":"ETHUSDT"})
        return float(resp.json()['price'])

    async def get_usd_rub_price(self) -> float:
        url = f'{config.USD_EXCHANGE_URL}/{config.API_KEY}/latest/USD'
        resp = await self.conn.get(url)
        return resp.json()['conversion_rates']['RUB']
        
    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        await self.conn.aclose()