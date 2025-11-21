import pymysql
import config


def get_connection():
    coon = pymysql.connect(user=config.user,passwd=config.password,
                           host=config.host,database=config.database)
    return coon.cursor()



