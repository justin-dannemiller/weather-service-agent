from pydantic import BaseModel, Field

class TemperatureInput(BaseModel):
    city: str = Field(..., description="The city to retrieve the temperature for")

class TemperatureOutput(BaseModel):
    temperature: float = Field(..., description="The temperature of the city in Fahrenheit")

