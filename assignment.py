import requests
from datetime import datetime
API_URL = "https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22"

def get_weather_data():
    response = requests.get(API_URL)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error retrieving weather data.")
        return None

def get_weather_by_date(weather_data, date_input):
    for forecast in weather_data['list']:
        if date_input in forecast['dt_txt'][:10]:
            return forecast['main']['temp']
    return None

def get_wind_speed_by_date(weather_data, date_input):
    for forecast in weather_data['list']:
        if date_input in forecast['dt_txt'][:10]:
            return forecast['wind']['speed']
    return None

def get_pressure_by_date(weather_data, date_input):
    for forecast in weather_data['list']:
        if date_input in forecast['dt_txt'][:10]:
            return forecast['main']['pressure']
    return None

def main():
    weather_data = get_weather_data()
    if not weather_data:
        return

    while True:
        print("\n1. Get weather\n2. Get Wind Speed\n3. Get Pressure\n0. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 0:
            print("Exiting the program.")
            break
        elif choice == 1:
            date_input = input("Enter the date (yyyy-mm-dd): ")
            try:
                date_input = datetime.strptime(date_input, "%Y-%m-%d")
            except ValueError:
                print("Invalid date format. Please use the format (yyyy-mm-dd).")
                continue
            temperature = get_weather_by_date(weather_data, date_input.strftime("%Y-%m-%d"))
            if temperature is not None:
                print(f"Temperature on {date_input}: {temperature} °C")
            else:
                print("No data available for the given date.")
        elif choice == 2:
            date_input = input("Enter the date (yyyy-mm-dd): ")
            try:
                date_input = datetime.strptime(date_input, "%Y-%m-%d")
            except ValueError:
                print("Invalid date format. Please use the format (yyyy-mm-dd).")
                continue
            wind_speed = get_wind_speed_by_date(weather_data, date_input.strftime("%Y-%m-%d"))
            if wind_speed is not None:
                print(f"Wind Speed on {date_input}: {wind_speed} m/s")
            else:
                print("No data available for the given date.")
        elif choice == 3:
            date_input = input("Enter the date (yyyy-mm-dd): ")
            try:
                date_input = datetime.strptime(date_input, "%Y-%m-%d")
            except ValueError:
                print("Invalid date format. Please use the format (yyyy-mm-dd).")
                continue
            pressure = get_pressure_by_date(weather_data, date_input.strftime("%Y-%m-%d"))
            print(date_input.strftime("%Y-%m-%d"))
            if pressure is not None:
                print(f"Pressure on {date_input}: {pressure} hPa")
            else:
                print("No data available for the given date.")
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
