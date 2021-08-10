from MySQLCommand.CreateConnection import connect


def get_Churches_counter(name, region):
    name1 = name.rstrip()
    name1 = ''.join(map(str, name1))
    connection = connect()
    query = "select church from catalog_of_metrics  where village regexp  (%s) and province regexp  (%s)"
    cursor = connection.cursor()
    cursor.execute(query, (('.*?\\' + name1 + '\\b.*?'), ('.*?\\' + region + '\\b.*?')))
    result = cursor.fetchall()
    churches = []
    for item in result:
        churches.append(item)
    cursor.close()
    connection.close()
    return len(list(set(churches)))
