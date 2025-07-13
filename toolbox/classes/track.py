from dataclasses import dataclass
from typing import Optional

@dataclass
class Track:
   track_id: int
   track_name: Optional[str] = ""