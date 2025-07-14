from toolbox.nascar_api import Feeds, get_api_data
from sqlalchemy import Engine 
import pandas as pd
from .race_list_logic import clean_df

def get_race_list(url_header: str, year: int, sql_engine: Engine | None = None, load_to_sql: bool = True) -> tuple[bool, pd.DataFrame]:
   api_result = get_api_data(Feeds.Race_List, {"year": year}, url_header=url_header)

   if api_result[0]:
      df = api_result[2]

      df = clean_df(df)

      if load_to_sql:
         if sql_engine == None: return (False, pd.DataFrame())
         existing_df = pd.read_sql_table(table_name="race_list", con=sql_engine, schema="nascar")
         df = pd.concat([df, existing_df])
         df.drop_duplicates().to_sql("race_list", con=sql_engine, if_exists="append", index=False)

      return (True, df)
   else:
      print(f"API call failed for Feeds.Race_List. URL response code = {api_result[1]}")
      return (False, pd.DataFrame())