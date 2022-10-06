from MySQLCommand.CreateConnection import connect


def update_user_activity(user):
    """
    This nodule update count of user activity when it is registrated and search something
    :param user: user to find and update
    :return: true if all is ok
    """
    connection = connect()
    cursor = connection.cursor()
    cursor.execute(
        "SELECT count_of_visits FROM activity where userid=(%s)",
        (
            user,
        ),
    )
    activity = int(*list(*cursor.fetchall()))
    cursor.execute("UPDATE activity SET count_of_visits=(%s) WHERE userid=(%s)", (activity + 1, user))
    cursor.close()
    connection.commit()
    connection.close()
