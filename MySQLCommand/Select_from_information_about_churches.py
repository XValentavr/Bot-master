from MySQLCommand.CreateConnection import connect
def SelectOperation(name, current_church, current_region):
    metric = []
    new_church = current_church.rstrip()
    new_church = ''.join(map(str, new_church))
    connection = connect()
    query = "select archive.Name, church,birth,wedding,divorce, death,testament,additional from catalog_of_metrics left join archive archive on archive.number_of_archive = catalog_of_metrics.number_of_archive where church regexp  (%s) and church regexp(%s)  and church regexp(%s)"
    cursor = connection.cursor()
    cursor.execute(query, (('.*?\\' + name + '\\b.*?'), ('.*?\\'+new_church+'\\b.*?'), ('.*?\\'+current_region+'\\b.*?')))
    result = cursor.fetchall()
    for item in result:
        metric.append(item)
    cursor.close()
    connection.close()
    return metric
