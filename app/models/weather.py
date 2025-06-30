from pydantic import BaseModel  
from typing import List, Dict  

class WeatherDescription(BaseModel):  
    main: str
    description: str  
    icon: str

class MainWeatherData(BaseModel):  
    temp: float  
    feels_like: float  
    temp_min: float  
    temp_max: float  
    pressure: int  
    humidity: int  

class WeatherResponse(BaseModel):  
    name: str
    weather: List[WeatherDescription]  
    main: MainWeatherData