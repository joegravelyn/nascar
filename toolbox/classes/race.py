from dataclasses import dataclass

@dataclass
class Race:
   race_id: int
   master_race_id: int
   series_id: int
   season: int
   race_name: str
   track_id: int
   track_name: str

   scheduled_date: str
   scheduled_distance: float
   scheduled_laps: int

   race_type_id: int
   restrictor_plate: bool
   playoff_round: int

   @classmethod
   def from_dict(cls, d):
      return cls(
         race_id = d.get("race_id"),
         master_race_id = d.get("master_race_id"),
         series_id = d.get("series_id"),
         season = d.get("race_season"),
         race_name = d.get("race_name"),
         track_id = d.get("track_id"),
         track_name = d.get("track_name"),

         scheduled_date = d.get("date_scheduled"),
         scheduled_distance = d.get("scheduled_distance"),
         scheduled_laps = d.get("scheduled_laps"),

         race_type_id = d.get("race_type_id"),
         restrictor_plate = d.get("restrictor_plate"),
         playoff_round = d.get("playoff_round", 0),
      )
     

   
   #inspection_complete: bool = field(metadata={"sql": "RaceID"})
   # race_date: str = field(metadata={"sql": ""})
   # qualifying_date: str = field(metadata={"sql": ""})
   # tunein_date: str = field(metadata={"sql": ""})
   # actual_distance: float = field(metadata={"sql": ""})
   # actual_laps: int = field(metadata={"sql": ""})
   # stage_1_laps: int = field(metadata={"sql": ""})
   # stage_2_laps: int = field(metadata={"sql": ""})
   # stage_3_laps: int = field(metadata={"sql": ""})
   # number_of_cars_in_field: int = field(metadata={"sql": ""})
   # pole_winner_driver_id: int = field(metadata={"sql": ""})
   # pole_winner_speed: float = field(metadata={"sql": ""})
   # number_of_lead_changes: int = field(metadata={"sql": ""})
   # number_of_leaders: int = field(metadata={"sql": ""})
   # number_of_cautions: int = field(metadata={"sql": ""})
   # number_of_caution_laps: int = field(metadata={"sql": ""})
   # average_speed: float = field(metadata={"sql": ""})
   # total_race_time: str = field(metadata={"sql": ""})
   # margin_of_victory: str = field(metadata={"sql": ""})
   # race_purse: float = field(metadata={"sql": ""})
   # race_comments: str = field(metadata={"sql": ""})
   # attendance: int = field(metadata={"sql": ""})
   # infractions: list = field(metadata={"sql": ""})
   # schedule: list = field(metadata={"sql": ""})
   # radio_broadcaster: str = field(metadata={"sql": ""})
   # television_broadcaster: str = field(metadata={"sql": ""})
   # satellite_radio_broadcaster: str = field(metadata={"sql": ""})
   # is_qualifying_race: bool = field(metadata={"sql": ""})
   # qualifying_race_no: int = field(metadata={"sql": ""})
   # qualifying_race_id: int = field(metadata={"sql": ""})
   # has_qualifying: bool = field(metadata={"sql": ""})
   # winner_driver_id: int = field(metadata={"sql": ""})
   # pole_winner_laptime: str = field(metadata={"sql": ""})


   
         # race_date = d.get("race_date"),
         # qualifying_date = d.get("qualifying_date"),
         # tunein_date = d.get("tunein_date"),
         # actual_distance = d.get("actual_distance"),
         # actual_laps = d.get("actual_laps"),
         # stage_1_laps = d.get("stage_1_laps"),
         # stage_2_laps = d.get("stage_2_laps"),
         # stage_3_laps = d.get("stage_3_laps"),
         # number_of_cars_in_field = d.get("number_of_cars_in_field"),
         # pole_winner_driver_id = d.get("pole_winner_driver_id"),
         # pole_winner_speed = d.get("pole_winner_speed"),
         # number_of_lead_changes = d.get("number_of_lead_changes"),
         # number_of_leaders = d.get("number_of_leaders"),
         # number_of_cautions = d.get("number_of_cautions"),
         # number_of_caution_laps = d.get("number_of_caution_laps"),
         # average_speed = d.get("average_speed"),
         # total_race_time = d.get("total_race_time"),
         # margin_of_victory = d.get("margin_of_victory"),
         # race_purse = d.get("race_purse"),
         # race_comments = d.get("race_comments"),
         # attendance = d.get("attendance"),
         # infractions = d.get("infractions"),
         # schedule = d.get("schedule"),
         # radio_broadcaster = d.get("radio_broadcaster"),
         # television_broadcaster = d.get("television_broadcaster"),
         # satellite_radio_broadcaster = d.get("satellite_radio_broadcaster"),
         # inspection_complete = d.get("inspection_complete"),
         # is_qualifying_race = d.get("is_qualifying_race"),
         # qualifying_race_no = d.get("qualifying_race_no"),
         # qualifying_race_id = d.get("qualifying_race_id"),
         # has_qualifying = d.get("has_qualifying"),
         # winner_driver_id = d.get("winner_driver_id"),
         # pole_winner_laptime = d.get("pole_winner_laptime")