from typing import Dict, List, Tuple, Union
from collections import defaultdict
from weatherman.utils import extract_year, extract_year_month
from weatherman.results import (YearlyExtremeWeatherResult,
                                MonthlyAveragesWeatherResult,
                                MonthlyExtremeBarChartResult)
import functools
import logging

MAX_TEMP = 'Max TemperatureC'
MIN_TEMP = 'Min TemperatureC'
MAX_HUMIDITY = 'Max Humidity'
MEAN_HUMIDITY = 'Mean Humidity'
NEGATIVE_INFINITY = float('-inf')
POSITIVE_INFINITY = float('inf')


class WeatherCalculations:
    """
    Performs calculations on parsed weather data.
    """
    def __init__(self, weather_recordings_data: List[Dict[str, str]]):
        self.weather_data = weather_recordings_data

    def error_handler(self, func):
        """
        Decorator to handle errors consistently.
        """
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:

                return func(*args, **kwargs)
            except (ValueError, TypeError) as e:
                logging.error(f'Error in {func.__name__}: {e}')

                return None

        return wrapper

    def compute_yearly_extreme_weather(self, year: str) -> Union[YearlyExtremeWeatherResult, None]:
        """
        Compute the yearly extreme weather statistics (max temp, min temp, max humidity).
        """
        return self._compute_extreme_weather_by_period(year, 'year')

    def compute_monthly_extreme_weather(self, month: str) -> Union[MonthlyExtremeBarChartResult, None]:
        """
        Compute the monthly extreme weather statistics (highest and lowest temperatures).
        """
        weather_data_by_month = self.filter_weather_data_by_month(month)
        days, highest_temp, lowest_temp = [], [], []
        for weather_entry in weather_data_by_month:
            days.append(weather_entry.get('PKT', ''))
            highest_temp.append(self._safe_float(weather_entry.get(MAX_TEMP, 0)) or 0)
            lowest_temp.append(self._safe_float(weather_entry.get(MIN_TEMP, 0)) or 0)

        return MonthlyExtremeBarChartResult(days, highest_temp, lowest_temp)

    def compute_monthly_averages_weather(self, month: str) -> Union[MonthlyAveragesWeatherResult, None]:
        """
        Compute the monthly average weather statistics (average max temp, min temp, mean humidity).
        """
        weather_data_filtered_by_month = self.filter_weather_data_by_month(month)
        sums, counts = defaultdict(float), defaultdict(int)

        for weather_entry in weather_data_filtered_by_month:
            for key in [MAX_TEMP, MIN_TEMP, MEAN_HUMIDITY]:
                value = self._extract_and_validate(weather_entry, key)
                if value is not None:

                    sums[key] += value
                    counts[key] += 1

        return MonthlyAveragesWeatherResult(
            self._calculate_average(sums[MAX_TEMP], counts[MAX_TEMP]),
            self._calculate_average(sums[MIN_TEMP], counts[MIN_TEMP]),
            self._calculate_average(sums[MEAN_HUMIDITY], counts[MEAN_HUMIDITY])
        )

    def _compute_extreme_weather_by_period(self, period: str, period_type: str) ->\
            Union[YearlyExtremeWeatherResult, None]:
        """
        Compute the extreme weather statistics for a given period (year or month).
        """
        data_filter = self.filter_weather_data_by_year if period_type == 'year' else self.filter_weather_data_by_month
        weather_data_filtered = data_filter(period)
        extreme_values = {
            MAX_TEMP: (max, NEGATIVE_INFINITY, ''),
            MIN_TEMP: (min, POSITIVE_INFINITY, ''),
            MAX_HUMIDITY: (max, NEGATIVE_INFINITY, ''),
        }

        for weather_entry in weather_data_filtered:
            for key, (operation, initial, _) in extreme_values.items():
                extreme_values[key] = self._update_extreme_tuple(
                    extreme_values[key],
                    self._extract_and_validate(weather_entry, key),
                    weather_entry['PKT'],
                    operation
                )

        return YearlyExtremeWeatherResult(
            extreme_values[MAX_TEMP][0],
            extreme_values[MAX_TEMP][1],
            extreme_values[MIN_TEMP][0],
            extreme_values[MIN_TEMP][1],
            extreme_values[MAX_HUMIDITY][0],
            extreme_values[MAX_HUMIDITY][1]
        )

    def _get_extreme_value(self, data: List[Dict[str, str]], key: str, func) -> Tuple[float, str]:
        """
        Utility function to get the extreme value (max/min) and corresponding day.
        """
        extreme_value, extreme_day = NEGATIVE_INFINITY if func == max else POSITIVE_INFINITY, ''
        for weather_entry in data:
            value = self._extract_and_validate(weather_entry, key)
            extreme_value, extreme_day = self._update_extreme_tuple(
                (extreme_value, extreme_day), value, weather_entry['PKT'], func
            )

        return extreme_value, extreme_day

    def _extract_and_validate(self, weather_entry: Dict[str, str], key: str) -> Union[float, None]:
        """
        Extract and validate the value for the given key from a weather entry.
        """

        return self._safe_float(weather_entry.get(key, '')) if key in weather_entry else None

    def _update_extreme_tuple(self, extreme_tuple: Tuple[float, str],
                              value: float, date: str, func) -> Tuple[float, str]:
        """
        Update the extreme value tuple based on the comparison function provided.
        """
        if value is not None and func(value, extreme_tuple[0]) == value:

            return value, date

        return extreme_tuple

    @error_handler
    def _safe_float(self, value: str) -> float:
        """
        Safely convert a string to a float.
        """
        return float(value)

    def filter_weather_data_by_year(self, date_year: str) -> List[Dict[str, str]]:
        """
        Filter weather data for a specific year.
        """
        filter_year = int(date_year)
        return [
            entry for entry in self.weather_data
            if extract_year(entry.get('PKT')) == filter_year
        ]

    def filter_weather_data_by_month(self, date_year_month: str) -> List[Dict[str, str]]:
        """
        Filter weather data for a specific month.
        """
        filter_year, filter_month = extract_year_month(date_year_month)
        filtered_data = [
            entry for entry in self.weather_data
            if extract_year_month(entry.get('PKT')) == (filter_year, filter_month)
        ]
        if not filtered_data:

            logging.error(f'Weather data related to {date_year_month} not found in records.')
            raise ValueError(f'Weather data related to {date_year_month} not found in records. '
                             f'Please enter a different date.')
        return filtered_data

    @staticmethod
    def _calculate_average(sum_value: float, count_value: int) -> Union[float, None]:
        """
        Calculate the average of a sum divided by a count.
        """
        return round(sum_value / count_value, 2) if count_value > 0 else None
