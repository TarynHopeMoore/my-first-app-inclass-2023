from app.weather import display_forecast
from app.weather import location_information

def test_display_forecast():
    zip_code = "20057"
    assert display_forecast(zip_code, country_code="US") == 200

def test_location_information():
    zip_code = "20057"
    assert location_information() == "<class 'pandas.core.series.Series'>"

