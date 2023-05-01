#!/usr/bin/env python
# coding: utf-8

# # 3. Data ingestion

# Using the python mysql connector, read and upload the previously generated CSV files into the MYSQL Database
#
# Output/Deliverables:
# - Table DDLs (Create table statements) in the folder sql/ddl/
# - Python code that creates the tables and ingests the data into the tables

# In[2]:


# INSTALL LIBRARIES
# ==============================================================================
# !pip install nbconvert
# !pip install python-dotenv
# !pip install mysql-connector
# !pip install mysql-connector-python
# pip install nbconvert


# In[4]:


# IMPORT LIBRARIES

# Data processing
# ==============================================================================
import pandas as pd
import numpy as np

# mysql connector
# ==============================================================================
import mysql.connector

# interface for SQLite databases
# ==============================================================================
import sqlite3

# Allows us to display more than one output per cell
# ==============================================================================
from IPython.core.interactiveshell import InteractiveShell

InteractiveShell.ast_node_interactivity = "all"

# Display all columns
# ==============================================================================
pd.options.display.max_columns = None

# Hide passwords
# ==============================================================================
import os
from dotenv import load_dotenv

load_dotenv()


# ## File opening

# In[5]:


# This is a function that reads the CSV file and returns the resulting DataFrame.


def open_file(
    ubi, csv_file
):  # argument ubi is the folder where is the file, must be a string. `csv_file` which is expected to be a string representing the name of a CSV file.
    df = pd.read_csv(
        ubi + csv_file + ".csv", index_col=0
    )  # The `index_col=0` argument specifies that the first column of the CSV file should be used as the index of the DataFrame.

    return df


# ``Teams``

# In[6]:


df_teams = open_file("../sample/data/", "teams")
df_teams.head()


# ``Games``

# In[7]:


df_games = open_file("../sample/data/", "games")
df_games.head()


# ``Players``

# In[8]:


df_players = open_file("../sample/data/", "players")
df_players.head()


# ## Database creation

# In[11]:


# os.getenv() is a method in the os module in Python that retrieves the value of an environment variable.
password_ada = os.getenv("password_ada")


# In[12]:


# This function creates a new database in a MySQL server.


def create_DB(
    nombre_bbdd,
):  # `nombre_bbdd`, is the name of the database to be created, must be a string.
    cnx = mysql.connector.connect(
        user="root", password=password_ada, host="127.0.0.1"
    )  # A connection to the MySQL server is established using the `mysql.connector` module.

    mycursor = cnx.cursor()  # A cursor object is created to execute SQL statements.

    sql = f"CREATE DATABASE {nombre_bbdd}"  # he SQL statement to create a new database is constructed using the `nombre_bbdd`argument.

    try:  # Execute the SQL statement using the cursor's `execute()` method. If the execution is successful, a message is printed to confirm the creation of the database.
        mycursor.execute(sql)
        print(f"The database {nombre_bbdd} has been successfully created.")

    except mysql.connector.Error as err:  # If an error occurs, the `except` block catches the error and prints the error message, error code, and SQL state.
        print(err)
        print("Error Code:", err.errno)
        print("SQLSTATE", err.sqlstate)
        print("Message", err.msg)
    return (
        mycursor.close()
    )  # Finally, the function closes the cursor using the `close()` method and returns `None`.


# In[13]:


create_DB("db_ball_api")


# ## Tables creation

# In[14]:


# This is a Python function that connects to a MySQL database using the `mysql.connector` module and executes a given SQL query.


def execute_query(
    query,
):  # The function takes a single argument `query`, which is the SQL query to be executed.

    cnx = mysql.connector.connect(
        user="root", password=password_ada, host="127.0.0.1", database="db_ball_api"
    )

    mycursor = (
        cnx.cursor()
    )  # It creates a cursor object, executes the query using the cursor, and commits the changes to the database.

    try:  # Execute the SQL statement using the cursor's `execute()` method.
        mycursor.execute(query)
        cnx.commit()

    except mysql.connector.Error as err:  # If an error occurs, the `except` block catches the error and prints the error message, error code, and SQL state.
        print(err)
        print("Error Code:", err.errno)
        print("SQLSTATE", err.sqlstate)
        print("Message", err.msg)

    else:
        mycursor.close()
        cnx.close()  # Finally, the function closes the cursor and the database connection.


# `Teams`

# In[62]:


with open("../sql/ddl/create_teams_table.sql", "r") as sql_file:
    teams_sql_query = sql_file.read()
    execute_query(teams_sql_query)


# In[63]:


teams_sql_query


# In[104]:


execute_query(teams_sql_query)


# `Games`

# In[18]:


with open("../sql/ddl/create_games_table.sql", "r") as sql_file:
    games_sql_query = sql_file.read()


# In[19]:


games_sql_query


# In[108]:


execute_query(games_sql_query)


# `Players`

# In[21]:


with open("../sql/ddl/create_players_table.sql", "r") as sql_file:
    players_sql_query = sql_file.read()


# In[22]:


players_sql_query


# In[23]:


execute_query(players_sql_query)


# ## Data ingestion

# `Teams`

# In[105]:


# This code is connecting to a SQLite database named 'DB_Ball_API', creating a cursor object, and then using pandas to write a dataframe named 'df_teams' to a table named 'table_teams' in the database. It then executes a SELECT statement to retrieve all rows from the 'table_teams' table, and for each row, it checks if any of the values are None. If any values are None, it replaces them with the string "None" and inserts the updated row into the 'table_teams' table using an INSERT statement. If none of the values are None, it inserts the original row into the 'table_teams' table using an INSERT statement. The function 'execute_query' is not shown in this code, so it is assumed to be defined elsewhere.

conn = sqlite3.connect("DB_Ball_API")
c = conn.cursor()

