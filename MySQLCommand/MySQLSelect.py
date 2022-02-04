"""
This module gets all information from database
"""

# local imports
import re

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
    query = """select archive.Name, province,eparchy,county,religion,village,church, birth, wedding, divorce, death, testament, additional from catalog_of_metrics  join archive archive on archive.num = catalog_of_metrics.archive where village regexp(%s)"""
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
    return new_metrics
