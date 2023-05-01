#!/usr/bin/env python
# coding: utf-8

# # 2. Data preparation

# Create a python script that will convert the previously generated JSON files into flattened CSV files, for each of the three exercises above. Sample files will be available in the folder sample/data
#
# ### Output/Deliverables:
# - One flattened CSV file for each of the entities (teams, players, games)

# In[ ]:


# INSTALL LIBRARIES
# ==============================================================================
# !pip install pandas
# !pip install numpy
# !pip install json


# In[1]:


# IMPORT LIBRARIES

# Data processing
# ==============================================================================
import pandas as pd
import numpy as np
import json

# Display all columns
# ==============================================================================
pd.options.display.max_columns = None


# In[2]:


# This function reads a JSON file, encapsulates the string with brackets [], replaces any new line characters with an empty string, and replaces any instances of }{ with },{ to ensure that the file is in a valid JSON format. Finally, it loads the modified string as a JSON object using the json.loads() method and returns the resulting object.
def read_json_file(file):  # `file`is the name of the JSON file

    with open(file, "r") as r:
        response = r.read()
        response = response.replace("\n", "")
        response = response.replace("}{", "},{")
        response = "[" + response + "]"
    return json.loads(response)


# In[3]:


# The above code is creating a list of dictionaries and then converting it to a dataframe and saving as a csv file.
def csv_file(
    open_file, ubi, csv_file_name
):  # `open_file` is the result of applying the read_json_file, `ubi` is the name in string of the folder where we want to save the file, `csv_file_name` is the name of the CSV_file, must be a string.

    information = []
    for call in open_file:
        for i in call["data"]:
            information.append(i)
            df = pd.DataFrame.from_dict(pd.json_normalize(information))
    df.to_csv(ubi + csv_file_name + ".csv")

    return df


# ## 2.1 Teams

# In[4]:


all_teams = read_json_file("../sample/data/teams.json")


# In[5]:


teams_csv = csv_file(all_teams, "../sample/data/", "teams")


# In[6]:


teams_csv.tail()


# In[7]:


teams_csv.columns


# In[8]:


teams_csv.shape


# ## 2.2 Games

# In[9]:


all_games = read_json_file("../sample/data/games.json")


# In[10]:


games_csv = csv_file(all_games, "../sample/data/", "games")


# In[11]:


games_csv.tail()


# In[12]:


games_csv.info()


# In[13]:


games_csv.columns


# In[14]:


games_csv.shape


# ## 2.3 Players

# In[15]:


all_players = read_json_file("../sample/data/players.json")


# In[16]:


players_csv = csv_file(all_players, "../sample/data/", "players")


# In[17]:


players_csv.head()


# In[18]:


players_csv.tail()


# In[20]:


players_csv.shape


# In[21]:


players_csv.columns


# In[22]:


players_csv.info()
