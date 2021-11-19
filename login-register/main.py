import os.path
import getpass

if not os.path.exists('record.txt'):
    fs = open('record.txt', 'w')
    fs.close()


def register():
    username = input("Enter username: ")
    if username in open('record.txt', 'r').read():
        print("username already exists")
        exit()

    password = getpass.getpass("Enter password: ")
    confirm_password = getpass.getpass("Enter confirm password: ")
    if password != confirm_password:
        print("password not match")
        exit()

    file = open('record.txt', 'a')
    file.write(username)
    file.write(" ")
    file.write(password)
    file.write("\n")
    file.close()
    print("user was successfully created")
    exit()


def login():
    username = input("Enter username: ")
    password = getpass.getpass("Enter password: ")
    users_data = []

    for file in open('record.txt', 'r').readlines():
        users_data.append(file.split())

    total_users = len(users_data)
    increment = 0
    is_login = False
    while increment < total_users:
        uname = users_data[increment][0]
        upass = users_data[increment][1]
        if username == uname and password == upass:
            is_login = True

        increment += 1

    if is_login:
        print(f"welcome {username}")
    else:
        print("username & password not match")


question = input("Do you have an account? y/n: ")

if question == 'y':
    print('=============Login =============')
    login()

else:
    print("================register ==============")
    register()
