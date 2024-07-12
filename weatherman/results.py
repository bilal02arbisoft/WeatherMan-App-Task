from typing import List


class YearlyExtremeWeatherResult:
    """
    Data Structure Representing yearly extreme weather statistics.
    """
    def __init__(self, max_temp: float, max_temp_day: str,
                 min_temp: float, min_temp_day: str,
                 max_humid: float, max_humid_day: str):

        self.max_temp = max_temp
        self.max_temp_day = max_temp_day
        self.min_temp = min_temp
        self.min_temp_day = min_temp_day
        self.max_humid = max_humid
        self.max_humid_day = max_humid_day

    def __repr__(self) -> str:

        return (f'Highest Temperature: {self.max_temp}C on {self.max_temp_day}\n'
                f'Lowest Temperature: {self.min_temp}C on {self.min_temp_day}\n'
                f'Max Humidity: {self.max_humid}% on {self.max_humid_day}\n')


class MonthlyAveragesWeatherResult:
    """
     Data Structure representing monthly average weather statistics.
    """
    def __init__(self, avg_highest_temp: float,
                 avg_lowest_temp: float,
                 avg_mean_humidity: float):

        self.avg_highest_temp = avg_highest_temp
        self.avg_lowest_temp = avg_lowest_temp
        self.avg_mean_humid = avg_mean_humidity

    def __repr__(self) -> str:

        return (f'Average Highest Temp: {self.avg_highest_temp}C \n'
                f'Average Lowest Temp: {self.avg_lowest_temp}C \n'
                f'Average Mean Humidity: {self.avg_mean_humid}% \n')


class MonthlyExtremeBarChartResult:
    """
     Data Structure Representing monthly extreme
     weather statistics for generating a bar chart.
    """
    def __init__(self, days: List[str], highest_temps: List[float],
                 lowest_temps: List[float]):

        self.days = days
        self.highest_temps = highest_temps
        self.lowest_temps = lowest_temps

    def __repr__(self) -> str:

        bar_chart_lines = []

        for day, high_temp, low_temp in zip(self.days, self.highest_temps, self.lowest_temps):
            high_bar = '+' * int(high_temp)
            low_bar = '+' * int(low_temp)
            line = f'\033[91m{high_bar} {high_temp}C {day}\033[0m   \033[94m{low_bar} {low_temp}C {day}\033[0m'
            bar_chart_lines.append(line)

        return '\n'.join(bar_chart_lines)
