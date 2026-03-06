from pydantic import BaseModel, Field

from weather_service_agent.models.weather_conditions import WeatherCondition

class CityWeatherRecord(BaseModel):
    temperature: float = Field(..., description="Thre temperature of the city in Celsius")
    conditions: list[WeatherCondition] = Field(..., description="The weather conditions of the city")
    wind_speed: float = Field(..., description="The speed of the wind in the city in kph")
