import pymysql


def get_connection(user_name ,entry_password,host_run ,database_run):
    return pymysql.connect(user=user_name,password=entry_password,host=host_run,database=database_run)



