from toolbox.nascar_api import Feeds, get_api_data
from sqlalchemy import Engine 
import pandas as pd

def get_tracks(url_header: str, sql_engine: Engine, load_to_sql: bool = True) -> tuple[bool, pd.DataFrame]:
   api_result = get_api_data(Feeds.Tracks, {}, url_header=url_header)

   if api_result[0]:
      df = api_result[2]

      # cleaning logic goes here if needed

      if load_to_sql:
         exist_df = pd
         df.to_sql("tracks", con=sql_engine, if_exists="append", index=False)

      return (True, df)
   else:
      print(f"API call failed for Feeds.Tracks. URL response code = {api_result[1]}")
      return (False, pd.DataFrame())