from toolbox.nascar_api import Feeds, get_api_data
from sqlalchemy import Engine 
import pandas as pd
from .live_ops_logic import json_to_df

def get_live_ops(url_header: str, sql_engine: Engine | None = None, load_to_sql: bool = True) -> tuple[bool, pd.DataFrame]:
   api_result = get_api_data(Feeds.Live_Ops, {}, url_header=url_header)

   if api_result["result"]:
      df = json_to_df(api_result["json"])

      if load_to_sql:
         if sql_engine == None: return (False, pd.DataFrame())
         existing_df = pd.read_sql_table(table_name="live_ops", con=sql_engine, schema="nascar")
         df = pd.concat([df, existing_df])
         df.drop_duplicates().to_sql("live_ops", con=sql_engine, if_exists="append", index=False)

      return (True, df)
   else:
      print(f"API call failed for Feeds.Live_Ops. URL response code = {api_result["result_code"]}")
      return (False, pd.DataFrame())