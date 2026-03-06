## Tools
1) weather_temperature
    - Gets the temperature in Fahrenheit for a given city\n
    - Args:
         - city (str)
    - Returns:
        - temperature (float)
2) weather_conditions
    - Gets the weather conditions for a given city
    - Args: 
        - city (str)
    - Returns:
        - conditions(list[str]): List of descriptive weather conditions (e.g., "rainy", "cloudy", "sunny")
        - wind_speed (float):  Speed of wind in kph
3) weather_advice
    - Gives advice on what to wear and bring given the weather conditions
    - Args:
        - temperature (float): Temperature in Celsius
        - conditions (list[str]): List of weather conditions impacting the city (e.g., ['rainy', 'cloudy'])
        - wind_speed (float): Speed of wind in in kph
