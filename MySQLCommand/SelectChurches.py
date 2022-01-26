"""
Select all churches when its needed
"""

# local imports
from MySQLCommand.CreateConnection import connect
import re


def get_Churches(name: str, county: str) -> [list, int]:
    """
    get all churches of current county
    :param name: str
    :param county: str
    :return: list
    """
    name1 = name.rstrip()
    name1 = "".join(map(str, name1))
    name1 = re.escape(name1)
    churches = []
    connection = connect()
    query = "select church from catalog_of_metrics  where village regexp  (%s)and county regexp  (%s)"
    cursor = connection.cursor()
    cursor.execute(
        query,
        (
            (".*?\\" + name1 + "\\b.*?"),
            (".*?\\" + county + "\\b.*?"),
        ),
    )
    result = list(zip(*cursor.fetchall()))
    new_churches = []
    if len(result) != 0:
        for item in result[0]:
            churches.append(item)
        cursor.close()
        connection.close()
        for church in churches:
            church = re.sub("\(.*", "", church, flags=re.DOTALL)
            church = re.sub(",.*", "", church, flags=re.DOTALL)
            if church.strip() not in new_churches:
                new_churches.append(church.strip())
    return new_churches, len(new_churches)
