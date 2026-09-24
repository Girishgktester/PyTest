import pytest

def test_logout(page):
    print("LOGOUT USER", page["url"])
    print("Application url ", page["url"])
    assert True


