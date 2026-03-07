from weather_service_agent.models.weather_conditions import WeatherCondition
from weather_service_agent.models.weather_advice import (
    WeatherAdviceInput,
    WeatherAdviceOutput,
    ClothingLevel,
    RecommendedItem
)

RECOMMENDED_ITEM_MAP: dict[WeatherCondition, list[RecommendedItem]] = {
    WeatherCondition.sunny: [RecommendedItem.sunglasses],
    WeatherCondition.rainy: [RecommendedItem.umbrella, RecommendedItem.rain_jacket],
    WeatherCondition.snowy: [
        RecommendedItem.boots,
        RecommendedItem.gloves, 
        RecommendedItem.scarf
    ],
    WeatherCondition.foggy: [],
    WeatherCondition.cloudy: []
}
def weather_advice(
    temperature: float,
    weather_conditions: list[WeatherCondition],
    wind_speed: float
) -> WeatherAdviceOutput:
    """
    Description: 
        Generate recommendations on clothing and items to bring based on weather.
    
    When to use:
        Temperature and weather conditions have already been retrieved and user desires
        practical recommendations on clothing and items to bring.
    
    Inputs:
        temperature (float): The temperature of the city in Celsius.
        weather_conditions (list[WeatherCondition]): List of weather conditions impacting the city 
            (e.g., ['rainy', 'cloudy']).
        wind_speed (float): Speed of wind in kph.
    
    Returns:
        WeatherAdviceOutput: Data model containing recommended clothing level and items to bring.
    """
    recommended_items : list[RecommendedItem] = []
    for condition in weather_conditions:
        recommended_items.extend(RECOMMENDED_ITEM_MAP.get(condition, []))

    if temperature >= 16:
        clothing_level = ClothingLevel.light
    elif temperature >= 4 and temperature < 16:
        clothing_level = ClothingLevel.layered
    else:
        clothing_level = ClothingLevel.winter

    if wind_speed > 60.0:
        high_wind_warning = True
    return WeatherAdviceOutput(
        clothing_level=clothing_level,
        recommended_items=recommended_items,
        high_wind_warning=high_wind_warning
    )

    