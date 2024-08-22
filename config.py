import psycopg2
from configparser import ConfigParser

config = ConfigParser()
config.load('conf.ini')

host = config['DataBase']['host']
db_name = config['DataBase']['db_name']
user = config['DataBase']['user']
password = config['DataBase']['password']
port = config['DataBase']['port']