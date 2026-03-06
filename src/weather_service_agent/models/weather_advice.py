from pydantic import BaseModel, Field
from weather_service_agent.models.weather_conditions import WeatherCondition

class WeatherAdviceInput(BaseModel):
    temperature: float = Field(..., description="The temperature of the city in Fahrenheit")
    weather_conditions: list[WeatherCondition] = Field(
        ..., 
        description="List of weather conditions impacting the city (e.g., ['rainy', 'cloudy'])"
    )
    wind_speed: float = Field(..., description="Speed of wind in city")