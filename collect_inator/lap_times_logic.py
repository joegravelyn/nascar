import pandas as pd

def json_to_df(json: dict | list | object, year: int, series_id: int, race_id: int) -> dict[str, pd.DataFrame]:
   lap_times_laps = pd.DataFrame(json["laps"]) # type: ignore
   lap_times_laps = lap_times_laps.explode("Laps", ignore_index=True)

   driver_laps = pd.json_normalize(lap_times_laps["Laps"]) # type: ignore

   lap_times_laps = lap_times_laps.join(driver_laps, rsuffix="_lap")
   lap_times_laps = lap_times_laps.drop("Laps", axis=1)
   lap_times_laps = lap_times_laps.rename(columns={
      "Number": "car_number",
      "FullName": "driver_full_name",
      "Manufacturer": "mfr",
      "RunningPos": "finish_pos",
      "NASCARDriverID": "driver_id",
      "Lap": "lap_number",
      "LapTime": "lap_time",
      "LapSpeed": "lap_speed",
      "RunningPos_lap": "running_pos"
      })
   lap_times_laps[["year", "series_id", "race_id"]] = [year, series_id, race_id]


   
   lap_times_flags = pd.DataFrame(json["flags"]) # type: ignore
   lap_times_flags = lap_times_flags.rename(columns={
      "LapsCompleted": "lap_number",
      "FlagState": "flag_state"
      })
   lap_times_flags[["year", "series_id", "race_id"]] = [year, series_id, race_id]


   return {"lap_times_laps": lap_times_laps, "lap_times_flags": lap_times_flags}