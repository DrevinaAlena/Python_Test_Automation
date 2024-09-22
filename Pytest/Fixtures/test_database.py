###### Part3 ######
def test_data_verification(table_cursor):
    """checking if the inserted data matches expected values."""
    table_cursor.execute('SELECT id, name FROM items')
    fetched_data = table_cursor.fetchall()

    expected_data = [(1, 'Item 1'), (2, 'Item 2')]
    assert fetched_data == expected_data, "Fetched database data does not match expected."