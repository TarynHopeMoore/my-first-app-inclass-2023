from app.weather import display_forecast

def test_display_forecast():
    zip_code = "20057"
    assert display_forecast(zip_code, country_code="US") == 200

