from toolbox import nascar_config
from collect_inator import get_race_list

get_race_list(nascar_config.url_user_header, nascar_config.mysql_engine, 2025)