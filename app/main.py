from fastapi import FastAPI, HTTPException  
from app.services.weather import get_cached_weather
from app.models.weather import WeatherResponse  

app = FastAPI(title="Weather Microservice")  

@app.get("/weather/{city}", response_model=WeatherResponse)  
async def weather(city: str):  
    try:  
        data = await get_cached_weather(city)  
        return data  
    except Exception as e:  
        raise HTTPException(status_code=404, detail=str(e))