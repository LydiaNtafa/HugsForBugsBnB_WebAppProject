from lib.UserRepository import *
from lib.User import *


def test_all(db_connection):
    db_connection.seed("seeds/makers_bnb_database.sql")
    repository = UserRepository (db_connection)
    assert repository.all() == [
        User(1, 'asha@example.com', 'password1'),
        User(2, 'lydia@example.com', 'password2'),
        User(3, 'fahim@example.com', 'password3'),
        User(4, 'gemma@example.com', 'password4')
        ]


def test_find(db_connection):
    db_connection.seed("seeds/makers_bnb_database.sql")
    repository = UserRepository(db_connection)
    user = repository.find(4)
    assert user == User(4, 'gemma@example.com', 'password4')


def test_create_user(db_connection):
    db_connection.seed("seeds/makers_bnb_database.sql")
    repository = UserRepository(db_connection)
    repository.create(User(None,'testemail','testpassword'))
    assert repository.all() == [
        User(1, 'asha@example.com', 'password1'),
        User(2, 'lydia@example.com', 'password2'),
        User(3, 'fahim@example.com', 'password3'),
        User(4, 'gemma@example.com', 'password4'),
        User(5, 'testemail', 'testpassword')
    ]

def test_find_by_email_does_raise_an_error(db_connection):
    db_connection.seed("seeds/makers_bnb_database.sql")
    repository = UserRepository(db_connection)
    searched_user = repository.find_user_by_email("fahim@example.com")
    assert searched_user == "User already exists"


def test_find_by_email_no_error_raised(db_connection):
    db_connection.seed("seeds/makers_bnb_database.sql")
    repository = UserRepository(db_connection)
    searched_user = repository.find_user_by_email("alex@example.com")
    assert searched_user == True













