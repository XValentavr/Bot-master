"""
This module gets all information from database
"""

# local imports
import re
from collections import OrderedDict

from MySQLCommand.CreateConnection import connect


def SelectOperation(name: str) -> list:
    """
    get all information if province and locality is set
    :param name: str
    :return: list
    """
    name = "".join(map(str, name.rstrip()))
    name = re.escape(name)
    connection = connect()
    query = """select archive.Name, province,village,county,church, birth, wedding, divorce, death, testament, additional from catalog_of_metrics  join archive archive on archive.num = catalog_of_metrics.archive where village regexp(%s)"""
    cursor = connection.cursor()
    cursor.execute(query, (name,))
    result = cursor.fetchall()
    metrics = [item for item in result]
    cursor.close()
    connection.close()
    new_metrics = []
    for i in metrics:
        if i not in new_metrics:
            new_metrics.append(i)

    # sort keys, then get values from original - fast

    return create_sorted(new_metrics)


def create_sorted(metrics):
    """
    Sorts by length of metric
    :param metrics: income metric
    :return: final sorted result
    """
    final = []
    mtrc_dct = {len(str(m)): m for m in metrics}
    for i in sorted(mtrc_dct.keys()):
        final.append(mtrc_dct.get(i))
    return final
