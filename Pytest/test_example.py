import pytest

@pytest.mark.long_running
def test_example_long():
    assert True

def test_example_quick():
    assert True