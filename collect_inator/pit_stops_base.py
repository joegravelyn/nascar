from toolbox.nascar_api import Feeds, get_api_data
from sqlalchemy import Engine 
import pandas as pd
from .pit_stops_logic import clean_df

def get_pit_stops(url_header: str, year: int, series_id: int, race_id: int, sql_engine: Engine, load_to_sql: bool = True) -> tuple[bool, pd.DataFrame]:
   api_result = get_api_data(Feeds.Pit_Stops, {"year": year, "series_id": series_id, "race_id": race_id}, url_header=url_header)

   if api_result[0]:
      df = api_result[2]

      df = clean_df(df)

      if load_to_sql:
         existing_df = pd.read_sql_table(table_name="pit_stops", con=sql_engine, schema="nascar")
         df = pd.concat([df, existing_df])
         df.drop_duplicates().to_sql("pit_stops", con=sql_engine, if_exists="append", index=False)

      return (True, df)
   else:
      print(f"API call failed for Feeds.Pit_Stops. URL response code = {api_result[1]}")
      return (False, pd.DataFrame())