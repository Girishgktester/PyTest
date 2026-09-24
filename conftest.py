import pytest


@pytest.fixture(scope="session")
def browser():
    print("Setting up browser")

    b = {
        "name": "Chrome",
        "version": "100.0",
        "platform": "windows"
    }

    yield b

    print("Tearing down browser")


@pytest.fixture(scope="module")
def page(browser):
    print("Setting up page with browser:", browser["name"])

    p = {
        "url": "https://www.udemy.com/",
        "title": "Example page"
    }

    yield p

    print("Tearing down page")