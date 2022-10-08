import datetime

from MySQLCommand.CreateConnection import connect


def send_info_message(count_of_new, count_of_uses):
    """
    This module send information message about user activity
    :param count_of_new: count of new users during week
    :param count_of_uses: count of usages during week
    :return: message
    """
    return f"Нових користувачів - {count_of_new}.\n" \
           f"Активних дій {count_of_uses}"


def get_count_of_new_user(now):
    """
    This module gets count of new user during last week
    :param now: date to clock
    :return: count of users
    """
    week = now - datetime.timedelta(days=7, hours=0, minutes=0, seconds=0)
    connection = connect()
    cursor = connection.cursor()
    cursor.execute(
        "SELECT COUNT(*) FROM activity where (date BETWEEN (%s) and (%s)) and flag=0",
        (
            (week),
            (now),
        ),
    )
    activity = int(*list(*cursor.fetchall()))
    cursor.close()
    connection.close()
    return activity


def get_count_of_uses(now):
    """
    This module counts uses of bot by user per last week
    :param now: now time to send message
    :return:  list of count usages
    """
    week = now - datetime.timedelta(days=7, hours=0, minutes=0, seconds=0)
    connection = connect()
    cursor = connection.cursor()
    cursor.execute(
        "UPDATE activity SET diff = count_of_visits-was_before_set where (date BETWEEN (%s) and (%s)) ",
        (week, now))
    connection.commit()
    cursor.execute(
        "UPDATE activity SET was_before_set=count_of_visits  where (date BETWEEN (%s) and (%s)) ",
        (week, now))
    connection.commit()
    cursor.execute(
        "UPDATE activity SET flag =1 ",)
    connection.commit()
    cursor.execute(
        "SELECT diff from activity WHERE (date BETWEEN(%s) and (%s))",
        (week, now)
    )
    activity = cursor.fetchall()
    cursor.close()
    connection.close()

    return sum([a for act in activity for a in act])
