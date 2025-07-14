from toolbox.nascar_api import Feeds, get_api_data
from sqlalchemy import Engine 
import pandas as pd

def get_race_list(url_header: str, year: int, sql_engine: Engine, load_to_sql: bool = True) -> tuple[bool, pd.DataFrame]:
   api_result = get_api_data(Feeds.Race_List, {"year": year}, url_header=url_header)

   if api_result[0]:
      df = api_result[2]

      # cleaning logic goes here if needed

      if load_to_sql:
         exist_df = pd
         df.to_sql("race_list", con=sql_engine, if_exists="append", index=False)

      return (True, df)
   else:
      print(f"API call failed for Feeds.Race_List. URL response code = {api_result[1]}")
      return (False, pd.DataFrame())