import mysql.connector
from datetime import date

### GESTION BASE DE DONNEES ###

connection = mysql.connector.connect(
    user='root', password='root', host='mysql', port="3306", database='dbstime')
print("DB connected")

cursor = connection.cursor()
cursor.execute('Select * FROM user')
users = cursor.fetchall()
connection.close()

## fonction d'inscription
def register():
    print('Choose a username')
    username = str(input())
    print('What is your password')
    password = str(input())
    print('What is your firstname')
    firstname = str(input())
    print('What is your name')
    name = str(input())
    print('What is your email')
    email = str(input())

    ## retravailler, pose soucis
    ##
    ##
    sql = "INSERT INTO user (Username, Password, Firstname, Surname, Email, Birthdate, DateInscription) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    now = date.today()
    val = (username, password, firstname, name, email, now, now)
    cursor.execute(sql, val)

def login():
    print('Enter your username')
    username = str(input())
    print('Enter your password')
    password = str(input())

    ## produire le SQL query en dessous

def show_library():
    print('library page')

    ## produire le SQL query en dessous

def show_game_shop():
    print('shop page')

    ## produire le SQL query en dessous

def show_item_shop():
    print('Item shop page')

    ## produire le SQL query en dessous

def my_item():
    print("Item page'")


### GESTION INTERFACE ###

print('what do you wish to do ? Enter the number you wish for :')
print('1.  Register')
print('2.  Login')
print('3.  See my games')
print('4.  Buy a game')
print('5.  Buy / sell an item')
print('6.  See my items' )
print('')

choice1 = int(input())

match choice1:
    case 1:
        register()
    case 2:
        login()
    case 3:
        show_library()
    case 4:
        show_game_shop()
    case 5:
        show_item_shop()
    case 6:
        my_item()