# How to run the code

## Introduction

Welcome to the data-analyst-full-project-adalab, a code project for data analysis that includes data cleaning, data manipulation, and data visualization. The project is written in Python and uses various libraries such as Pandas, Numpy, and Matplotlib. You can access the code on Github at https://github.com/belenaj.

The project involves three parts: data collection, data preparation, and data ingestion, which are executed in sequence.

The data for this project is extracted from the API https://www.balldontlie.io/home.html#introduction, which is a basketball database that does not require registration or an API key.

## Instructions

### 1. Data collection

Open the Jupyter notebook 1.data_collection.ipynb located in the "notebooks" folder for data collection.
Ensure that you have the following libraries installed: request, pandas, numpy, json, and jupyter.

!pip install request
!pip install pandas
!pip install numpy
!pip install json
!pip install jupyter

- Run the Jupyter notebook ``1.data_collection.ipynb``.

- In the script you can find two reusable functions named "paginate_api_calls" and "write_json_file".

    - **"paginate_api_calls"** handles the pagination of the API. It accepts two arguments(url, params).

    - **"write_json_file"** writes the responses to disk. It accepts two arguments (results, filename).

- After running the script, three JSON files will be created:
    - "teams.json" in the "data/teams" folder
    - "games.json" in the "data/games" folder
    - "players.json" in the "data/players" folder

⚠️Note that a local MySQL database is required for further execution.

### 2. Data preparation

Next, perform the following steps:

- Open the Jupyter notebook 2.data_preparation.ipynb in the "notebooks" folder.

- Ensure that you have the following libraries installed: pandas, numpy, and json.

!pip install pandas
!pip install numpy
!pip install json

- Run the Jupyter notebook ``2.data_preparation.ipynb``.

- In the script you can find two functions named "read_json_file" and "csv_file".

    - **"read_json_file"** reads a JSON file. It accepts one argument (file is the name of the JSON file created after running the script ``1.data_collection``, it is a string and must include the ubication before the name)

    - **"csv_file"**  normalizes the JSON data using pandas json_normalize() method to convert the nested JSON data to a flat table structure and save the flattened data as CSV file. It accepts three arguments (open_file, ubi and csv_file_name. open_file is the result of applying the read_json_file. ubi is the name in string of the folder where we want to save the file, and csv_file_name is the name of the CSV_file, which must be a string.)

- After running the script, three CSV files will be created:
    - "teams.csv" in the "data/teams" folder
    - "games.csv" in the "data/games" folder
    - "players.csv" in the "data/players" folder

### 3. Data ingestion

Lastly, complete the following steps:

- Open the Jupyter notebook ``3.data_ingestion.ipynb`` in the "notebooks" folder.

- Ensure that you have the following libraries installed: 

!pip install nbconvert
!pip install python-dotenv
!pip install mysql-connector
!pip install mysql-connector-python

- Run the Jupyter notebook ``3.data_ingestion.ipynb``.

- In the script you can find four functions named "open_file", "create_DB", "execute_query" and "update_to_null".

    - **"open_file"** opens a csv file and give back a Dataframe, it is the result of running the sricpt `2.data_preparation` It accepts two arguments: ubi and csv_file. ubi is the folder where is the file, must be a string. csv_file which is expected to be a string representing the name of the CSV file we want to open.

    - **"create_DB"** creates a new MySQL database with the given name as the argument, using the specified user credentials and host. It returns a closed cursor object after executing the creation query.

    - **"execute_query"** takes an SQL query as input, connects to a MySQL database, and executes the query. If there is an error, it will print out information about the error. Finally, it closes the cursor and the database connection. It accepts an SQL query.

    -**"update_to_null"** creates a SQL query string that updates the specified column in the specified table to NULL where the value of the column is 'None'. It accepts two arguments: table (the name of the table) and column (the name of the column to update).

- ⚠️ ATTENTION
* The functions "create_DB" and "execute_query" connect to the MySQL server using the root user and the password stored in the password_ada variable. password_ada must be replaced with your password. 
os.getenv() is a method in the os module in Python that retrieves the value of an environment variable. Environment variables are variables that are set outside of the application code to store sensitive information as passwords.

* In order to create the tables it is necesary to create the queries in the folder sql/ddl. The code will read the SQL query to create a table from a file, and executes it using the function execute_query().

* To insert the data the code retrieves data from a SQLite database, then iterates over the rows of data, checking for any None values. If a None value is found in a row, it is replaced with the string "None". Then a SQL query is constructed to insert the row of data into each table (table_teams, table_games, table_players). The constructed query is then executed with the execute_query() function. If there are no None values in a row, the row is inserted into the table as is.

- As a result there will be crated in MYSQL:
    - "db_ball_api" database
    - "table_teams" table
    - "table_games" table
    - "table_players" table
    - Ingestion of data into all three created tables.

### Convertion from jupyter notebook to python 🐍

- The nbconvert package allows Jupyter notebooks to be converted to a variety of formats, including Python scripts. This can be useful for sharing code with individuals who do not have Jupyter installed or for incorporating notebook code into a larger codebase.

- To convert the Jupyter notebooks located in the "notebooks" folder, specifically the files named "1.data_collection.ipynb", "2.data_preparation.ipynb", and "3.data_ingestion.ipynb", follow these steps:

    1. Open your terminal or command prompt.

    2. Navigate to the "notebooks" folder using the cd command.

    3. Run the following command:
    
    This command will convert the specified Jupyter notebooks to Python scripts.

    Note: If you have multiple Jupyter notebooks in the "notebooks" folder and you want to convert them all to Python scripts, you can use the * wildcard character. For example:

    4. After running the command, you should see the newly created Python scripts in the "notebooks" folder.