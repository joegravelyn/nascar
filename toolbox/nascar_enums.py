from enum import Enum
from typing import Any

class Series(Enum):
   UNKNOWN = 0
   Cup = 1
   Xfinity = 2
   Truck = 3
   ARCA = 4

   @classmethod
   def _missing_(cls, value: object) -> Any:
      return Series.UNKNOWN

class RaceType(Enum):
   UNKNOWN = 0
   PointsRace = 1
   Exhibition = 2

   @classmethod
   def _missing_(cls, value: object) -> Any:
      return RaceType.UNKNOWN