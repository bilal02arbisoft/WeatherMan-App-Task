# Weatherman-App-TASK

## Introduction
Weatherman-App-TASK is a comprehensive weather data analysis tool designed to parse, process, and generate insightful reports from weather data files. The application supports various types of reports, including monthly, yearly, and graphical representations like bar charts.

## Features
- Display highest temperature and day for a given year.
- Display lowest temperature and day for a given year.
- Display most humid day and humidity for a given year.
- Display average highest temperature for a given month.
- Display average lowest temperature for a given month.
- Display average mean humidity for a given month.
- Generate horizontal bar charts for highest and lowest temperatures for a given month.
- Support for multiple reports in a single command.

## Directory Structure

The application is organized as follows:

```bash
Weatherman-App-TASK/
├── weatherman/
│   ├── __init__.py              # Initialization script
│   ├── parser.py                # Module for parsing data
│   ├── utility.py               # Utility functions
│   ├── calculations.py          # Weather data calculations
│   ├── results.py               # Handles output results
│   ├── reports.py               # Report generation module
│   ├── validateandprocess.py    # Data validation and processing
│   ├── commandlineinterface.py  # CLI for user interaction
├── main.py                      # Main application script
├── README.md                    # Documentation file
├── .gitignore                   # Specifies intentionally untracked files to ignore
````

## Dependencies

- Python 3.12.3

## Pre-requisites

- Python 3.12.3 must be installed on your system.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/bilal02arbisoft/Weatherman-App-TASK.git
    ```
2. Navigate to the project directory:
    ```bash
    cd Weatherman-App-TASK
    ```
## Detailed Usage

To run the application, use the `main.py` file. Below are some example usages.

### Generate Yearly Extreme Report
For a given year, display the highest temperature and day, lowest temperature and day, most humid day, and humidity.
```sh
python3 main.py /path/to/files-dir -e 2004
```
### Generate Monthly Average Report
For a given month, display the average highest temperature, average lowest temperature, and average mean humidity.
```sh
python3 main.py /path/to/files-dir -a 2005/6
```
### Generate Monthly Bar Chart Report
For a given month, draw two horizontal bar charts on the console for the highest and lowest temperature on each day. Highest in red and lowest in blue.
```sh
python3 main.py /path/to/files-dir -c 2011/03
```
### Generate Multiple Reports
Generate all types of reports for a given month
```sh
python3 main.py /path/to/files-dir -c 2011/03 -a 2011/3 -e 2011

````


