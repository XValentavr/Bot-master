"""
This module gets data from database if church mod is selected
"""

# local imports
import re

from MySQLCommand.CreateConnection import connect
from MySQLCommand.MySQLSelect import create_sorted


def select_operation_get_churches(
        current_church: str, current_village: str, current_region: str
) -> list:
    """
    get info from database when church mod is selected
    :param current_church: str
    :param current_village: list
    :param current_region: str
    :return: list
    """
    new_village = "".join(map(str, current_village.rstrip()))
    if not new_village.startswith(".*?"):
        new_village = re.escape(new_village)
    connection = connect()
    query = "select archive.Name, province,village,county,church,birth,wedding,divorce, death,testament,additional from catalog_of_metrics left join archive archive on archive.num = catalog_of_metrics.archive where church regexp  (%s)and village regexp(%s)  and county regexp(%s)"
    cursor = connection.cursor()
    cursor.execute(
        query,
        (
            (current_church),
            (new_village),
            (current_region),
        ),
    )
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    new_metrics = []
    final = []
    mtrc_dct = {len(str(m)): m for m in new_metrics}
    for i in sorted(mtrc_dct.keys()):
        final.append(mtrc_dct.get(i))
    return create_sorted([churches for churches in result])
