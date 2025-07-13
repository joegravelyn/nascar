from toolbox import nascar_api
from sqlalchemy import Engine 

def get_flag_data(url_header: str, sql_engine: Engine, series_id: int, race_id: int, print_instead_of_load: bool = False):
   api_result = nascar_api.get_data(nascar_api.Feeds.Flag_Data, url_header=url_header, series_id=series_id, race_id=race_id)
   if api_result[0]:
      df = api_result[2]

      # cleaning logic goes here if needed
      df["beneficiary"] = df["beneficiary"].apply(clean_beneficiary)

      if print_instead_of_load:
         print("Printing flag data instead of loading...")
         print(df)
      else:
         df.to_sql("flags", con=sql_engine, if_exists="append", index=False)
         print(f"Flag data loaded for series_id={series_id} and race_id={race_id}")
   else:
      print(f"API call failed. URL response code = {api_result[1]}")

def clean_beneficiary(b: str):
   if b == None: return None

   clean_b = b.strip()
   try:
      return int(clean_b)
   except:  
      return None