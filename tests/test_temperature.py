import pytest

from weather_service_agent.core.exceptions import ToolExecutionError
from weather_service_agent.tools.temperature import temperature
from weather_service_agent.models.temperature import TemperatureOutput


def test_temperature_valid_city():
    """
    Test that the temperature tool returns the correct temperature for a valid city name.
    """
    valid_city = "palo alto"
    result = temperature(valid_city)
    assert isinstance(result, TemperatureOutput)
    assert result.temperature == 22.8

def test_temperature_valid_city_with_whitespace():
    """
    Test that the temperature tool returns the correct temperature for a city name
    with whitespace
    """
    valid_city = "  san francisco  "
    result = temperature(valid_city)
    assert isinstance(result, TemperatureOutput)
    assert result.temperature == 20.0

def test_temperature_invalid_city():
    """
    Test that the temperature tool raises an exception for an invalid city name.
    """
    invalid_city = "not a real city"
    with pytest.raises(ToolExecutionError) as exec_info:
        temperature(invalid_city)
    assert exec_info.value.code == "city_not_found"
    assert exec_info.value.message == f"No weather data available for city '{invalid_city}'. Temperature could not be retrieved."