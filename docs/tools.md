## Tools
1) weather_temperature
    - Gets the temperature in Celsius for a given city\n
    - Args:
         - city (str): Name of city
    - Returns:
        - temperature (float): Temperature of city in Celsius
2) weather_conditions
    - Gets the weather conditions for a given city
    - Args: 
        - city (str): Name of city
    - Returns:
        - conditions(list[WinterCondition]): List of weather conditions impacting city (e.g., ["rainy", "cloudy"])
        - wind_speed (float):  Speed of wind in kph
3) weather_advice
    - Gives advice on what to wear and bring given the weather conditions
    - Args:
        - temperature (float): Temperature in Celsius
        - conditions (list[str]): List of weather conditions impacting the city (e.g., ['rainy', 'cloudy'])
        - wind_speed (float): Speed of wind in in kph
