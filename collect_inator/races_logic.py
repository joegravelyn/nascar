import pandas as pd

def json_to_df(json: dict | list | object, year: int) -> dict[str, pd.DataFrame]:
   df = pd.DataFrame(json) # type: ignore
   # may not be needed, but a good reminder to check
   # df[["year"]] = [year]
   return {"races": df}

   # races = []
   # for series in json: # type: ignore
   #    races += json[series] # type: ignore
   # df = pd.DataFrame(races)
   # return df