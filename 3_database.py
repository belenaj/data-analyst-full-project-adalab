#!/usr/bin/env python
# coding: utf-8

# # 3. Data ingestion

# Using the python mysql connector, read and upload the previously generated CSV files into the MYSQL Database
# 
# Output/Deliverables:
# - Table DDLs (Create table statements) in the folder sql/ddl/
# - Python code that creates the tables and ingests the data into the tables

# In[3]:


# pip install jupyter


# In[4]:


# pip install nbconvert

# In[1]:


# Data processing
# ==============================================================================
import pandas as pd
import numpy as np
import datetime

# mysql connector
# ==============================================================================
# pip install mysql-connector
# pip install mysql-connector-python
import mysql.connector 

#Allows us to display more than one output per cell
# ==============================================================================
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all" 

# Display all columns
# ==============================================================================
pd.options.display.max_columns = None


# In[2]:


# This is a function that reads the CSV file and returns the resulting DataFrame. 

def open_file (csv_file): #parameter `csv_file` which is expected to be a string representing the name of a CSV file.
    df = pd.read_csv(f'notebooks/{csv_file}.csv', index_col=0) # The `index_col=0` argument specifies that the first column of the CSV file should be used as the index of the DataFrame.

    return df


# ``Teams``

# In[3]:


df_teams = open_file("teams")
df_teams.head()


# ``Games``

# In[4]:


df_games = open_file("games")
df_games.head()


# ``Players``

# In[5]:


df_players = open_file("players")
df_players.head()


# ## Database creation

# In[6]:


def create_DB(nombre_bbdd):
    cnx = mysql.connector.connect(user='root', password='AlumnaAdalab',
                                host='127.0.0.1')

    mycursor = cnx.cursor()

    sql = (f"CREATE DATABASE {nombre_bbdd}")
    try:
        mycursor.execute(sql)
        print(f"The database {nombre_bbdd} has been successfully created.")

    except mysql.connector.Error as err:
        print(err)
        print("Error Code:", err.errno)
        print("SQLSTATE", err.sqlstate)
        print("Message", err.msg)
    return mycursor.close() 
    


# In[7]:


create_DB("db_ball_api")


# ## Tables creation

# In[7]:


# This is a Python function that connects to a MySQL database using the `mysql.connector` module and executes a given SQL query. 

def execute_query(query): # The function takes a single argument `query`, which is the SQL query to be executed.
    
    cnx = mysql.connector.connect(user='root', password='AlumnaAdalab',
                                host='127.0.0.1', database= 'DB_Ball_API')

    mycursor = cnx.cursor() # It creates a cursor object, executes the query using the cursor, and commits the changes to the database.
    
    try: 
        mycursor.execute(query)
        cnx.commit()

    except mysql.connector.Error as err:
        print(err)
        print("Error Code:", err.errno)
        print("SQLSTATE", err.sqlstate)
        print("Message", err.msg)
    
    else:
        mycursor.close()
        cnx.close() # Finally, the function closes the cursor and the database connection.


# `Teams`

# In[13]:


teams_table_query = """CREATE TABLE IF NOT EXISTS table_teams (
id INT NOT NULL,
abbreviation VARCHAR(255),
city VARCHAR(255),
conference VARCHAR(255),
division VARCHAR(255),
full_name VARCHAR(255),
name VARCHAR(255),
PRIMARY KEY (id));"""


# In[14]:


execute_query(teams_table_query)


# `Games`

# In[15]:


games_table_query = """CREATE TABLE IF NOT EXISTS table_games (
id INT NOT NULL ,
`date` VARCHAR(255) ,
home_team_score INT ,
period INT ,
postseason VARCHAR(255) ,
season INT ,
status VARCHAR(255) ,
time VARCHAR(255) ,
visitor_team_score INT ,
`home_team.id` INT ,
`home_team.abbreviation` VARCHAR(255) ,
`home_team.city` VARCHAR(255) ,
`home_team.conference` VARCHAR(255) ,
`home_team.division` VARCHAR(255) ,
`home_team.full_name` VARCHAR(255) ,
`home_team.name` VARCHAR(255) ,
`visitor_team.id` INT ,
`visitor_team.abbreviation` VARCHAR(255) ,
`visitor_team.city` VARCHAR(255) ,
`visitor_team.conference` VARCHAR(255) ,
`visitor_team.division` VARCHAR(255) ,
`visitor_team.full_name` VARCHAR(255) ,
`visitor_team.name` VARCHAR(255) ,
PRIMARY KEY (id));"""


# In[16]:


execute_query(games_table_query)


# `Players`

# In[17]:


