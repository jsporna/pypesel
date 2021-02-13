from pesel import Pesel
import random
from datetime import datetime
import pytest

random.seed(datetime.now())


@pytest.fixture(scope="session")
def incorrect_pesel_value():
    return "65432101238"


def test_incorrect_pesel(incorrect_pesel_value):
    with pytest.raises(ValueError):
        Pesel(incorrect_pesel_value)


@pytest.mark.parametrize('year', [random.randint(0, 1799), random.randint(2300, 10000)])
def test_incorrect_year(year):
    with pytest.raises(ValueError):
        Pesel.generate(year=year)


@pytest.mark.parametrize('month', [0, random.randint(13, 100)])
def test_incorrect_month(month):
    with pytest.raises(ValueError):
        Pesel.generate(month=month)


@pytest.mark.parametrize('day', [0, random.randint(32, 100)])
def test_incorrect_day(day):
    with pytest.raises(ValueError):
        Pesel.generate(day=day)


@pytest.mark.parametrize(('month', 'day'), [(1, 32), (2, 30), (3, 32), (4, 31), (5, 32), (6, 31),
                                            (7, 32), (8, 32), (9, 31), (10, 32), (11, 31), (12, 32)])
def test_incorrect_month_day(month, day):
    with pytest.raises(ValueError):
        Pesel.generate(month=month, day=day)


@pytest.mark.parametrize(('year', 'month', 'day'), [(1832, 2, 30), (1831, 2, 29), (1900, 2, 29)])
def test_incorrect_year_month_day(year, month, day):
    with pytest.raises(ValueError):
        Pesel.generate(year=year, month=month, day=day)
