from toolbox import nascar_config
import collect_inator

schedule = collect_inator.get_schedule(url_header=nascar_config.url_user_header, year=2025, series_id=1, sql_engine=nascar_config.mysql_engine
                            #, load_to_sql=False
                            )
#print(schedule[1])
flags = collect_inator.get_flag_data(url_header=nascar_config.url_user_header, series_id=1, race_id=5569, sql_engine=nascar_config.mysql_engine
                             #, load_to_sql=False
                             )
#print(flags[1])
