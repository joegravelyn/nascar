import pandas as pd

def json_to_df(json: dict | list | object) -> pd.DataFrame:
   races = []
   for series in json: # type: ignore
      races += json[series] # type: ignore
   df = pd.DataFrame(races)
   return df