players_table_query = """CREATE TABLE IF NOT EXISTS table_players (
id INT NOT NULL ,
first_name VARCHAR(255),
height_feet VARCHAR(255),
height_inches VARCHAR(255),
last_name VARCHAR(255),
position VARCHAR(255),
weight_pounds VARCHAR(255),
`team.id` INT,
`team.abbreviation` VARCHAR(255),
`team.city` VARCHAR(255),
`team.conference` VARCHAR(255),
`team.division` VARCHAR(255),
`team.full_name` VARCHAR(255),
`team.name` VARCHAR(255),
PRIMARY KEY (id));"""


# In[18]:


execute_query(players_table_query)


# ## Insert data

# `Teams`

# In[9]:


# This code is iterating through each row of a pandas DataFrame using the `iterrows()` method. For each row, it is constructing an SQL query to insert the values of that row into a table.
for index, row in df_teams.iterrows():

    try: 

        query_teams = f""" INSERT INTO table_teams (`id`, `abbreviation`, `city`, `conference`, `division`, `full_name`, `name`)
                        VALUES ("{row['id']}", "{row['abbreviation']}", "{row['city']}", "{row['conference']}", "{row['division']}", "{row['full_name']}","{row['name']}");
                                """
        # Llamamos a la función dentro del for, ya que si no, no itera por todos los valores y sólo nos inserta la primera línea.
        execute_query(query_teams)

    except:
            pass


# `Games`

# In[10]:


# This code is iterating through each row of a pandas DataFrame using the `iterrows()` method. For each row, it is constructing an SQL query to insert the values of that row into a table.
for index, row in df_games.iterrows():

    try:    

        query_games = f""" INSERT INTO table_games (`id`, `date`, `home_team_score`, `period`, `postseason`, `season`, `status`,
                                                    `time`, `visitor_team_score`,`home_team.id`, `home_team.abbreviation`, `home_team.city`,
                                                    `home_team.conference`, `home_team.division`, `home_team.full_name`, `home_team.name`, 
                                                    `visitor_team.id`, `visitor_team.abbreviation`, `visitor_team.city`, `visitor_team.conference`,
                                                    `visitor_team.division`, `visitor_team.full_name`, `visitor_team.name`)

                        VALUES ("{row['id']}", "{row['date']}", "{row['home_team_score']}", "{row['period']}", "{row['postseason']}", "{row['season']}","{row['status']}",
                                "{row['time']}", "{row['visitor_team_score']}", "{row['home_team.id']}", "{row['home_team.abbreviation']}", "{row['home_team.city']}",
                                "{row['home_team.conference']}", "{row['home_team.division']}", "{row['home_team.full_name']}", "{row['home_team.name']}",
                                "{row['visitor_team.id']}", "{row['visitor_team.abbreviation']}", "{row['visitor_team.city']}", "{row['visitor_team.conference']}",
                                "{row['visitor_team.division']}", "{row['visitor_team.full_name']}", "{row['visitor_team.name']}");
                                """
        # Llamamos a la función dentro del for, ya que si no, no itera por todos los valores y sólo nos inserta la primera línea.
        execute_query(query_games)

    except:
        pass


# `Players`

# In[11]:


# This code is iterating through each row of a pandas DataFrame using the `iterrows()` method. For each row, it is constructing an SQL query to insert the values of that row into a table.
for index, row in df_players.iterrows():

    try: 
        query_players = f""" INSERT INTO table_players (`id`, `first_name`, `height_feet`, `height_inches`, `last_name`,
                                                    `position`, `weight_pounds`,`team.id`, `team.abbreviation`,
                                                    `team.city`, `team.conference`, `team.division`, `team.full_name`, 
                                                    `team.name`)
                        VALUES ("{row['id']}", "{row['first_name']}", "{row['height_feet']}", "{row['height_inches']}", "{row['last_name']}",
                                "{row['position']}", "{row['weight_pounds']}", "{row['team.id']}", "{row['team.abbreviation']}",
                                "{row['team.city']}", "{row['team.conference']}", "{row['team.division']}", "{row['team.full_name']}",
                                "{row['team.name']}");
                                """
    # Llamamos a la función dentro del for, ya que si no, no itera por todos los valores y sólo nos inserta la primera línea.
        execute_query(query_players)

    except:
        pass


# ## Clean null values

# In[12]:


# This function creates a SQL query string that updates the specified `column` in the specified `table` to `NULL` where the value of the `column` is `'NaN'`. 

def update_to_null (table, column): # It takes two parameters: `table` and `column`.
    query = f"UPDATE {table} set {column} = NULL WHERE {column} = 'NaN'"
    execute_query(query) # The function then executes the query using a function called `execute_query`
    
    return query #returns the query string.


# `Teams`

# In[13]:


update_to_null("table_teams", "city")


# In[14]:


update_to_null("table_teams", "division")


# `Players`

# In[15]:


update_to_null("table_players", "height_feet")


# In[16]:


update_to_null("table_players", "height_inches")


# In[17]:


update_to_null("table_players", "weight_pounds")

