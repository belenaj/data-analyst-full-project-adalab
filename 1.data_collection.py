#!/usr/bin/env python
# coding: utf-8

# # 1. Data collection

# ### Output/Deliverables:
# - For each exercise, a notebook in the folder notebooks/ must be commited
# - Create one reusable (shared across exercises) python function called paginate_api_calls that will handle the pagination of the API. - It will accept two arguments (url, parameters)
# - Create one reusable python function called write_json_file that will write the responses to disk
# - Exercise 1: One JSON file containing all teams in the folder /data/teams. Each row in this file will represent one API response. You can find an example in sample/data/teams.json
# - Exercise 2: One JSON file containing all games in the folder /data/games. Each row in this file will represent one API response. You can find an example in sample/data/games.json
# - Exercise 3: One JSON file containing all players in the folder /data/players. Each row in this file will represent one API response. You can find an example in sample/data/players.json
# - Pagination must be dynamic. i.e. control pagination until the end.
# - Git repository must not contain any JSON/CSV files
# 
# ### Key Points:
# - Pagination. Each API call contains metadata that you can use to control it. I recommend to use the attribute next_page 'meta': {'total_pages': 2, 'current_page': 1, 'next_page': 2, 'per_page': 30, 'total_count': 45}
# - Reducing the number of API calls to the maximum. There is a parameter to increase the number of items retrieved in each API call. By modifying it, you can reduce the total number of API Calls
# - API Search/Query: Read the docs carefully

# In[1]:


pip install ipykernel


# In[2]:


# request
# ==============================================================================
import requests

# Data processing
# ==============================================================================
import pandas as pd
import numpy as np
import json

#Allows us to display more than one output per cell
# ==============================================================================
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all" 

# Display all columns
# ==============================================================================
pd.options.display.max_columns = None


# `` Create one reusable (shared across exercises) python function called paginate_api_calls that will handle the pagination of the API. It will accept two arguments (url, parameters) ``

# In[3]:


# The above code is creating a function that is going to be used to paginate the API calls.

def paginate_api_calls(url, params): # You must give the url and the params as a dictionary

    params.setdefault("page",1) #

 # To call the API
    response = requests.get(url, params)
    
    if "meta" in response.json().keys(): # The API call can contain metadata as meta or not.

        meta = response.json()["meta"]
        next_page= meta["next_page"]
        results=[]

        # This is a while loop that is going to iterate through the pages of the API.
        while next_page != None :

            response = requests.get(url, params)
            results.append(response.json())
            next_page = response.json()["meta"]["next_page"]
            
            params["page"] += 1
        
        return results

    # This is a condition that is going to be used if the API call does not have metadata for pagination.
    else:
       
        print("There is not page parameter")
        results =response.json()

        return results


# In[4]:


# To obtein information abour the status of the API call

def check_api_call(url,params):

 # To call the API
    response = requests.get(url, params)
    status_code = response.status_code
    reason_status = response.reason
    
    meta = response.json()["meta"]
    next_page= meta["next_page"]
    results=[]

        # This is a while loop that is going to iterate through the pages of the API.
    while next_page != None :

        response = requests.get(url, params)
        status_code = response.status_code
        reason_status = response.reason
        results.append(response.json())
        next_page = response.json()["meta"]["next_page"]
        
        params["page"] += 1

        if status_code == 200:
            print('The request was successful, the status code was returned:',status_code,' and as reason for the status code:',reason_status)
        elif status_code == 402:
            print('User could not be authorised, status code returned:', status_code,' and as reason for the status code: ',reason_status)
        elif status_code == 404:
            print('Something went wrong, the resource was not found, the status code was returned:', status_code,' and as reason for the status code: ',reason_status)
        else:
            print('Something unexpected has happened, the status code has been returned:', status_code,' and as reason for the status code: ',reason_status)

    return f'There are {meta["current_page"]} pages. The status of the request is {status_code} and the reason of the state {reason_status}.'


# ``Create one reusable python function called write_json_file that will write the responses to disk``

# In[5]:


# The above code is taking the results from the API call and writing them to a json file.
def write_json_file(results, name_of_file): # You must give the result of the API call and the ubi and name of the file that will be created as a string

    for i in results:

        if len(results) <= 1:
            print("There is only one page")

        else:
            call = json.dumps(i)
            with open(name_of_file+".json", "a") as outfile:
                outfile.write(call + "\n" )

    return "Se ha creado el archivo:", name_of_file+".json"


# ## Exercise 1.1: Get all teams. 
# - https://www.balldontlie.io/home.html#get-all-teams
# - Bear in mind pagination. It is possible to pass additional arguments to the API call.

# In[6]:


# url and params to the API call
teams_url = 'https://www.balldontlie.io/api/v1/teams'
teams_params = {} # It must be a dictionary


# In[7]:


# Function to the API call
teams = paginate_api_calls(teams_url, teams_params)


# In[8]:


check_api_call(teams_url,teams_params)


# In[9]:


teams


# In[10]:


all_teams = write_json_file(teams,"notebooks/teams")


# In[11]:


all_teams


# ## Exercise 1.2
# - It is required to obtain all games of the 1991-1992 season. No need to rename/remove fields from the response.

# In[12]:


# url and params to the API call
games_url = 'https://www.balldontlie.io/api/v1/games'
games_params= {'seasons[]': 1991, "per_page":100} # It must be a dictionary


# In[13]:


# Function to the API call
games = paginate_api_calls(games_url, games_params)


# In[14]:


check_api_call(games_url,games_params)


# In[15]:


games


# In[16]:


all_games_1991 = write_json_file(games,"notebooks/games")


# ## Exercise 1.3
# - It is required to obtain all players. No need to rename/remove fields from the response.

# In[17]:


# url and params to the API call
players_url = 'https://www.balldontlie.io/api/v1/players'
players_params= {"per_page":100} # It must be a dictionary


# In[18]:


# Function to the API call
players = paginate_api_calls(players_url, players_params)


# In[19]:


check_api_call(players_url,players_params)


# In[20]:


players


# In[21]:


all_players = write_json_file(players,"notebooks/players")


# In[22]:


print(all_players)

