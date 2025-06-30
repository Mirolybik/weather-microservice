import httpx  
from app.config import settings  
from app.models.weather import WeatherResponse  
from app.services.cache import cache  

async def get_weather_data(city: str) -> dict:  
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={settings.OPENWEATHERMAP_API_KEY}&units=metric"  
    async with httpx.AsyncClient() as client:  
        response = await client.get(url)  
        if response.status_code != 200:
            raise Exception("City not found or API error")  
        return response.json()  

async def get_cached_weather(city: str) -> dict:  
    cached = await cache.get_weather(city)
    if cached:  
        return cached  
    data = await get_weather_data(city)  
    await cache.set_weather(city, data)  
    return data