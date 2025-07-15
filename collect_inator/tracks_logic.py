import pandas as pd

def json_to_df(json: dict | list | object) -> dict[str, pd.DataFrame]:
   df = pd.DataFrame(json) # type: ignore
   # may not be needed, but a good reminder to check
   # df[[]] = []
   return {"tracks": df}