df_teams.to_sql("table_teams", conn, if_exists="replace", index=False)

c.execute(
    """  
SELECT * FROM table_teams
          """
)


for row in c.fetchall():

    # print (row)
    if None in list(row):
        list_none = list(row)
        for index, value in enumerate(list_none):
            if value == None:
                list_none[index] = "None"
            tupla_none = tuple(list_none)

        query_teams = f""" INSERT INTO table_teams (`id`, `abbreviation`, `city`, `conference`, `division`, `full_name`, `name`)
                            VALUES {tupla_none};
                                    """
        execute_query(query_teams)

    else:
        query_teams = f""" INSERT INTO table_teams (`id`, `abbreviation`, `city`, `conference`, `division`, `full_name`, `name`)
                            VALUES {row};
                                    """
        execute_query(query_teams)


# `Games`

# In[109]:


# This code is connecting to a SQLite database named 'DB_Ball_API', creating a cursor object, and then using pandas to write a dataframe named 'df_games' to a table named 'table_games' in the database. It then executes a SELECT statement to retrieve all rows from the 'table_games' table, and for each row, it checks if any of the values are None. If any values are None, it replaces them with the string "None" and inserts the updated row into the 'table_games' table using an INSERT statement. If none of the values are None, it inserts the original row into the 'table_games' table using an INSERT statement. The function 'execute_query' is not shown in this code, so it is assumed to be defined elsewhere.

conn = sqlite3.connect("DB_Ball_API")
c = conn.cursor()

df_games.to_sql("table_games", conn, if_exists="replace", index=False)

c.execute(
    """  
SELECT * FROM table_games
          """
)


for row in c.fetchall():

    # print (row)
    if None in list(row):
        list_none = list(row)
        for index, value in enumerate(list_none):
            if value == None:
                list_none[index] = "None"
            tupla_none = tuple(list_none)

        query_games = f"""INSERT INTO table_games (`id`, `date`, `home_team_score`, `period`, `postseason`, `season`, `status`,
                                                    `time`, `visitor_team_score`,`home_team.id`, `home_team.abbreviation`, `home_team.city`,
                                                    `home_team.conference`, `home_team.division`, `home_team.full_name`, `home_team.name`, 
                                                    `visitor_team.id`, `visitor_team.abbreviation`, `visitor_team.city`, `visitor_team.conference`,
                                                    `visitor_team.division`, `visitor_team.full_name`, `visitor_team.name`)
                            
                            VALUES {tupla_none};
                                    """
        execute_query(query_games)

    else:
        query_games = f"""INSERT INTO table_games (`id`, `date`, `home_team_score`, `period`, `postseason`, `season`, `status`,
                                                    `time`, `visitor_team_score`,`home_team.id`, `home_team.abbreviation`, `home_team.city`,
                                                    `home_team.conference`, `home_team.division`, `home_team.full_name`, `home_team.name`, 
                                                    `visitor_team.id`, `visitor_team.abbreviation`, `visitor_team.city`, `visitor_team.conference`,
                                                    `visitor_team.division`, `visitor_team.full_name`, `visitor_team.name`)
                            
                            VALUES {row};
                                    """
        execute_query(query_games)


# `Players`

# In[110]:


# This code is connecting to a SQLite database named 'DB_Ball_API', creating a cursor object, and then using pandas to write a dataframe named 'df_games' to a table named 'table_games' in the database. It then executes a SELECT statement to retrieve all rows from the 'table_games' table, and for each row, it checks if any of the values are None. If any values are None, it replaces them with the string "None" and inserts the updated row into the 'table_games' table using an INSERT statement. If none of the values are None, it inserts the original row into the 'table_games' table using an INSERT statement. The function 'execute_query' is not shown in this code, so it is assumed to be defined elsewhere.

conn = sqlite3.connect("DB_Ball_API")
c = conn.cursor()

df_players.to_sql("table_players", conn, if_exists="replace", index=False)

c.execute(
    """  
SELECT * FROM table_players
          """
)


for row in c.fetchall():

    # print (row)
    if None in list(row):
        list_none = list(row)
        for index, value in enumerate(list_none):
            if value == None:
                list_none[index] = "None"
            tupla_none = tuple(list_none)

        query_players = f"""INSERT INTO table_players (`id`, `first_name`, `height_feet`, `height_inches`, `last_name`,
                                                    `position`, `weight_pounds`,`team.id`, `team.abbreviation`,
                                                    `team.city`, `team.conference`, `team.division`, `team.full_name`, 
                                                    `team.name`)
                            
                            VALUES {tupla_none};
                                    """
        execute_query(query_players)

    else:
        query_players = f"""INSERT INTO table_players (`id`, `first_name`, `height_feet`, `height_inches`, `last_name`,
                                                    `position`, `weight_pounds`,`team.id`, `team.abbreviation`,
                                                    `team.city`, `team.conference`, `team.division`, `team.full_name`, 
                                                    `team.name`)
                            
                            VALUES {row};
                                    """
        execute_query(query_players)


# ## Clean null values

# In[111]:


# This function creates a SQL query string that updates the specified `column` in the specified `table` to `NULL` where the value of the `column` is `'None'`.


def update_to_null(table, column):  # It takes two parameters: `table` and `column`.
    query = f"UPDATE {table} set {column} = NULL WHERE {column} = 'None'"
    execute_query(
        query
    )  # The function then executes the query using a function called `execute_query`

    return query  # returns the query as a string.


# `Teams`

# In[112]:


update_to_null("table_teams", "city")


# In[113]:


update_to_null("table_teams", "division")


# `Players`

# In[114]:


update_to_null("table_players", "height_feet")


# In[115]:


update_to_null("table_players", "height_inches")


# In[116]:


update_to_null("table_players", "weight_pounds")
