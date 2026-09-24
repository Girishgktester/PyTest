import sys

import pytest


def test_always_runs():
    assert 1 + 1 == 2
    print("This test always runs")


@pytest.mark.skip(reason="Example: skip a test without running it")
def test_skipped():
    assert False


@pytest.mark.skipif(sys.version_info < (3, 10), reason="Needs Python 3.10+")
def test_skip_on_old_python():
    assert True


@pytest.mark.xfail(reason="Known bug — expect failure for now")
def test_expected_failure():
    assert 2 + 2 == 5


@pytest.mark.smoke
def test_smoke_example():
    """Run only smoke tests: pytest -m smoke"""
    assert "hello".upper() == "HELLO"
    print("Smoke test passed")


@pytest.mark.slow
def test_slow_example():
    """Run everything except slow: pytest -m 'not slow'"""
    total = sum(range(100))
    assert total == 4950
    print("Slow test passed")


@pytest.mark.parametrize(
    "value, expected",
    [
        pytest.param(2, 4, marks=pytest.mark.smoke),
        pytest.param(3, 9, marks=pytest.mark.smoke),
        pytest.param(0, 0, marks=pytest.mark.skip(reason="Edge case not implemented")),
    ],
)
def test_square_with_per_case_marks(value, expected):
    assert value * value == expected


@pytest.mark.integration
def test_integration_marker_example():
    """Grouping: pytest -m integration"""
    import json

    data = json.loads('{"ok": true}')
    assert data["ok"] is True
