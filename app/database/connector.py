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
