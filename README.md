# data-analysts-full-project-adalab

Data for these exercises will be extracted from the API https://www.balldontlie.io/home.html#introduction
(Basketball database). It doesn't require registration nor API Key.

## Data ingestion: 
Create a python script that will retrieve data from the API and will store it as files in the local filesystem.

#### Exercise 1: 
Get all teams. https://www.balldontlie.io/home.html#get-all-teams
Bear in mind pagination. It is possible to pass additional arguments to the API call. Example:
```
params_arg = {'player_ids[]': [170, 237, 115], 'season': 2014}
r = requests.get('https://www.balldontlie.io/api/v1/season_averages', params=params_arg)
```

#### Exercise 2: 
It is required to obtain all matches of the 1991-1992 season. No need to rename/remove fields from the response.


#### Output/ Deliverables:
- Create one reusable (shared across exercises) python function called `paginate_api_calls` that will handle the pagination of the API. It will accept two arguments (url, parameters)
- Create one reusable python function that will write to disk
- Exercise 1: One JSON file containing all teams in the folder `/data/teams`. Each row in this file will represent one API call
- Exercise 2: One JSON file per match in the folder `/data/matches`
- Pagination must be dynamic. i.e. control pagination until the end.
- Git repository must not contain any JSON files


Key Points:
- Pagination. Each API call contains metadata that you can use to control it. I recommend to use the attribute `next_page`

`'meta': {'total_pages': 2, 'current_page': 1, 'next_page': 2, 'per_page': 30, 'total_count': 45}`

- Iteration
- API Search/Query: Read the docs carefully

#### Tools:
- Python / Jupyter
- requests https://pypi.org/project/requests/
- JSON https://docs.python.org/es/3/library/json.html


## Data transformation: 
Create a python script that will convert the previously generated JSON files into flattened CSV files.
Alternatively, this exercise can be done with Penthaho Community Edition.
