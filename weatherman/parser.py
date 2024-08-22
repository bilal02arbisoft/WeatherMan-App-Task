import glob
import os
from typing import Dict, List, Set

from weatherman.utils import extract_year, is_valid_path


class ParseWeatherFiles:
    """
    Parses weather data files from a specified directory.
    """
    def __init__(self, directory_path: str):
        if is_valid_path(directory_path):

            self.weather_dir_path = directory_path

        else:
            raise FileNotFoundError(f'The path {directory_path} does not exist. Try entering a valid path.')

    def find_weather_files(self) -> List[str]:
        """
        Finds all weather data files with a .txt extension in the specified weather directory.

        Returns:
            List[str]: A list of file paths for weather data files.
        """
        return glob.glob(os.path.join(self.weather_dir_path, '*.txt'))

    def load_single_weather_file(self, file_path: str) -> List[Dict[str, str]]:
        """
        Reads the weather file specified by `file_path` and parses its contents.

        Args:
            file_path (str): The path to the weather data file to be loaded.

        Returns:
            List[Dict[str, str]]: A list of parsed weather data entries.
        """
        weather_data = []
        with open(file_path, 'r') as file:
            weather_factors = [factor.strip()
                               for factor in file.readline().strip().split(',')]
            for line in file:
                weather_observations = line.strip().split(',')
                if len(weather_factors) == len(weather_observations):

                    weather_entry = {weather_factors[i]: weather_observations[i]
                                     for i in range(len(weather_observations))}
                    weather_data.append(weather_entry)

        return weather_data

    def parse_weather_files(self) -> List[Dict[str, str]]:
        """
        Parses weather data files by loading each file found in the weather directory.

        This method retrieves the list of weather data files from the `find_weather_files` method
        and processes each file by calling `load_single_weather_file` with the file path.

        Returns:
            List[Dict[str, str]]: A list of parsed weather data entries.
        """
        all_weather_data = []
        for path_of_single_file in self.find_weather_files():
            all_weather_data.extend(self.load_single_weather_file(path_of_single_file))

        return all_weather_data


class WeatherDataController:
    """
    Controller layer responsible for managing parsing and associated data used for reporting and logic.
    """
    def __init__(self, directory_path: str):
        try:
            self.parser = ParseWeatherFiles(directory_path)
            self.weather_data: List[Dict[str, str]] = []
        except FileNotFoundError as e:
            print(f"Error initializing WeatherDataController: {e}")

    def load_and_parse_data(self) -> None:
        """
        Loads and parses the weather data files.

        Returns:
            None
        """
        self.weather_data = self.parser.parse_weather_files()

    def extract_years_from_weather_data(self) -> Set[int]:
        """
        Extracts unique years from the 'PKT' field in the weather data.

        Returns:
            Set[int]: A set of unique years extracted from the 'PKT' field in the weather data.
        """
        return {extract_year(entry['PKT'])
                for entry in self.weather_data
                if 'PKT' in entry}

    def get_weather_data(self) -> List[Dict[str, str]]:
        """
        Returns the parsed weather data.

        Returns:
            List[Dict[str, str]]: A list of parsed weather data entries.
        """
        return self.weather_data
