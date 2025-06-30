import redis.asyncio as redis  
from app.config import settings  

class RedisCache:  
    def __init__(self):  
        self.redis = redis.Redis(host="redis", port=6379, db=0)  

    async def get_weather(self, city: str):  
        data = await self.redis.get(f"weather:{city}")  
        return eval(data) if data else None  

    async def set_weather(self, city: str, data: dict, ttl: int = 300):  
        await self.redis.setex(f"weather:{city}", ttl, str(data))  

cache = RedisCache()