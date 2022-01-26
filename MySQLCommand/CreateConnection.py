"""
This module creates localhost database connection
"""

# local imports
import mysql
from mysql.connector import MySQLConnection, Error


def connect():
    """
    create connection
    :return: connection of database
    """
    try:
        conn = mysql.connector.connect(
            host="localhost", database="genealogyboutique", user="root", password="root"
        )
    except Error as e:
        print("Error:", e)

    finally:
        return conn
