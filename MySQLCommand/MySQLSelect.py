from MySQLCommand.CreateConnection import connect
def SelectOperation(name, current_church):
    metric = []
    connection = connect()
    query = "select archive.Name, church,birth,wedding,divorce, death,testament,additional from catalog_of_metrics left join archive archive on archive.number_of_archive = catalog_of_metrics.number_of_archive where church regexp  (%s) and church regexp(%s)"
    cursor = connection.cursor()
    cursor.execute(query, (('.*?\\' + name + '\\b.*?'), ('.*?\\'+current_church+'\\b.*?')))
    result = cursor.fetchall()
    global count_of
    for item in result:
        metric.append(item)
    cursor.close()
    connection.close()
    return metric
