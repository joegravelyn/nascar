import collect_inator.get_flag_data
from toolbox import nascar_config
import collect_inator

collect_inator.get_race_schedule(nascar_config.url_user_header, nascar_config.mysql_engine, year=2025, series_id=1)#, print_instead_of_load=True)
collect_inator.get_flag_data(nascar_config.url_user_header, nascar_config.mysql_engine, series_id=1, race_id=5569)#, print_instead_of_load=True)