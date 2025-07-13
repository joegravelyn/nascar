from toolbox import Race
import pandas as pd
import requests
from datetime import date
from sqlalchemy import Engine 

def get_race_list(url_header: str, sql_engine: Engine, year: int = date.today().year):
   response = requests.get(f"https://cf.nascar.com/cacher/{year}/race_list_basic.json", url_header)
   if response.status_code == 200: 
      races: list[Race] = []
      race_list = response.json()

      # Loop through top element (series) in response json
      for series in race_list:
         races += [Race.from_dict(race) for race in race_list[series]]

      races_df = pd.DataFrame(races)
      races_df.to_sql("races", con=sql_engine, if_exists="append", index=False)
      print(f"Data loaded for year = {year}")
   else:
      print(f"Data not loaded. URL response code = {response.status_code}")