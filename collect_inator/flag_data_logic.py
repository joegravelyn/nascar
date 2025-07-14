import pandas as pd

def json_to_df(json: object) -> pd.DataFrame:
   df = pd.DataFrame(json) # type: ignore
   df["beneficiary"] = df["beneficiary"].apply(clean_beneficiary)
   return df

def clean_beneficiary(b: str):
   if b == None: return None

   clean_b = b.strip()
   try:
      return int(clean_b)
   except:  
      return None