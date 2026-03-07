from enum import Enum
from pydantic import BaseModel, Field

from weather_service_agent.models.weather_conditions import WeatherCondition

class WeatherAdviceInput(BaseModel):
    temperature: float = Field(..., description="The temperature of the city in Celsius")
    weather_conditions: list[WeatherCondition] = Field(
        ..., 
        description="List of weather conditions impacting the city (e.g., ['rainy', 'cloudy'])"
    )
    wind_speed: float = Field(..., description="Speed of wind in city")

class ClothingLevel(str, Enum):
    light = "light"
    layered = "layered"
    winter = "winter"

class RecommendedItem(str, Enum):
    umbrella = "umbrella"
    rain_jacket = "rain_jacket"
    sunglasses = "sunglasses"
    boots = "boots"
    scarf = "scarf"
    gloves = "gloves"

class WeatherAdviceOutput(BaseModel):
    clothing_level: ClothingLevel = Field(
        ..., 
        description="The level of clothing recommended (e.g., 'light', 'layered', or 'winter')"
    )
    recommended_items: list[RecommendedItem] = Field(
        default_factory=list,
        description="List of recommended items to bring (e.g., ['boots', 'scarf', 'gloves'])"
    )
    high_wind_warning: bool = Field(False, description="Whether the wind speeds are dangerously high.")