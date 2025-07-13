import configparser
from pathlib import Path
import mysql.connector

#confirm = input("This will delete the entire database and recreate it. If you want to proceed, enter \"confirm\": ")
confirm = "confirm"

if confirm.lower() == "confirm":

   config = configparser.ConfigParser()
   config.read(Path.cwd().joinpath("config.ini"))

   mydb = mysql.connector.connect(
      host=config["mysql"]["host"],
      user=config["mysql"]["user"],
      password=config["mysql"]["password"])

   mycursor = mydb.cursor()

   mycursor.execute("DROP DATABASE IF EXISTS nascar;")
   mycursor.execute("CREATE DATABASE nascar;")
   mydb.database = "nascar" # type: ignore

   for script in Path.cwd().joinpath("mysql_db", "sql_scripts").glob("*.sql"):
      print(f"Running script in {script}")
      sql = script.read_text()
      print(sql)
      mycursor.execute(sql)