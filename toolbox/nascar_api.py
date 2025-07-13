# Credit to https://github.com/ooohfascinating/NascarApi/tree/main for starting point

import pandas as pd
import requests
from enum import Enum

class Feeds(Enum):
   Tracks = "https://cf.nascar.com/data/cacher/production/tracks.json"
   Live_Ops = "https://cf.nascar.com/live-ops/live-ops.json"
   # per year
   Race_List = "https://cf.nascar.com/cacher/|year|/race_list_basic.json"
   # per year and series
   Schedule = "https://cf.nascar.com/cacher/|year|/|series_id|/schedule-feed.json"
   Current_Points = "https://cf.nascar.com/cacher/|year|/|series_id|/points-feed.json"
   Owner_Points = "https://cf.nascar.com/cacher/|year|/|series_id|/final/|series_id|-owners-points.json"
   Drivers_Feed = "https://cf.nascar.com/cacher/|year|/|series_id|/drivers-combined-feed-v2.json"
   Playoffs_Round_0 = "https://cf.nascar.com/data/cacher/production/|year|/|series_id|/playoffs/round_0.json"
   Playoffs_Round_1 = "https://cf.nascar.com/data/cacher/production/|year|/|series_id|/playoffs/round_1.json"
   Playoffs_Round_2 = "https://cf.nascar.com/data/cacher/production/|year|/|series_id|/playoffs/round_2.json"
   Playoffs_Round_3 = "https://cf.nascar.com/data/cacher/production/|year|/|series_id|/playoffs/round_3.json"
   Playoffs_Round_4 = "https://cf.nascar.com/data/cacher/production/|year|/|series_id|/playoffs/round_4.json"
   # per race - occasionally with year and/or series as well
   Flag_Data = "https://cf.nascar.com/live/feeds/series_|series_id|/|race_id|/live-flag-data.json"
   Live_Feed = "https://cf.nascar.com/live/feeds/series_|series_id|/|race_id|/live_feed.json"
   Live_Points = "https://cf.nascar.com/live/feeds/series_|series_id|/|race_id|/live_points.json"
   Live_Pit_Stops = "https://cf.nascar.com/cacher/|year|/|series_id|/|race_id|/live-pit-data.json"
   Lap_Times = "https://cf.nascar.com/cacher/|year|/|series_id|/|race_id|/lap-times.json"
   Race_Results = "https://cf.nascar.com/cacher/|year|/|series_id|/|race_id|/raceResults.json"
   Lap_Notes = "https://cf.nascar.com/cacher/|year|/|series_id|/|race_id|/lap-notes.json"
   Snaps = "https://cf.nascar.com/cacher/|year|/|series_id|/|race_id|/snappytv.json"
   Weekend_Feed = "https://cf.nascar.com/cacher/|year|/|series_id|/|race_id|/weekend-feed.json"
   Lap_Averages = "https://cf.nascar.com/cacher/|year|/|series_id|/|race_id|/lap-averages.json"
   Box_Score = "https://cf.nascar.com/loopstats/prod/|year|/|series_id|/|race_id|.json"


def get_data(feed: Feeds, url_header: str, year: int = 0, series_id: int = 0, race_id: int = 0) -> tuple[bool, int, pd.DataFrame]:
   result = False
   response = requests.get(feed.value.replace("|year|", str(year)).replace("|series_id|", str(series_id)).replace("|race_id|", str(race_id)), url_header)

   if response.status_code == 200:
      result = True
      result_df = pd.DataFrame(response.json())
   else:
      result_df = pd.DataFrame()

   return (result, response.status_code, result_df)
