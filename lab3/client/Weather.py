import random


class Weather:
    def __init__(self):
        self._current_weather = {}

    def get_weather(self, city: str):
        weather = self._current_weather.get(city, "sun")
        print(f"Weather in {city} is {weather}")
        return weather

    def update_random_weather(self, city: str):
        weather_list = ["sun", "snow", "rain"]
        chosen_weather = random.choice(weather_list)
        self._current_weather[city] = chosen_weather
        print(f"Weather updated for {city}: {chosen_weather}")
        return chosen_weather
