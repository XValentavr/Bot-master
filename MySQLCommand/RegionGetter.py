'''
from MySQLCommand.CreateConnection import connect


def get_Region(name):
    connection = connect()
    query = "select church from catalog_of_metrics  where county regexp  (%s)"
    cursor = connection.cursor()
    cursor.execute(query, (('.*?\\' + name + '\\b.*?'),))
    result = cursor.fetchall()
    region = [reg for reg in result]
    cursor.close()
    connection.close()
    return region
'''
