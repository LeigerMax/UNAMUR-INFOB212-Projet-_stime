import mysql.connector
from mysql.connector import errorcode

from app.settings import Database

connection_setting = {
    "user": Database.USER,
    "password": Database.PASSWORD,
    "host": Database.HOST,
    "port": Database.PORT,
    "database": Database.NAME
}


def connect():
    cnx = None

    try:
        cnx = mysql.connector.connect(**connection_setting)
    except mysql.connector.Error as err:
        cnx.close()
        raise err

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
            result = f(cnx, *args, **kwargs)
        except Exception as e:
            cnx.rollback()
            raise e
        else:
            cnx.commit()
        finally:
            cnx.close()
        return result

    return with_connection_
