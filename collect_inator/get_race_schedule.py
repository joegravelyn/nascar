from toolbox import nascar_api
from datetime import date
from sqlalchemy import Engine 

def get_race_schedule(url_header: str, sql_engine: Engine, series_id: int, year: int = date.today().year, print_instead_of_load: bool = False):
   api_result = nascar_api.get_data(nascar_api.Feeds.Schedule, url_header=url_header, year=year, series_id=series_id)
   if api_result[0]:
      df = api_result[2]

      # cleaning logic goes here if needed

      if print_instead_of_load:
         print("Printing schedule data instead of loading...")
         print(df)
      else:
         df.to_sql("schedule", con=sql_engine, if_exists="append", index=False)
         print(f"Schedule data loaded for year={year} and series_id={series_id}")
   else:
      print(f"API call failed. URL response code = {api_result[1]}")