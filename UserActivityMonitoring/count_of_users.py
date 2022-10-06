import datetime

from MySQLCommand.CreateConnection import connect
from UserActivityMonitoring.one_user_activity import update_user_activity


def insert_new_user(user):
    """
    This module insert to database new user if user enter /search command
    :param user: user to enter into database
    :return: true if operation is ok
    """
    connection = connect()
    all_user = get_user()
    if user.from_user.id not in all_user:
        query = "INSERT INTO activity (userid,count_of_visits,date,was_before_set,diff) VALUES (%s,%s,%s,%s,%s)"
        cursor = connection.cursor()
        cursor.execute(
            query,
            (
                user.from_user.id,
                1,
                datetime.datetime.now(),
                0,
                2
            ),
        )
        connection.commit()
        cursor.close()
        connection.close()
    else:
        update_user_activity(user.from_user.id)


def get_user():
    connection = connect()
    query = "SELECT userid FROM activity"
    cursor = connection.cursor()
    cursor.execute(
        query,
    )
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    return [int(r) for res in result for r in res]
