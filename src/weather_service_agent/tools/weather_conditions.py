from weather_service_agent.models.weather_conditions import WeatherConditionsInput, WeatherConditionsOutput
from weather_service_agent.core.exceptions import ToolExecutionError
from weather_service_agent.data.weather_data import WEATHER_DATA


def weather_conditions(city: str) -> WeatherConditionsOutput:
    """
    Description: Gets the weather conditions for a given city
    
    This tool should be used when the user's query requires information about the 
    weather conditions of a given city.

    Examples:
        User query: 'Is it raining in Moscow?'
        User query: 'What are the weather conditions in Athens'
    """
    city_name = city.strip().lower()
    if city_name not in WEATHER_DATA:
        raise ToolExecutionError(
            code="city_not_found",
            message=f"No weather data available for city '{city}'. "
        )
    record = WEATHER_DATA[city_name]
    return WeatherConditionsOutput(
        weather_conditions=record.conditions,
        wind_speed=record.wind_speed
    )
    