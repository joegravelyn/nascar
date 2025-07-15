import pandas as pd

def json_to_df(json: dict | list | object, series_id: int, race_id: int) -> dict[str, pd.DataFrame]:
   df = pd.DataFrame(json) # type: ignore
   # may not be needed, but a good reminder to check
   # df[["series_id", "race_id"]] = [series_id, race_id]
   return {"live_points": df}