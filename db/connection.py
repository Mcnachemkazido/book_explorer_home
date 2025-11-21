


def get_connection(connection_director,details):
    return connection_director.connect(user=details.user,passwd=details.password,
                           host=details.host,database=details.database)



