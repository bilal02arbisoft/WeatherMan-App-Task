import argparse


def start_weatherman_app() -> None:
    parser = argparse.ArgumentParser('Weather data Processor Application')

    parser.add_argument('directory', type=str, help='Path to weather data files directory')
    parser.add_argument('-e', type=str, help='Year to display extremes (format: YYYY)')
    parser.add_argument('-a', type=str, help='Month to display averages (format: YYYY-MM)')
    parser.add_argument('-c', type=str, help='Month to display bar chart (format: YYYY-MM)')

    args = parser.parse_args()

    try:

        weather_parser = ParseWeatherFiles(args.directory)
        weather_parser.parse_weather_files()
        weather_cal = WeatherCalculations(weather_parser.weather_data)
        existing_years = weather_parser.extract_years_from_weather_data()
        process_weather = ValidateProcessWeather(existing_years)

        if args.e:

            try:
                input_year: str = args.e
                report = process_weather.yearly_weather(input_year,
                                                        weather_cal.compute_yearly_extreme_weather,
                                                        WeatherReportsGenerate.report_on_yearly_extreme)
                print(report)

            except ValueError as e:
                print(f'An error occurred : {e}')

        if args.a:

            try:
                input_year_month = args.a
                report = process_weather.monthly_weather(input_year_month,
                                                         weather_cal.compute_monthly_averages_weather,
                                                         WeatherReportsGenerate.report_on_monthly_average)
                print(report)

            except ValueError as e:
                print(f'An error occurred : {e}')

        if args.c:

            try:
                input_year_month = args.c
                report = process_weather.monthly_weather(input_year_month,
                                                         weather_cal.compute_monthly_extreme_weather,
                                                         WeatherReportsGenerate.report_on_monthly_extreme_bar_chart)
                print(report)

            except ValueError as e:
                print(f'An error occurred : {e}')

    except Exception as e:
        print(f'An error occurred : {e}')
