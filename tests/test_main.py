import pytest

from main import division


@pytest.mark.skip
def test_division_good():
    assert division(10, 2) == 5
