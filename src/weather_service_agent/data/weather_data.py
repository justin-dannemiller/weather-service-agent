from weather_service_agent.models.city_weather_record import CityWeatherRecord
from weather_service_agent.models.weather_conditions import WeatherCondition

WEATHER_DATA = {
    "palo alto": CityWeatherRecord(
        temperature = 22.8,
        conditions=[WeatherCondition.sunny, WeatherCondition.foggy],
        wind_speed=7.9
    ),
    "san francisco": CityWeatherRecord(
        temperature = 20.0,
        conditions=[WeatherCondition.sunny],
        wind_speed=6.2
    ),
    "london": CityWeatherRecord(
        temperature=12.0, 
        conditions=[WeatherCondition.rainy, WeatherCondition.cloudy],
        wind_speed=18.0
    ),
    "paris": CityWeatherRecord(
        temperature=15.7,
        conditions=[WeatherCondition.cloudy],
        wind_speed=12.4
    ),
    "new york": CityWeatherRecord(
        temperature=-0.8,
        conditions=[WeatherCondition.snowy, WeatherCondition.cloudy],
        wind_speed=8.6,
    )
}