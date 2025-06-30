Weather Microservice 🌤️
    REST API for fetching weather data using FastAPI, Docker, and OpenWeatherMap.

Description:
    A microservice that provides weather data for any city via the OpenWeatherMap API.
    Caching of weather data in Redis to reduce external API load.
    Automated documentation via Swagger UI.
    Containerized with Docker and Docker Compose.

Technologies:
    FastAPI — For building the REST API.
    OpenWeatherMap — Source of weather data.
    Redis — Caching layer.
    Docker — Environment isolation.
    Pydantic — Data validation.

---

Installation & Setup

1. Clone the Repository
```bash
git clone https://github.com/Mirolybik/weather-microservice.git   
cd weather-microservice
```
2. Create .env File
```bash
cp .env.example .env
```
Add your OpenWeatherMap API key:
```env
OPENWEATHERMAP_API_KEY=your_api_key_here  
REDIS_URL=redis://redis:6379/0
```
3. Install Dependencies
```bash
pip install -r requirements.txt 
```
4. Run the Microservice
```bash
docker-compose up -d
```

---

API Usage:
    Access Documentation
    🔗 http://localhost:8000/docs

Get Weather for a City
```bash
curl -X GET "http://localhost:8000/weather/Detroit"
```

Response:
```json
{
  "name": "Detroit",
  "weather": [{"main": "Clear", "description": "clear sky", "icon": "01d"}],
  "main": {
    "temp": 22.5,
    "feels_like": 21.8,
    "temp_min": 20.0,
    "temp_max": 25.0,
    "pressure": 1013,
    "humidity": 60
  }
}
```

Error: City Not Found
```bash
curl -X GET "http://localhost:8000/weather/InvalidCityName123"  
```
Response:
```json
{"detail": "City not found or API error"}  
```
