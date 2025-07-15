import pandas as pd

def json_to_df(json: dict | list | object, series_id: int, race_id: int) -> dict[str, pd.DataFrame]:
   df = pd.DataFrame(json) # type: ignore
   df["beneficiary"] = df["beneficiary"].apply(clean_beneficiary)
   return {"flags": df}

def clean_beneficiary(b: str):
   if b == None: return None

   clean_b = b.strip()
   try:
      return int(clean_b)
   except:  
      return None