from backend.db.sql_api import select

def home():
    print('welcome to home page')
    q_data = select('user', 'add')
    print(q_data)

def movie():
    print('welcome to home page')


def tv():
    print('welcome to home page')