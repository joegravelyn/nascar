# Credit to https://github.com/ooohfascinating/NascarApi/tree/main for starting point

from dataclasses import dataclass
import pandas as pd
import requests
from enum import Enum

@dataclass
class Feed:
   url: str
   params: list[str]


class Feeds(Enum):
   Tracks = Feed("https://cf.nascar.com/data/cacher/production/tracks.json", [])
   Live_Ops = Feed("https://cf.nascar.com/live-ops/live-ops.json", [])
   # per year
   Race_List = Feed("https://cf.nascar.com/cacher/|year|/race_list_basic.json", ["year"])
   # per year and series
   Schedule = Feed("https://cf.nascar.com/cacher/|year|/|series_id|/schedule-feed.json", ["year", "series_id"])
   Current_Points = Feed("https://cf.nascar.com/cacher/|year|/|series_id|/points-feed.json", ["year", "series_id"])
   Owner_Points = Feed("https://cf.nascar.com/cacher/|year|/|series_id|/final/|series_id|-owners-points.json", ["year", "series_id"])
   Drivers_Feed = Feed("https://cf.nascar.com/cacher/|year|/|series_id|/drivers-combined-feed-v2.json", ["year", "series_id"])
   Playoffs_Round_0 = Feed("https://cf.nascar.com/data/cacher/production/|year|/|series_id|/playoffs/round_0.json", ["year", "series_id"])
   Playoffs_Round_1 = Feed("https://cf.nascar.com/data/cacher/production/|year|/|series_id|/playoffs/round_1.json", ["year", "series_id"])
   Playoffs_Round_2 = Feed("https://cf.nascar.com/data/cacher/production/|year|/|series_id|/playoffs/round_2.json", ["year", "series_id"])
   Playoffs_Round_3 = Feed("https://cf.nascar.com/data/cacher/production/|year|/|series_id|/playoffs/round_3.json", ["year", "series_id"])
   Playoffs_Round_4 = Feed("https://cf.nascar.com/data/cacher/production/|year|/|series_id|/playoffs/round_4.json", ["year", "series_id"])
   # per race live feeds
   Flag_Data = Feed("https://cf.nascar.com/live/feeds/series_|series_id|/|race_id|/live-flag-data.json", ["series_id", "race_id"])
   Live_Feed = Feed("https://cf.nascar.com/live/feeds/series_|series_id|/|race_id|/live_feed.json", ["series_id", "race_id"])
   Live_Points = Feed("https://cf.nascar.com/live/feeds/series_|series_id|/|race_id|/live_points.json", ["series_id", "race_id"])
   # per race
   Pit_Stops = Feed("https://cf.nascar.com/cacher/|year|/|series_id|/|race_id|/live-pit-data.json", ["year", "series_id", "race_id"])
   Lap_Times = Feed("https://cf.nascar.com/cacher/|year|/|series_id|/|race_id|/lap-times.json", ["year", "series_id", "race_id"])
   Race_Results = Feed("https://cf.nascar.com/cacher/|year|/|series_id|/|race_id|/raceResults.json", ["year", "series_id", "race_id"])
   Lap_Notes = Feed("https://cf.nascar.com/cacher/|year|/|series_id|/|race_id|/lap-notes.json", ["year", "series_id", "race_id"])
   Snaps = Feed("https://cf.nascar.com/cacher/|year|/|series_id|/|race_id|/snappytv.json", ["year", "series_id", "race_id"])
   Weekend_Feed = Feed("https://cf.nascar.com/cacher/|year|/|series_id|/|race_id|/weekend-feed.json", ["year", "series_id", "race_id"])
   Lap_Averages = Feed("https://cf.nascar.com/cacher/|year|/|series_id|/|race_id|/lap-averages.json", ["year", "series_id", "race_id"])
   Box_Score = Feed("https://cf.nascar.com/loopstats/prod/|year|/|series_id|/|race_id|.json", ["year", "series_id", "race_id"])


def get_api_data(feed: Feeds, params: dict[str, int], url_header: str) -> dict[str, str | bool | int | dict | list | object]:
   request_url = feed.value.url
   for p in feed.value.params:
      request_url = request_url.replace(f"|{p}|", str(params[p]))

   response = requests.get(request_url, url_header)

   return {
      "request": request_url, 
      "result": response.status_code == 200, 
      "result_code": response.status_code, 
      "json": response.json() if response.status_code == 200 else None
   }