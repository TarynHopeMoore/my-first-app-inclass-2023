# this is the "web_app/routes/weather_routes.py" file...

from flask import Blueprint, request, render_template, redirect, flash

from app.weather import location_information, display_forecast, get_forecast

weather_routes = Blueprint("weather_routes", __name__)


@weather_routes.route("/weather/form")
def stocks_form():
    print("WEATHER FORM...")
    return render_template("weather_form.html")

@weather_routes.route("/weather/dashboard", methods=["GET", "POST"])
def weather_dashboard():
    print("WEATHER REPORT")

    if request.method == "POST":
        request_data_weather = dict(request.form)
        print("FORM DATA:", request_data_weather)
    else:
        request_data_weather = dict(request.args)
        print("URL PARAMS:", request_data_weather)

    zip_code = request_data_weather.get("zip_code") or "20057"

    try:
        test = display_forecast(zip_code=zip_code)
        geo = dict(location_information(zip_code=zip_code))
        data = get_forecast(zip_code=zip_code)

        flash("Fetched Latest Weather Data!", "success")
        return render_template("weather_dashboard.html",
            data=data[1])

    except Exception as err:
        print('OOPS', err)

        flash("Zip Code Error. Please check your zip code and try again!", "danger")
        return redirect("/weather/form")

