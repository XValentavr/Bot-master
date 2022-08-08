"""
This module creates localhost database connection
"""

# local imports
import mysql
from mysql.connector import MySQLConnection


def connect():
    """
    create connection
    :return: connection of database
    """
    conn = mysql.connector.connect(
        host="localhost", database="genealogyboutique", user="valentyn",
        password="valentyn"
    )
    return conn
