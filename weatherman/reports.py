from weatherman.results import MonthlyAveragesWeatherResult, MonthlyExtremeBarChartResult, YearlyExtremeWeatherResult


class WeatherReportsGenerate:
    """
    Generates formatted reports based on weather statistics.
    """
    @staticmethod
    def report_on_yearly_extreme(results: YearlyExtremeWeatherResult) -> str:

        return repr(results)

    @staticmethod
    def report_on_monthly_average(results: MonthlyAveragesWeatherResult) -> str:

        return repr(results)

    @staticmethod
    def report_on_monthly_extreme_bar_chart(results: MonthlyExtremeBarChartResult) -> str:

        return repr(results)
