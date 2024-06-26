    # project-one
<<<<<<< branch1
## Dependencies
- Python 3.x
- pandas
- matplotlib
## Description
- Provide a numeric average rate of the state with the highest and lowest infant mortality ate in the United States.
- Provide a data outcomes to explain the correlation between states with the lowest and highest median houshold income and highest and lowest infant mortality rate.
## Installation
- To use this project, you need to have Python installed on your system. You can install the required Python packages using pip. Run the following command in your terminal or command prompt:
- '''Bash
  pip install pandas matplotlib
- Once installed, you can import the necessary modules in your Python script as follows:
- import pandas as pd
- from pathlib import Path
- import matplotlib.pyplot as plt
## Usage
- Ensure you have Python installed on your system.
- Clone or download this repository to your local machine.
- Place the CSV files (data-table.csv and poorest-states-2024.csv) in the same directory as the Python script.
- Open a terminal or command prompt and navigate to the directory containing the Python script.
## Functionality
- Reads data from CSV files (data-table.csv and poorest-states-2024.csv) into pandas DataFrames.
- Cleans and processes the data, including converting columns to numeric types and grouping by specific columns.
- Calculates average rates and identifies states with the highest and lowest average rates.
- Visualizes the data using matplotlib, including bar charts for average rates by state and median household income by state in 2021.
- Performs additional analysis, such as identifying the top and bottom five states based on median household income in 2021.
A shared repo for first project
* Used census API to get poverty rates by state
* Used Maternal Death Counts and Rates tabular data from KFF website below:
    https://www.kff.org/other/state-indicator/maternal-deaths-and-mortality-rates-per-100000-live-births/?currentTimeframe=0&sortModel=%7B%22colId%22:%22Location%22,%22sort%22:%22asc%22%7D
* Definitions
Maternal deaths: include deaths of women while pregnant or within 42 days of termination of pregnancy, irrespective of the duration and the site of the pregnancy, from any cause related to or aggravated by the pregnancy or its management, but not from accidental or incidental causes.
* Data on popular vote in 2020 election came from:
    https://www.cookpolitical.com/2020-national-popular-vote-tracker
