# Python version
class PyVersion:
    MAJOR = 3
    MINOR = 10


# Database
class Database:
    USER = "root"
    PASSWORD = "supersecretpassword123"  # QoL: store password in environment variables
    HOST = "127.0.0.1"
    PORT = "3306"
    NAME = "dbstime"


# Password
class Password:
    SALT = b"this_is_a_very_secret_salt_that_should_be_kept_secret"
