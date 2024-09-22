import pytest
import sqlite3

###### Part1 ######
@pytest.fixture(scope='session')
def connection():
    """fixturing for creating a database connection."""
    connection = sqlite3.connect('database_sample.db')
    yield connection
    connection.close()

@pytest.fixture(scope='session')
def cursor(connection):
    """fixturing for getting a database cursor from the connection."""
    return connection.cursor()

###### Part2 ######
@pytest.fixture(scope='function', params=[(1, 'Item 1'), (2, 'Item 2')])
def table_cursor(request, cursor):
    """preparing table, inserting data, and providing a cursor to interact with the table."""
    cursor.execute('DROP TABLE IF EXISTS items')
    cursor.execute('CREATE TABLE items (id INTEGER, name TEXT)')
    cursor.execute('INSERT INTO items VALUES (?, ?)', request.param)
    cursor.connection.commit()
    yield cursor
    cursor.execute('DROP TABLE IF EXISTS items')