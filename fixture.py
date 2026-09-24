import pytest


# --- basic fixture (function scope is default) ---

@pytest.fixture
def logged_in_user():
    print("Logging in...")
    user = {
        "username": "girish",
        "role": "admin",
    }
    return user


def test_dashboard(logged_in_user):
    print("Opening dashboard...")
    assert logged_in_user["username"] == "girish"
    assert logged_in_user["role"] == "admin"


# --- one fixture can use another ---

@pytest.fixture
def empty_cart():
    return {"items": []}


@pytest.fixture
def cart_with_one_item(empty_cart):
    empty_cart["items"].append("pen")
    return empty_cart


def test_cart_not_empty(cart_with_one_item):
    assert cart_with_one_item["items"] == ["pen"]


# --- yield = setup, then teardown after test ---

@pytest.fixture
def open_connection():
    print("DB connect")
    conn = {"connected": True}
    yield conn
    print("DB disconnect")
    conn["connected"] = False


def test_db_query(open_connection):
    assert open_connection["connected"] is True


# --- scope: class = one setup for all tests in the class ---

@pytest.fixture(scope="class")
def shared_session():
    print("session started for TestUserArea")
    session = {"visits": 0}
    yield session
    print("session ended")


class TestUserArea:
    def test_visit_home(self, shared_session):
        shared_session["visits"] += 1
        assert shared_session["visits"] == 1

    def test_visit_profile(self, shared_session):
        # same session dict as test_visit_home
        shared_session["visits"] += 1
        assert shared_session["visits"] == 2


# --- shared fixtures from conftest.py (browser, page) ---

def test_open_app(page):
    print("url is", page["url"])
    assert "udemy" in page["url"]


# --- notes (try these yourself) ---
#
# scope options: function | class | module | package | session
#
# @pytest.fixture(scope="module")
#
# put common fixtures in conftest.py so every test file can use them
#
# @pytest.fixture(autouse=True)
# def reset_something():
#     ... runs before each test in this file even if test does not ask for it
