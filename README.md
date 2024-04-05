**Faker Data Generator and ETL Pipeline for Company Data**

This project utilizes Python's Faker library to generate 100,000 synthetic records for 10 different companies. 
An ETL (Extract, Transform, Load) pipeline has been built to extract data from CSV files, transform it, and ingest it into a PostgreSQL database. 
This process has been implemented individually for each of the 10 companies.

**Table of Contents**

    About
    Features
    Installation
    Usage
    Contributors
    License

**About**

This project aims to create synthetic data for 10 different companies using Python's Faker library. 
The generated data is then processed through an ETL pipeline to be stored in a PostgreSQL database. Each company's data is handled separately within the pipeline.

**Features**

    Generates synthetic data for 10 different companies.
    Implements an ETL pipeline for each company to extract, transform, and load data into a PostgreSQL database.

**Installation**

Clone the repository to your local machine:

	git clone https://github.com/your-username/your-project.git

Install the required dependencies:

	pip install glob
	pip install pandas
	pip install sqlalchemy

Set up a PostgreSQL database and update the database configuration in the project files.

Run the ETL pipeline for each company to generate and ingest the data.

**Usage**

Generate synthetic data for a company using the Faker library:

	python generate_data.py

Run the ETL pipeline to process and ingest the generated data into the PostgreSQL database:

	python etl_pipeline.py

Repeat the above steps for each company to handle their respective data.

**Contributors**

Contributors for this project are:

    Emmanuel Gligbe
    Israel Ansah Owusu
    Francisca Frimpomaa Amponsah
    Florentyna Anima Adu Boakye Yiadom
    Ruth Amanquah
    Nathaniel Yeboah Frimpong
    Vanessa Bedzra

**License**

This project is licensed under the MIT License.
