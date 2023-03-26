import mysql.connector
from mysql.connector import errorcode

from app.settings import Database
from app.view.console_utils.colors import RED_BLD
from app.view.console_utils.io import color_print

connection_setting = {
    "user": Database.USER,
    "password": Database.PASSWORD,
    "host": Database.HOST,
    "port": Database.PORT,
    "database": Database.NAME
}


def connect():
    try:
        cnx = mysql.connector.connect(**connection_setting)
    except mysql.connector.Error as err:
        color_print(err, RED_BLD)
        raise err
    else:
        return cnx


def with_connection(f):
    """
    Decorator used to create a connection to the database. Instantly closed when the function is executed.
    :param f: the function to execute with the decorator, should contain a SQL query
    :return: the return value of function f
    """

    def with_connection_(*args, **kwargs):
        cnx = connect()

        try:
            result = f(*args, connection=cnx, **kwargs)
        except Exception as e:
            cnx.rollback()
            raise e
        else:
            cnx.commit()
        finally:
            cnx.close()
        return result

    return with_connection_
