import configparser
from sqlalchemy import create_engine

config = configparser.ConfigParser()
config.read("config.ini")

url_user_header = config["url_request"]["user_header"]

mysql_engine = create_engine(f"mysql+mysqlconnector://{config["mysql"]["user"]}:{config["mysql"]["password"]}@{config["mysql"]["host"]}/nascar")


if __name__ == "__main__":
   print(url_user_header)