#IMPORTS
import pgeocode
import requests
import json

from pgeocode import Nominatim
from IPython.display import Image, display


ZIP_CODE = "20057"
COUNTRY_CODE = "US"
DEGREE_SIGN = u"\N{DEGREE SIGN}"

#FUNCTIONS

def location_information(zip_code = ZIP_CODE, country_code = COUNTRY_CODE):
    nomi = Nominatim(country_code)
    geo = nomi.query_postal_code(zip_code)

    return geo

def display_forecast(zip_code = ZIP_CODE, country_code= COUNTRY_CODE):
    """
    Displays a seven day weather forecast for the provided zip code.

    Params :

        country_code (str) a valid country code (see supported country codes list). Default is "US".

        zip_code (str) a valid US zip code, like "20057" or "06510".

    """

    geo = location_information(zip_code, country_code)
    latitude = geo["latitude"]
    longitude = geo["longitude"]

    request_url = f"https://api.weather.gov/points/{latitude},{longitude}"
    response = requests.get(request_url)
    parsed_response = json.loads(response.text)

    forecast_url = parsed_response["properties"]["forecast"]
    forecast_response = requests.get(forecast_url)
    parsed_forecast_response = json.loads(forecast_response.text)

    periods = parsed_forecast_response["properties"]["periods"]
    daytime_periods = [period for period in periods if period["isDaytime"] == True]

    for period in daytime_periods:
        #print(period.keys())
        print("-------------")
        print(period["name"], period["startTime"][0:7])
        print(period["shortForecast"], f"{period['temperature']} {DEGREE_SIGN}{period['temperatureUnit']}")
        #print(period["detailedForecast"])
        display(Image(url=period["icon"]))
    
    return forecast_response.status_code

if __name__ == "__main__":
    zip_code = input("Please input a zip code (e.g. '06510'): ") or "06510"
    print("ZIP CODE:", zip_code)

    print("LOCATION INFO:")
    print(location_information(zip_code))

    print("FORECAST:")
    display_forecast(zip_code)
