"""
This module gets data from database if church mod is selected
"""

# local imports
from MySQLCommand.CreateConnection import connect


def select_operation_get_churches(current_church: str, current_village: str, current_region: str) -> list:
    """
    get info from database when church mod is selected
    :param current_church: str
    :param current_village: list
    :param current_region: str
    :return: list
    """
    new_village = ''.join(map(str, current_village.rstrip()))
    connection = connect()
    query = "select archive.Name, province,eparchy,village,county,religion,church,birth,wedding,divorce, death,testament,additional from catalog_of_metrics left join archive archive on archive.num = catalog_of_metrics.archive where church regexp  (%s)and village regexp(%s)  and county regexp(%s)"
    cursor = connection.cursor()
    cursor.execute(query, (
        ('.*?\\' + current_church + '\\b.*?'), ('.*?\\' + new_village + '\\b.*?'),
        ('.*?\\' + current_region + '\\b.*?'),))
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    return [churches for churches in result]
