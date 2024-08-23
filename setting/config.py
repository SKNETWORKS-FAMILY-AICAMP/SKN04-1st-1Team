from configparser import ConfigParser

config = ConfigParser()
config.read('./setting/conf.ini', encoding='utf-8')

HOST     = config['DataBase']['host']
DB_NAME  = config['DataBase']['db_name']
USER     = config['DataBase']['user']
PASSWORD = config['DataBase']['password']
PORT     = config['DataBase']['port']