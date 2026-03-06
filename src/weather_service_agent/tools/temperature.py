from langchain_core.tools import tool

from weather_service_agent.models.temperature import TemperatureInput, TemperatureOutput
from weather_service_agent.core.exceptions import ToolExecutionError
from weather_service_agent.data.weather_data import WEATHER_DATA

@tool(args_schema=TemperatureInput)
def temperature(city: str) -> TemperatureOutput:
    """
    Description: Gets the temperature in Celsius for a given city

    This tool can be user saks for temperature of a specific city

    Example: 
        User query: 'What is the temperature in Moscow?'
    """
    city_name = city.lower()
    if city_name not in WEATHER_DATA:
        raise ToolExecutionError(
            code="city_not_found",
            message=f"No weather data available for city '{city}'. Temperature could not be retrieved"
        )

    weather_data = WEATHER_DATA[city_name]
    return TemperatureOutput(temperature=weather_data.temperature)