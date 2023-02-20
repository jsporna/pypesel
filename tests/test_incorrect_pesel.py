import random
import time

import pytest

from pesel import Pesel

random.seed(time.time())


@pytest.fixture(
    scope="session", params=["65432101238", "6543210123", 65432101238, 6543210123]
)
def pesel_value(request):
    return request.param


@pytest.fixture(scope="session", params=["654321012"])
def short_pesel_value(request):
    return request.param


def test_incorrect_pesel_object(pesel_value):
    with pytest.raises(ValueError):
        Pesel(pesel_value)


def test_incorrect_pesel_value_too_short(short_pesel_value):
    with pytest.raises(ValueError):
        Pesel.checksum(short_pesel_value)


def test_incorrect_pesel_validation(pesel_value):
    assert Pesel.validate(pesel_value) is False


@pytest.mark.parametrize("year", [random.randint(0, 1799), random.randint(2300, 10000)])
def test_incorrect_year(year):
    with pytest.raises(ValueError):
        Pesel.generate(year=year)


@pytest.mark.parametrize("month", [0, random.randint(13, 100)])
def test_incorrect_month(month):
    with pytest.raises(ValueError):
        Pesel.generate(month=month)


@pytest.mark.parametrize("day", [0, random.randint(32, 100)])
def test_incorrect_day(day):
    with pytest.raises(ValueError):
        Pesel.generate(day=day)


@pytest.mark.parametrize(
    ("month", "day"),
    [
        (1, 32),
        (2, 30),
        (3, 32),
        (4, 31),
        (5, 32),
        (6, 31),
        (7, 32),
        (8, 32),
        (9, 31),
        (10, 32),
        (11, 31),
        (12, 32),
        (13, 32),
    ],
)
def test_incorrect_month_day(month, day):
    with pytest.raises(ValueError):
        Pesel.generate(month=month, day=day)


@pytest.mark.parametrize(
    ("year", "month", "day"), [(1832, 2, 30), (1831, 2, 29), (1900, 2, 29)]
)
def test_incorrect_year_month_day(year, month, day):
    with pytest.raises(ValueError):
        Pesel.generate(year=year, month=month, day=day)
