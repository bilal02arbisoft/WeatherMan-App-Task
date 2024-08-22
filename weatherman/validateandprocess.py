from typing import Callable, Set

from weatherman.utils import extract_year, is_valid_year, is_valid_year_month


class ValidateProcessWeather:
    """
    Validates user inputs and processes weather data based on it.
    """
    def __init__(self, weather_years: Set[int]):
        self.weather_existing_years = weather_years

    def is_year_in_existing_years(self, date_year: int) -> bool:
        """
        Checks if the year is in the existing weather years.
        """
        return date_year in self.weather_existing_years

    def validate_and_process(self, date: str, is_valid_date: Callable[[str], bool],
                             compute_weather: Callable, generate_weather_report: Callable,
                             date_type: str) -> str:
        """
        Validates the date, processes weather data, and generates a report.
        Args:
            date (str): The date string (YYYY or YYYY-MM) to validate and process.
            is_valid_date (Callable[[str], bool]): Function to validate the date format.
            compute_weather (Callable): Function to compute weather statistics.
            generate_weather_report (Callable): Function to generate weather report.
            date_type (str): Type of date, either 'year' or 'month'.
        """
        if is_valid_date(date):
            year = extract_year(date) if date_type == 'month' else int(date)
            if self.is_year_in_existing_years(year):
                results = compute_weather(date)
                return generate_weather_report(results)

            raise ValueError(f'Input {year} does not exist in records. '
                             f'Please enter a year in range: {self.weather_existing_years}')

        expected_format = 'YYYY-MM' if date_type == 'month' else 'YYYY'
        raise ValueError(f'Invalid {date_type} format {date}. Please use format {expected_format}.')

    def monthly_weather(self, date_year_month: str, compute_weather: Callable,
                        generate_weather_report: Callable) -> str:
        """
        Processes monthly weather data and generates a formatted report.
        Args:
            date_year_month (str): Year and month (YYYY-MM) for which to process weather data.
            compute_weather (Callable): Function to compute weather statistics.
            generate_weather_report (Callable): Function to generate weather report.
        """
        return self.validate_and_process(date_year_month, is_valid_year_month,
                                         compute_weather, generate_weather_report,
                                         'month')

    def yearly_weather(self, date_year: str, compute_weather: Callable,
                       generate_weather_report: Callable) -> str:
        """
        Processes yearly weather data and generates a formatted report.
        Args:
            date_year (str): Year for which to process weather data.
            compute_weather (Callable): Function to compute weather statistics.
            generate_weather_report (Callable): Function to generate weather report.
        """
        return self.validate_and_process(date_year, is_valid_year, compute_weather,
                                         generate_weather_report, 'year')
