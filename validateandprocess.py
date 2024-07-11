from typing import Set, Callable


class ValidateProcessWeather:

    """Validates user inputs and processes weather data based on it"""
    def __init__(self, weather_years: Set[int]):

        self.weather_existing_years = weather_years

    def year_found_in_existing_years(self, date_year) -> bool:

        return date_year in self.weather_existing_years

    def monthly_weather(self, date_year_month: str,
                        compute_weather: Callable,
                        generate_weather_report: Callable) -> str:
        """
        Processes monthly weather data and generates a formatted report.
        Args:
            date_year_month (str): Year and month (YYYY-MM) for which to process weather data.
            compute_weather (Callable): Function to compute weather statistics.
            generate_weather_report (Callable): Function to generate weather report.

        Returns:
            str: Formatted report on monthly weather statistics.
        """

        if (is_valid_year_month(date_year_month) and
           self.year_found_in_existing_years(extract_year(date_year_month))):

            result = compute_weather(date_year_month)
            report = generate_weather_report(result)

            return report

        elif not is_valid_year_month(date_year_month):

            raise ValueError(f'Invalid date format {date_year_month}. '
                             f'Please use format YYYY-MM ')

        elif not self.year_found_in_existing_years(extract_year(date_year_month)):

            raise ValueError(f'Input \'{extract_year(date_year_month)}\''
                             f' year mentioned in input {date_year_month} does not'
                             f' exist in records. Pls enter year in range: \n '
                             f'{self.weather_existing_years}')

    def yearly_weather(self, date_year: str,
                       compute_weather: Callable,
                       generate_weather_report: Callable) -> str:

        """
               Processes yearly weather data and generates a formatted report.

               Args:
                   date_year (str): Year for which to process weather data.
                   compute_weather (Callable): Function to compute weather statistics.
                   generate_weather_report (Callable): Function to generate weather report.

               Returns:
                   str: Formatted report on yearly weather statistics.
        """

        if (is_valid_year(date_year) and
           self.year_found_in_existing_years(int(date_year))):

            results = compute_weather(date_year)
            report = generate_weather_report(results)

            return report

        elif not is_valid_year(date_year):

            raise ValueError(f'Invalid year format: \'{date_year}\'.'
                             f' Please use format YYYY.')

        elif not self.year_found_in_existing_years(int(date_year)):

            raise ValueError(f'Input \'{date_year}\' year does not exists in records '
                             f'Please enter year in range: \n'
                             f'{self.weather_existing_years}')

