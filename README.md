# Partstown Webscraper

## Introduction

The Partstown Webscraper is a tool designed to identify and catalog parts for the TRUE GDM-72 Refrigerator. It uses web scraping to gather specific data on each part, linking them with their unique serial numbers, which are crucial for precise tracking and inventory management. This tool is particularly useful for restaurant operations where efficient maintenance of refrigeration equipment is essential.

## Objective

To automate the process of extracting detailed information about parts for the TRUE GDM-72 Refrigerator, including their unique serial numbers, from the Partstown website.

## Features

- **Serial Number Identification**: Extracts and displays serial numbers associated with each part of the TRUE GDM-72.
- **Part Filtering**: Filters parts based on specific criteria like gaskets, compressors, doors, hinges, and screws.
- **Automated Data Extraction**: Scrapes the Partstown website to collect part details automatically.
- **CSV Output**: Outputs the scraped data into a CSV file for easy management and reporting.

## Technologies Used

- Python 3.x
- BeautifulSoup for HTML parsing.
- pandas for data manipulation and CSV file operations.
- requests for handling HTTP requests.

## Setup

1. **Clone the repository**:

git clone https://github.com/yourusername/partstown-webscraper.git

2. **Navigate to the project directory:**

cd partstown-webscraper

3. **Install dependencies:**

pip install -r 

## Usage

To execute the bot:

python partstownWebscrape_v2.py

This will start the bot, which will perform the tasks as scheduled. Make sure to configure the scheduler according to your needs.

## Testing

### Strategy

- `Unit Tests`: Test each function for correct behavior, particularly focusing on accurate HTML parsing and data extraction.
- `Integration Tests`: Ensure that the components work together seamlessly to produce the expected output in the CSV file.
- `Error Handling Tests`: Verify that the program can handle potential errors gracefully, such as network issues or changes in the HTML structure of the source website.

### Features Tested

- `Data Parsing Accuracy:`: Confirms that the parsing logic correctly extracts and categorizes part names and serial numbers.
- `Filter Logic`: Verifies that the script correctly identifies and includes only the specified parts in the output.

### Features Not Tested

- `Internal Workings of Libraries`: Assumes that external libraries such as BeautifulSoup and pandas function as intended without testing their internal mechanisms.



