"""
This module show all information if county mod is selected
"""
# local imports
from MySQLCommand.CreateConnection import connect


def select_operation_get_counties(current_county: str, current_village: list) -> list:
    """
    get info is county is selected
    :param current_county: str
    :param current_village: list
    :return: list
    """
    new_village = ''.join(map(str, current_village.rstrip()))
    connection = connect()
    query = "select archive.Name, province,eparchy,village,religion,county,church,birth,wedding,divorce, death,testament," \
            "additional from catalog_of_metrics left join archive archive on archive.num =" \
            " catalog_of_metrics.archive where county regexp  (%s) and village regexp(%s)"
    cursor = connection.cursor()
    cursor.execute(query, (
        ('.*?\\' + current_county + '\\b.*?'), ('.*?\\' + new_village + '\\b.*?'),))
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    return [res for res in result]
