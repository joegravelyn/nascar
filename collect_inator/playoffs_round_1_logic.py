import pandas as pd

def json_to_df(json: dict | list | object, year: int, series_id: int) -> dict[str, pd.DataFrame]:
   df = pd.DataFrame(json) # type: ignore
   # may not be needed, but a good reminder to check
   # df[["year", "series_id"]] = [year, series_id]
   return {"playoffs_round_1": df}