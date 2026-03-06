from enum import Enum
from pydantic import BaseModel, Field

class WeatherConditionsInput(BaseModel):
    city: str = Field(..., description="The city to retrieved the weather conditions for")

class WeatherCondition(str, Enum):
    sunny = "sunny"
    cloudy = "cloudy"
    rainy = "rainy"
    snowy = "snowy"
    foggy = "foggy"

class WeatherConditionsOutput(BaseModel):
    weather_conditions: list[WeatherCondition] = Field(
        ...,
        description="List of weather conditions impacting the city (e.g., ['rainy', 'cloudy'])"
    )
    wind_speed: float = Field(..., description="Speed of wind in city in kph")
