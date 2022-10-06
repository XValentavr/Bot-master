"""
This module show all information if county mod is selected
"""
# local imports
import re

from MySQLCommand.CreateConnection import connect
from MySQLCommand.MySQLSelect import create_sorted


def select_operation_get_counties(current_county: str, current_village: list) -> list:
    """
    get info is county is selected
    :param current_county: str
    :param current_village: list
    :return: list
    """
    new_village = "".join(map(str, current_village.rstrip()))
    new_village = re.escape(new_village)

    connection = connect()
    query = (
        "select archive.Name, province,village,county,church,birth,wedding,divorce, death,testament,"
        "additional from catalog_of_metrics left join archive archive on archive.num ="
        " catalog_of_metrics.archive where county regexp  (%s) and village regexp(%s)"
    )
    cursor = connection.cursor()
    cursor.execute(
        query,
        (
            (current_county),
            (new_village),
        ),
    )
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    return create_sorted([res for res in result])
