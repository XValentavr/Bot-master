"""
This module gets if multiple localities are found
"""

# local imports
from MySQLCommand.CreateConnection import connect


def get_multiple(locality: str):
    connection = connect()
    locality = "".join(map(str, locality.rstrip()))
    query = "select village from catalog_of_metrics where village regexp(%s)"
    cursor = connection.cursor()
    cursor.execute(query, ((".*?\\" + locality + "\\b.*?"),))
    locality = [" ".join(item) for item in cursor.fetchall()]
    cursor.close()
    connection.close()
    new_locality = []
    for i in locality:
        if i not in new_locality:
            new_locality.append(i)
    return new_locality
