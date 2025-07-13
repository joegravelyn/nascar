from dataclasses import dataclass
from datetime import datetime

@dataclass
class RaceEvent:
   event_name: str
   notes: str
   start_time_utc: datetime
   run_type: int