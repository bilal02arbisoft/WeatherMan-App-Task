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
python3 main.py /path/to/files-dir -a 2005-06
```
### Generate Monthly Bar Chart Report
For a given month, draw two horizontal bar charts on the console for the highest and lowest temperature on each day. Highest in red and lowest in blue.
```sh
python3 main.py /path/to/files-dir -c 2011-03
```
### Generate Multiple Reports
Generate all types of reports for a given month
```sh
python3 main.py /path/to/files-dir -c 2011-03 -a 2011-3 -e 2011

````
## Sample Outputs

Yearly Extreme Report
```sh
Highest Temperature: 29.0C on 2004-6-4
Lowest Temperature: 0.0C on 2004-12-17
Max Humidity: 100.0% on 2004-12-16
```
Monthly Average Report
```sh
Average Highest Temp: 25.8C 
Average Lowest Temp: 20.88C 
Average Mean Humidity: 42.36%
```
Monthly Bar Chart Report
```sh
+++++ 5.0C 2011-3-1    0.0C 2011-3-1
++++ 4.0C 2011-3-2    0.0C 2011-3-2
++++++ 6.0C 2011-3-3    0.0C 2011-3-3
++++ 4.0C 2011-3-4    0.0C 2011-3-4
++++++ 6.0C 2011-3-5   +++ 3.0C 2011-3-5
+++++++++++++ 13.0C 2011-3-6   ++++ 4.0C 2011-3-6
++++++++++++ 12.0C 2011-3-7   ++++++ 6.0C 2011-3-7
+++++++++++++ 13.0C 2011-3-8   +++++ 5.0C 2011-3-8
+++++++++++++++ 15.0C 2011-3-9   ++++++ 6.0C 2011-3-9
+++++++++++++++ 15.0C 2011-3-10   ++++++ 6.0C 2011-3-10
++++++++++++++++ 16.0C 2011-3-11   ++++++++ 8.0C 2011-3-11
+++++++++++++++++ 17.0C 2011-3-12   ++++++++++ 10.0C 2011-3-12
++++++++++++++++++++++++++++++ 30.0C 2011-3-13   ++++++++++++ 12.0C 2011-3-13
+++++++++++++++++++++ 21.0C 2011-3-14   ++++++++++++++ 14.0C 2011-3-14
++++++++++++++++++++++ 22.0C 2011-3-15   ++++++++++++++++ 16.0C 2011-3-15
+++++++++++++++++++++ 21.0C 2011-3-16   +++++++++++++++ 15.0C 2011-3-16
++++++++++++++++++ 18.0C 2011-3-17   +++++++++++++ 13.0C 2011-3-17
+++++++++++++++++++ 19.0C 2011-3-18   +++++++++++++ 13.0C 2011-3-18
++++++++++ 10.0C 2011-3-19   ++++++++ 8.0C 2011-3-19
++++++++++++++ 14.0C 2011-3-20   ++++++ 6.0C 2011-3-20
++++++++++++++++ 16.0C 2011-3-21   ++++++++ 8.0C 2011-3-21
+++++++++++++++++++ 19.0C 2011-3-22   ++++++++++++ 12.0C 2011-3-22
++++++++++++++++++++ 20.0C 2011-3-23   +++++++++++++ 13.0C 2011-3-23
+++++++++++++++++++++ 21.0C 2011-3-24   ++++++++++++++ 14.0C 2011-3-24
++++++++++++++++++++++ 22.0C 2011-3-25   ++++++++++++++ 14.0C 2011-3-25
+++++++++++++++++++++ 21.0C 2011-3-26   +++++++++++++ 13.0C 2011-3-26
++++++++++ 10.0C 2011-3-27   ++++++++ 8.0C 2011-3-27
++++++++++++++ 14.0C 2011-3-28   ++++++++++++++ 14.0C 2011-3-28
+++++++++++++++ 15.0C 2011-3-29   +++++++++ 9.0C 2011-3-29
+++++++++++++++++ 17.0C 2011-3-30   ++++++++ 8.0C 2011-3-30
 0C 2011-3-31    0C 2011-3-31
```
Multiple reports

```sh
Highest Temperature: 38.0C on 2011-8-7
Lowest Temperature: -3.0C on 2011-1-15
Max Humidity: 100.0% on 2011-8-28

Average Highest Temp: 15.2C 
Average Lowest Temp: 8.6C 
Average Mean Humidity: 53.33% 

+++++ 5.0C 2011-3-1    0.0C 2011-3-1
++++ 4.0C 2011-3-2    0.0C 2011-3-2
++++++ 6.0C 2011-3-3    0.0C 2011-3-3
++++ 4.0C 2011-3-4    0.0C 2011-3-4
++++++ 6.0C 2011-3-5   +++ 3.0C 2011-3-5
+++++++++++++ 13.0C 2011-3-6   ++++ 4.0C 2011-3-6
++++++++++++ 12.0C 2011-3-7   ++++++ 6.0C 2011-3-7
+++++++++++++ 13.0C 2011-3-8   +++++ 5.0C 2011-3-8
+++++++++++++++ 15.0C 2011-3-9   ++++++ 6.0C 2011-3-9
+++++++++++++++ 15.0C 2011-3-10   ++++++ 6.0C 2011-3-10
++++++++++++++++ 16.0C 2011-3-11   ++++++++ 8.0C 2011-3-11
+++++++++++++++++ 17.0C 2011-3-12   ++++++++++ 10.0C 2011-3-12
++++++++++++++++++++++++++++++ 30.0C 2011-3-13   ++++++++++++ 12.0C 2011-3-13
+++++++++++++++++++++ 21.0C 2011-3-14   ++++++++++++++ 14.0C 2011-3-14
++++++++++++++++++++++ 22.0C 2011-3-15   ++++++++++++++++ 16.0C 2011-3-15
+++++++++++++++++++++ 21.0C 2011-3-16   +++++++++++++++ 15.0C 2011-3-16
++++++++++++++++++ 18.0C 2011-3-17   +++++++++++++ 13.0C 2011-3-17
+++++++++++++++++++ 19.0C 2011-3-18   +++++++++++++ 13.0C 2011-3-18
++++++++++ 10.0C 2011-3-19   ++++++++ 8.0C 2011-3-19
++++++++++++++ 14.0C 2011-3-20   ++++++ 6.0C 2011-3-20
++++++++++++++++ 16.0C 2011-3-21   ++++++++ 8.0C 2011-3-21
+++++++++++++++++++ 19.0C 2011-3-22   ++++++++++++ 12.0C 2011-3-22
++++++++++++++++++++ 20.0C 2011-3-23   +++++++++++++ 13.0C 2011-3-23
+++++++++++++++++++++ 21.0C 2011-3-24   ++++++++++++++ 14.0C 2011-3-24
++++++++++++++++++++++ 22.0C 2011-3-25   ++++++++++++++ 14.0C 2011-3-25
+++++++++++++++++++++ 21.0C 2011-3-26   +++++++++++++ 13.0C 2011-3-26
++++++++++ 10.0C 2011-3-27   ++++++++ 8.0C 2011-3-27
++++++++++++++ 14.0C 2011-3-28   ++++++++++++++ 14.0C 2011-3-28
+++++++++++++++ 15.0C 2011-3-29   +++++++++ 9.0C 2011-3-29
+++++++++++++++++ 17.0C 2011-3-30   ++++++++ 8.0C 2011-3-30
 0C 2011-3-31    0C 2011-3-31

```






