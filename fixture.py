import pytest

# Fixture = setup
@pytest.fixture
def logged_in_user():
    print("Logging in...")
    user = {
        "username": "girish",
        "role": "admin"
    }
    return user


# Test uses the fixture
def test_dashboard(logged_in_user):
    print("Opening dashboard...")

    assert logged_in_user["username"] == "girish"
    assert logged_in_user["role"] == "admin"
  
#   Scope of the fixtures
    
# @pytest.fixture(scope="function")
# @pytest.fixture(scope="class")
# @pytest.fixture(scope="module")
# @pytest.fixture(scope="package")
# @pytest.fixture(scope="session")

# Fixture dependancy
@pytest.fixture
def llm():
    return OpenAI()

@pytest.fixture
def judge(llm):
    return DeepEvalJudge(llm)


# conftest.py

# A special pytest file where you put shared fixtures.

# tests/
# ├── conftest.py
# ├── test_rag.py
# └── test_llm.py

# yield fixtures

# yield separates setup and teardown.

# @pytest.fixture
# def rag_db():
#     db = create_database()   # setup

#     yield db

#     db.delete()              # teardown


# autouse

# Normally a test must explicitly request a fixture:

# def test_rag(llm):

# With autouse=True, pytest automatically runs it.

@pytest.fixture(autouse=True)
def setup():
    print("Runs automatically")