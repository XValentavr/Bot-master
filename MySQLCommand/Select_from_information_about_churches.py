from MySQLCommand.CreateConnection import connect


def SelectOperation(current_church, current_village, current_region):
    new_village = ''.join(map(str, current_village.rstrip()))
    connection = connect()
    print(current_church)
    print(current_village)
    print(current_region)
    query = "select archive.Name, church,birth,wedding,divorce, death,testament,additional " \
            "from catalog_of_metrics left join archive archive on archive.num = catalog_of_metrics.archive where church regexp  (%s) and village regexp(%s)  and county regexp(%s)"
    cursor = connection.cursor()
    cursor.execute(query, (
        ('.*?\\' + current_church + '\\b.*?'), ('.*?\\' + new_village + '\\b.*?'),
        ('.*?\\' + current_region + '\\b.*?'),))
    result = cursor.fetchall()
    metric = [churches for churches in result]
    cursor.close()
    connection.close()
    return metric
