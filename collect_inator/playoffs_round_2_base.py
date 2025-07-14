from toolbox.nascar_api import Feeds, get_api_data
from sqlalchemy import Engine 
import pandas as pd
from .playoffs_round_2_logic import clean_df

def get_playoffs_round_2(url_header: str, year: int, series_id: int, sql_engine: Engine | None = None, load_to_sql: bool = True) -> tuple[bool, pd.DataFrame]:
   api_result = get_api_data(Feeds.Playoffs_Round_2, {"year": year, "series_id": series_id}, url_header=url_header)

   if api_result[0]:
      df = api_result[2]

      df = clean_df(df)

      if load_to_sql:
         if sql_engine == None: return (False, pd.DataFrame())
         existing_df = pd.read_sql_table(table_name="playoffs_round_2", con=sql_engine, schema="nascar")
         df = pd.concat([df, existing_df])
         df.drop_duplicates().to_sql("playoffs_round_2", con=sql_engine, if_exists="append", index=False)

      return (True, df)
   else:
      print(f"API call failed for Feeds.Playoffs_Round_2. URL response code = {api_result[1]}")
      return (False, pd.DataFrame())