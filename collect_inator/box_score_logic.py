import pandas as pd

def json_to_df(json: dict | list | object, year: int, series_id: int, race_id: int) -> dict[str, pd.DataFrame]:
   df = pd.DataFrame(json) # type: ignore
   # may not be needed, but a good reminder to check
   # df[["year", "series_id", "race_id"]] = [year, series_id, race_id]
   return {"box_score": df}