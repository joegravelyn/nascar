import pandas as pd

def json_to_df(json: object) -> pd.DataFrame:
   df = pd.DataFrame(json) # type: ignore
   return df