#!/usr/bin/env python
# coding: utf-8

# # 2. Data preparation

# Create a python script that will convert the previously generated JSON files into flattened CSV files, for each of the three exercises above. Sample files will be available in the folder sample/data
# 
# ### Output/Deliverables:
# - One flattened CSV file for each of the entities (teams, players, games)

# In[32]:


# pip install pandas


# In[33]:


# pip install numpy


# In[34]:


# Data processing
# ==============================================================================
import pandas as pd
import numpy as np
import json

# Display all columns
# ==============================================================================
pd.options.display.max_columns = None


# In[2]:


# This function the entire file, add brackets [] to encapsulate the string and then load it as string with json.loads()
def read_json_file(file):
    
    with open(file, "r") as r:
        response = r.read()
        response = response.replace('\n', '')
        response = response.replace('}{', '},{')
        response = "[" + response + "]"
    return json.loads(response)


# In[30]:


#The above code is creating a list of dictionaries and then converting it to a dataframe anda saving as a csv file.

def csv_file(open_file,csv_file_name):
   
    information=[]
    for call in open_file:
        for i in call["data"]:
            information.append(i)
            df = pd.DataFrame.from_dict(pd.json_normalize(information))
    df.to_csv("notebooks/"+ csv_file_name+".csv")
            
    return df


# ## 2.1 Teams

# In[28]:



all_teams= read_json_file('notebooks/teams.json')


# In[31]:


teams_csv = csv_file(all_teams,"teams")


# In[6]:


teams_csv.tail()


# In[20]:


teams_csv.columns


# In[7]:


teams_csv.shape


# ## 2.2 Games

# In[8]:


all_games= read_json_file('notebooks/games.json')


# In[9]:


games_csv = csv_file(all_games,"games")


# In[24]:


games_csv.tail()


# In[23]:


games_csv.info()


# In[22]:


games_csv.columns


# In[11]:


games_csv.tail()


# In[12]:


games_csv.shape


# ## 2.3 Players

# In[13]:


all_players= read_json_file('notebooks/players.json')


# In[14]:


players_csv = csv_file(all_players,"players")


# In[15]:


players_csv.head()


# In[16]:


players_csv.tail()


# In[17]:


players_csv.shape


# In[25]:


players_csv.columns


# In[26]:


players_csv.info()

