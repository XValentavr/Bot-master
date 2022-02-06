"""
This module gets county data from local database
"""
# local imports
from MySQLCommand.CreateConnection import connect
import re


def get_county(name: str, county: str) -> list:
    """
    gets information about county from database
    :param name: str
    :param county: str
    :return: list
    """
    name1 = name.rstrip()
    if not name1.startswith(".*?"):
        name1 = re.escape(name1)

    connection = connect()
    query = "select distinct county from catalog_of_metrics  where village regexp  (%s) and county regexp(%s)"
    cursor = connection.cursor()
    cursor.execute(
        query,
        (
            (name1),
            (county),
        ),
    )
    result = list(zip(*cursor.fetchall()))
    county = []
    if len(result) != 0:
        for item in result[0]:
            county.append(item)
        cursor.close()
        connection.close()
        for cnt in county:
            cnt = re.sub("\(.*", "", cnt, flags=re.DOTALL)
            cnt = re.sub(",.*", "", cnt, flags=re.DOTALL)
            if cnt.strip() not in county:
                county.append(cnt.strip())
    return county
