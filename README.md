# Nobel laureates data analysis

## Description
This project involves extracting and visualizing data regarding Nobel laureates. 
The main focus is on the laureates' names and their countries of origin. 
This analysis uses Python, specifically employing libraries like `requests` for API calls, `json` for handling JSON data, and `pygal` for data visualization.

## Features
- **Data extraction**: The script extracts data from the Nobel Prize API, focusing on laureates' information.
- **Data processing**: It processes the JSON data to extract the full names of the laureates and their countries of origin.
- **Error handling**: The script gracefully handles situations where country data might be missing or incorrect.
- **Data visualization**: Generates a bar chart representing the number of Nobel laureates per country using `pygal`.

## Installation and usage
To run this project locally, you will need Python and the following libraries installed on your system:
- Python 3.x
- `requests` library
- `json` library (usually included in standard Python distribution)
- `pygal` library for data visualization

After installing Python, proceed as follows:
1. Clone the repository to your local machine.
2. Run `APIscrapingExample_NobelLaureates.py` in the terminal or using an interpreter.
3. This will start the process of data extraction and visualization:
- API request: The script sends a request to the Nobel Prize API and retrieves data about laureates.
- JSON parsing: The received data is parsed from JSON format.
- Data extraction and printing: It extracts each laureate's name and country of origin, handling any missing data, and prints the info on screen.
- Data aggregation: The script counts the occurrences of each country in the dataset.
- Visualization: Creates a bar chart showing the distribution of Nobel laureates by country.

## Contributing
Contributions to this project are welcome. Please fork the repository and submit a pull request with your changes.

## License
[MIT License](LICENSE.md) - feel free to use and modify this code for your own projects.

