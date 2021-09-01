from MySQLCommand.CreateConnection import connect


def SelectOperation(name, current_province):
    name = ''.join(map(str, name.rstrip()))
    metrics = []
    connection = connect()

    query = "select archive.Name, province,eparchy,county,church, birth, wedding, divorce, death, testament, additional, religion from catalog_of_metrics  left join archive archive on archive.num = catalog_of_metrics.archive where village regexp(%s) and province regexp(%s)"
    cursor = connection.cursor()
    cursor.execute(query, (('.*?\\' + name + '\\b.*?'), ('.*?\\' + current_province + '\\b.*?'),))
    result = cursor.fetchall()
    for item in result:
        metrics.append(item)
    cursor.close()
    connection.close()
    new_metrics = []
    for i in metrics:
        if i not in new_metrics:
            new_metrics.append(i)
    return new_metrics
