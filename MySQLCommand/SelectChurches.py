from MySQLCommand.CreateConnection import connect


def get_Churches(name, region):
    name1 = name.rstrip()
    name1 = ''.join(map(str, name1))
    churches = []
    connection = connect()
    query = "select church from catalog_of_metrics  where church regexp  (%s)and church regexp  (%s)"
    cursor = connection.cursor()
    cursor.execute(query, (('.*?\\' + name1 + '\\b.*?'), ('.*?\\' + region + '\\b.*?'),))
    result = cursor.fetchall()
    for item in result:
        churches.append(item)
    cursor.close()
    connection.close()
    return churches
