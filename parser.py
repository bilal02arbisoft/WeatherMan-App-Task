import os
import glob
from typing import Dict, List, Set
from utils import is_valid_path, extract_year


class ParseWeatherFiles:

    """Parses weather data files from a specified directory."""
    def __init__(self, directory_path: str):

        if is_valid_path(directory_path):

            self.weather_dir_path = directory_path
            self.weather_data: list[Dict[str, str]] = []

        else:

            raise FileNotFoundError(f'The path {directory_path} does not exist. '
                                    f'Try Entering the valid path')

    def find_weather_files(self) -> List[str]:

        weather_files_path = glob.glob(os.path.join(self.weather_dir_path, '*.txt'))

        return weather_files_path

    def parse_weather_files(self) -> None:

        for path_of_single_file in self.find_weather_files():
            self.load_single_weather_file(path_of_single_file)

    def load_single_weather_file(self, file_path) -> None:

        with (open(file_path, 'r') as file):

            weather_factors = [factor.strip() for factor in file.readline().strip().split(',')]

            for line in file:
                weather_observations = line.strip().split(',')

                if len(weather_factors) == len(weather_observations):

                    weather_entry = {weather_factors[i]: weather_observations[i]
                                     for i in range(len(weather_observations))}

                    self.weather_data.append(weather_entry)

    def extract_years_from_weather_data(self) -> Set[int]:

        set_of_years: {int} = {extract_year(weather_entry.get('PKT'))
                               for weather_entry in self.weather_data
                               if weather_entry.get('PKT')}

        return set_of_years

