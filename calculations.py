from typing import Dict, Tuple, List
from collections import defaultdict
from parser import extract_year, extract_year_month
from results import YearlyExtremeWeatherResult, MonthlyAveragesWeatherResult, MonthlyExtremeBarChartResult


class WeatherCalculations:

    """Performs calculations on parsed weather data."""
    def __init__(self, weather_recordings_data: list[Dict[str, str]]):

        self.weather_data = weather_recordings_data

    def compute_yearly_extreme_weather(self, year: str) -> YearlyExtremeWeatherResult:

        weatherdata_filtered_by_year = self.filter_weather_data_by_year(year)

        max_temp_tuple: Tuple[float, str] = (float('-inf'), '')
        min_temp_tuple: Tuple[float, str] = (float('inf'), '')
        max_humid_tuple: Tuple[float, str] = (float('-inf'), '')

        for weather_entry in weatherdata_filtered_by_year:

            if weather_entry.get('Max TemperatureC'):

                try:
                    max_temp_value = float(weather_entry['Max TemperatureC'])
                    if max_temp_value > max_temp_tuple[0]:
                        max_temp_tuple = (max_temp_value, weather_entry['PKT'])

                except ValueError:
                    pass

            if weather_entry.get('Min TemperatureC'):

                try:
                    min_temp_value = float(weather_entry['Min TemperatureC'])
                    if min_temp_value < min_temp_tuple[0]:
                        min_temp_tuple = (min_temp_value, weather_entry['PKT'])

                except ValueError:
                    pass

            if weather_entry.get('Max Humidity'):

                try:
                    max_humid_value = float(weather_entry['Max Humidity'])
                    if max_humid_value > max_humid_tuple[0]:
                        max_humid_tuple = (max_humid_value, weather_entry['PKT'])

                except ValueError:
                    continue

        return YearlyExtremeWeatherResult(

            max_temp_tuple[0],
            max_temp_tuple[1],
            min_temp_tuple[0],
            min_temp_tuple[1],
            max_humid_tuple[0],
            max_humid_tuple[1]
        )

    def compute_monthly_averages_weather(self, month: str) -> MonthlyAveragesWeatherResult:

        weather_data_filtered_by_month = self.filter_weather_data_by_month(month)

        sums, counts = defaultdict(float), defaultdict(int)

        for weather_entry in weather_data_filtered_by_month:

            try:
                sums['highest'] += float(weather_entry.get('Max TemperatureC', 0))
                counts['highest'] += 1

            except ValueError:
                pass

            try:
                sums['lowest'] += float(weather_entry.get('Min TemperatureC', 0))
                counts['lowest'] += 1

            except ValueError:
                pass

            try:
                sums['mean_humid'] += float(weather_entry.get('Mean Humidity', 0))
                counts['mean_humid'] += 1

            except ValueError:
                continue

        avg_highest = sums['highest'] / counts['highest'] if counts['highest'] > 0 else None
        avg_lowest = sums['lowest'] / counts['lowest'] if counts['lowest'] > 0 else None
        avg_mean_humid = sums['mean_humid'] / counts['mean_humid'] if counts['mean_humid'] > 0 else None

        return MonthlyAveragesWeatherResult(

            round(avg_highest, 2),
            round(avg_lowest, 2),
            round(avg_mean_humid, 2)
        )

    def compute_monthly_extreme_weather(self, month: str) -> MonthlyExtremeBarChartResult:

        weather_data_by_month = self.filter_weather_data_by_month(month)

        highest_temp: List[float] = []
        lowest_temp: List[float] = []
        days: List[str] = []

        for weather_entry in weather_data_by_month:

            days.append(weather_entry.get('PKT', ''))

            try:
                highest_temp.append(float(weather_entry.get('Max TemperatureC', 0)))

            except (ValueError, TypeError):
                highest_temp.append(0)

            try:
                lowest_temp.append(float(weather_entry.get('Min TemperatureC', 0)))

            except (ValueError, TypeError):
                lowest_temp.append(0)

        return MonthlyExtremeBarChartResult(
            days,
            highest_temp,
            lowest_temp
        )

    def filter_weather_data_by_year(self, date_year: str) -> list[Dict[str, str]]:

        filtered_data: list[Dict[str, str]] = []
        filter_year = int(date_year)

        for weather_entry in self.weather_data:

            if weather_entry.get('PKT'):
                weather_entry_year = extract_year(weather_entry.get('PKT'))

                if filter_year == weather_entry_year:
                    filtered_data.append(weather_entry)

        return filtered_data

    def filter_weather_data_by_month(self, date_year_month: str) -> list[Dict[str, str]]:

        filtered_data: list[Dict[str, str]] = []

        for weather_entry in self.weather_data:

            if weather_entry.get('PKT'):
                weather_entry_year, weather_entry_month = extract_year_month(
                    weather_entry.get('PKT'))
                filter_year, filter_month = extract_year_month(date_year_month)

                if weather_entry_year == filter_year and weather_entry_month == filter_month:
                    filtered_data.append(weather_entry)

        if filtered_data:

            return filtered_data

        else:

            raise ValueError(f'Weather data related to {date_year_month} not found in records. '
                             f'Please Enter different date.')

