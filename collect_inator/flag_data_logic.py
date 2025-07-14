import pandas as pd

def clean_df(df: pd.DataFrame) -> pd.DataFrame:
   df["beneficiary"] = df["beneficiary"].apply(clean_beneficiary)
   return df

def clean_beneficiary(b: str):
   if b == None: return None

   clean_b = b.strip()
   try:
      return int(clean_b)
   except:  
      return None