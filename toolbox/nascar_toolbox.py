import pandas as pd
from datetime import datetime

# conn_str = f"Driver={{{config["sql_server"]["driver"]}}};Server={config["sql_server"]["server"]};Database={config["sql_server"]["database"]};TrustServerCertificate=yes;Trusted_Connection=yes"
# conn_url = sqlalchemy.engine.URL.create("mssql+pyodbc", query={"odbc_connect": conn_str})
# engine = sqlalchemy.create_engine(conn_url)


# # Functions to create empty dataframes with names
# def create_empty_race_metrics_df():
#    return pd.DataFrame(columns=[
#          "SourceFileName"
#       ,  "SeriesShortName"
#       ,  "RaceDate"
#       ,  "TrackName"
#       ,  "RaceName"
#       ,  "MetricName"
#       ,  "MetricValue"])
# def create_empty_entry_metrics_df():
#    return pd.DataFrame(columns=[
#          "SourceFileName"
#       ,  "SourcePageNum"
#       ,  "SourcePageMetric"
#       ,  "SeriesShortName"
#       ,  "RaceDate"
#       ,  "TrackName"
#       ,  "RaceName"
#       ,  "CarNumber"
#       ,  "MetricName"
#       ,  "MetricValue"])
# def create_empty_audit_log_df():
#    return pd.DataFrame(columns=[
#          "LogDate"
#       ,  "SourceFileName"
#       ,  "SourcePageNum"
#       ,  "SourcePageMetric"
#       ,  "SeriesShortName"
#       ,  "RaceDate"
#       ,  "TrackName"
#       ,  "RaceName"
#       ,  "CarNumber"
#       ,  "MetricName"
#       ,  "MetricValue"
#       ,  "LogMessage"]) 


# def get_last_run(process):
#    # Check date of last run to check for updated files
#    etlLog = pd.read_sql_query(sql=f"SELECT MAX(ProcessStart) AS processDate FROM py.EtlLog WHERE Process = '{process}'", con=engine)
#    return etlLog.loc[0, "processDate"]

# def get_data_dir(report_type = None):
#    if report_type == None:
#       if config["data"].getboolean("dir_is_suffix"):
#          return Path.cwd().parent.joinpath(config["data"]["dir"])
#       return Path(config["data"]["dir"])
#    else:
#       if config["data"].getboolean("dir_is_suffix"):
#          return Path.cwd().parent.joinpath(config["data"]["dir"], "Reports", report_type)
#       return Path(config["data"]["dir"]).joinpath(report_type)
   
# # Get the headers found in the dataframe and try to match page column definitions
# def check_for_report_page_definiton(process: str, report_columns: dict[str, list[tuple[str, str]]], report_file: Path, table_i: int, report_df: pd.DataFrame, first_entry_i: int, audit_log_df: pd.DataFrame) -> dict:
#    results = {"result": False, "found_page": None, "audit_df": None}

#    found_headers_df = report_df[first_entry_i-1 : first_entry_i]

#    for rp, rpc in report_columns.items():
#       test_headers = [c[0] for c in rpc]
#       found_headers = found_headers_df.apply(lambda r: r.to_list() == test_headers, axis=1).any()
#       if found_headers:
#          results["result"] = True
#          results["found_page"] = rp
#          return results

#    if not results["result"]:
#       msg = f"Dataframe column count cannot match any definitions for process {process}. Found: {found_headers_df.to_string()}"
#       results["audit_df"] = add_log_audit_message(audit_log_df
#          ,  log_source_file_name = report_file
#          ,  log_message = msg
#          ,  log_source_page_num = table_i
#          ,  log_source_page_metric = process
#          # ,  log_series_name=series
#          # ,  log_race_date=race_info["race_date"]
#          # ,  log_track_name=race_info["track_name"]
#          # ,  log_race_name=race_info["race_name"]
#          )
#    return results


# def check_report_page_column_count(report_columns, report_type, report_file, table_i, found_columns, audit_log_df):
#    results = {"result": len(found_columns) == len(report_columns[report_type]), "audit_df": None}
#    if not results["result"]:
#       msg = f"Dataframe has unexpected column count.\nExpected: {len(report_columns[report_type])} :: {report_columns[report_type]}\nActual: {len(found_columns)} :: {found_columns}"
#       results["audit_df"] = add_log_audit_message(audit_log_df
#          ,  log_source_file_name = report_file
#          ,  log_message = msg
#          ,  log_source_page_num = table_i
#          ,  log_source_page_metric = report_type
#          # ,  log_series_name=series
#          # ,  log_race_date=race_info["race_date"]
#          # ,  log_track_name=race_info["track_name"]
#          # ,  log_race_name=race_info["race_name"]
#          )
#    return results


# def get_sql_ids(stage_df, sql_table, sql_id, join_columns):
#    columns_plus_id = join_columns.copy()
#    columns_plus_id.append(sql_id)
#    # Get existing IDs and names from SQL
#    existing_df = pd.read_sql_table(table_name=sql_table, con=engine, schema="dbo", columns=columns_plus_id)
#    # Join existing data onto stage df
#    stage_df = stage_df.merge(existing_df, how="left", on=join_columns, suffixes=(None, "_existing"))
#    return {"stage": stage_df, "existing": existing_df}

# def catch_new_values(stage_df, sql_table, sql_id, join_columns, load_only_columns = None):
#    temp = get_sql_ids(stage_df, sql_table, sql_id, join_columns)
#    # Filter temp to null IDs and load names into SQL
#    load_columns = join_columns.copy()
#    if load_only_columns: load_columns += load_only_columns
#    temp["stage"][temp["stage"][sql_id].isnull()][load_columns].drop_duplicates().to_sql(name=sql_table, con=engine, schema="dbo", if_exists="append", index=False)
#    temp = get_sql_ids(stage_df, sql_table, sql_id, join_columns)
#    return temp


# def get_manufacturers():
#    return pd.read_sql_table(table_name="Manufacturers", con=engine, schema="dbo", columns=["ManufacturerName"])["ManufacturerName"]


# def add_log_audit_message(
#       log_df
#    ,  log_source_file_name
#    ,  log_message
#    ,  log_source_page_num=None
#    ,  log_source_page_metric=None
#    ,  log_series_name=None
#    ,  log_race_date=None
#    ,  log_track_name=None
#    ,  log_race_name=None
#    ,  log_car_number=None
#    ,  log_metric_name=None
#    ,  log_metric_value=None
#    ):

#    return pd.concat([log_df, pd.DataFrame({     
#          "LogDate": [datetime.now()]
#       ,  "SourceFileName": [log_source_file_name]
#       ,  "SourcePageNum": [log_source_page_num]
#       ,  "SourcePageMetric": [log_source_page_metric]
#       ,  "SeriesShortName": [log_series_name]
#       ,  "RaceDate": [log_race_date]
#       ,  "TrackName": [log_track_name]
#       ,  "RaceName": [log_race_name]
#       ,  "CarNumber": [log_car_number]
#       ,  "MetricName": [log_metric_name]
#       ,  "MetricValue": [log_metric_value]
#       ,  "LogMessage": [log_message]
#       })])


# def save_audit_log(log_df):
#    log_df.to_sql(name="AuditLog", con=engine, schema="py", if_exists="append", index=False)