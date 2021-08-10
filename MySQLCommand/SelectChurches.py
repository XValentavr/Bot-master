from MySQLCommand.CreateConnection import connect


def get_Churches(name, region):
    name1 = name.rstrip()
    name1 = ''.join(map(str, name1))
    churches = []
    connection = connect()
    query = "select church from catalog_of_metrics  where village regexp  (%s)and province regexp  (%s)"
    cursor = connection.cursor()
    cursor.execute(query, (('.*?\\' + name1 + '\\b.*?'), ('.*?\\' + region + '\\b.*?'),))
    result = cursor.fetchall()
    for item in result:
        churches.append(item)
    cursor.close()
    connection.close()
    new_churches = []
    for i in churches:
        if i not in new_churches:
            new_churches.append(i)
    return new_churches
