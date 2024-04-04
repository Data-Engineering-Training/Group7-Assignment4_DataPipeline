# MEPE RURAL BANK DATABASE ASSIGNMENT

## Overview

This project generates synthetic bank data using the Faker library in Python. It includes scripts to generate customer information, account details, and transaction data. The generated data can be ingested into a MySQL database for further analysis.

## Prerequisites

- Python
- Docker

## Installation

1. Clone this repository to your local machine.
2. Install the required Python packages:  `pip install -r requirements.txt`. 
   You can use a virtual environment for isolating these dependencies from other projects on your system.
   
## Running the Application Locally

The application is designed to be run using Docker, which simplifies the process of setting up and running the project in different environments. To get
To run the application locally, you will need to have both Docker and Docker Compose installed on your machine.
 Run the following command in terminal/command prompt while inside the project directory:
 docker-compose up --build


## Usage
To generate the data, run the following command in terminal/command prompt while inside the /pipeline directory:
`python data_generator.py` 
This will generate random data and save it as CSV files into the "data" folder.

To store the csv files into MySQL, run the following command
`python ingest_data.py`. 


## Folder Structure

- `data/generated_data`: Contains the generated CSV files for customers, accounts, and transactions.
- `docker-compose.yml`: Docker configuration file.
- `init.sql`: SQL script to initialize the database schema.
- `ingest_data.py`: Python script to ingest generated data into the MySQL database.
- `queries.sql`: Sample SQL queries to analyze the bank data.

## Docker Configuration

The `docker-compose.yml` file defines services for MySQL and PHPMyAdmin. MySQL is used to store the bank data, and PHPMyAdmin provides a web interface for database management.

