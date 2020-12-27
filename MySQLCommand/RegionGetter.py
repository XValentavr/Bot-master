from MySQLCommand.CreateConnection import connect


def get_Region(name):
    region = []
    connection = connect()
    query = "select church from catalog_of_metrics  where church regexp  (%s)"
    cursor = connection.cursor()
    cursor.execute(query, (('.*?\\'+name+'\\b.*?'),))
    result = cursor.fetchall()
    for i in result:
        region.append(i)
    cursor.close()
    connection.close()
    return region

