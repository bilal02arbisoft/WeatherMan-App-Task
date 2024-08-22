import argparse
import functools

from weatherman.calculations import WeatherCalculations
from weatherman.parser import WeatherDataController
from weatherman.reports import WeatherReportsGenerate
from weatherman.validateandprocess import ValidateProcessWeather


def try_handler(func):
    """
    Decorator to handle exceptions in a uniform way.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:

            return func(*args, **kwargs)
        except ValueError as e:

            return f'An error occurred: {e}'
        except Exception as e:

            return f'An unexpected error occurred: {e}'

    return wrapper


class WeatherApp:
    def __init__(self, directory: str):
        self.weather_controller = WeatherDataController(directory)
        self.weather_controller.load_and_parse_data()
        self.weather_cal = WeatherCalculations(self.weather_controller.get_weather_data())
        self.process_weather = ValidateProcessWeather(self.weather_controller.extract_years_from_weather_data())

    @try_handler
    def process_yearly_weather(self, input_year: str) -> str:
        report = self.process_weather.yearly_weather(
            input_year,
            self.weather_cal.compute_yearly_extreme_weather,
            WeatherReportsGenerate.report_on_yearly_extreme
        )

        return report

    @try_handler
    def process_monthly_averages_weather(self, input_year_month: str) -> str:
        report = self.process_weather.monthly_weather(
            input_year_month,
            self.weather_cal.compute_monthly_averages_weather,
            WeatherReportsGenerate.report_on_monthly_average
        )

        return report

    @try_handler
    def process_monthly_extreme_weather(self, input_year_month: str) -> str:
        report = self.process_weather.monthly_weather(
            input_year_month,
            self.weather_cal.compute_monthly_extreme_weather,
            WeatherReportsGenerate.report_on_monthly_extreme_bar_chart
        )

        return report

    def run(self, args):
        if args.e:
            print(self.process_yearly_weather(args.e))
        if args.a:
            print(self.process_monthly_averages_weather(args.a))
        if args.c:
            print(self.process_monthly_extreme_weather(args.c))


def start_weatherman_app() -> None:
    parser = argparse.ArgumentParser('Weather data Processor Application')
    parser.add_argument('directory', type=str, help='Path to weather data files directory')
    parser.add_argument('-e', type=str, help='Year to display extremes (format: YYYY)')
    parser.add_argument('-a', type=str, help='Month to display averages (format: YYYY-MM)')
    parser.add_argument('-c', type=str, help='Month to display bar chart (format: YYYY-MM)')
    args = parser.parse_args()

    app = WeatherApp(args.directory)
    app.run(args)
