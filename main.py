"""
WeatherMan App

This system is designed to parse weather data files, perform various calculations,
and generate different types of reports based on user input.

General To-Do List:
1. Define Data Structures:
   - Create a data structure for holding each weather reading.
   - Create a data structure for holding the results of calculations.

2. Define Classes:
   - WeatherDataParser: For parsing the files and populating the readings data structure with correct data types.
   - WeatherCalculator: For computing the calculations given the readings data structure.
   - WeatherReporter: For creating the reports given the results data structure.

3. Main Function:
   - Assemble the above components.
   - Parse command-line arguments to determine which reports to generate.
   - Load and parse weather data files.
   - Perform calculations.
   - Generate and display the requested reports.
"""