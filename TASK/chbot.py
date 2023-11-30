#CHATBOT WITH RULE-BASED RESPONSES
def chatbot():
    while True:
        user_input = input("Enter your message: ")

        # Greeting
        if user_input.lower() in ["hi", "hello", "good morning"]:
            print("Hello there! How can I help you today?")

        # Help
        elif user_input.lower() in ["help", "commands"]:
            print("Available commands:")
            print("- greet: Greet the chatbot")
            print("- help: Display available commands")
            print("- time: Get the current time")
            print("- weather: Get the current weather")

        # Time
        elif user_input.lower() == "time":
            import time
            current_time = time.strftime("%H:%M:%S")
            print("The current time is", current_time)

        # Weather
        elif user_input.lower() == "weather":
            import requests

            # Replace with your OpenWeatherMap API key
            api_key = "b073f167b994eb3755a3e9f16166ce58"
            city = "chennai"

            weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}")
            weather_json = weather_data.json()

            print(weather_json)  # Print the entire response from the API

            if "weather" in weather_json:
                description = weather_json["weather"][0]["description"]
                temperature = weather_json["main"]["temp"] - 273.15
                print(f"The weather in {city} is {description} with a temperature of {temperature:.2f} degrees Celsius.")
            else:
                print("Error fetching weather data.")

        # Default response
        else:
            print("Sorry, I didn't understand your request. Please try again.")

if __name__ == "__main__":
    chatbot()
