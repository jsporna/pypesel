from pesel import Pesel
import pytest


@pytest.fixture(scope='session', params=["65432101239"])
def pesel_value(request):
    return request.param


@pytest.fixture(scope='session')
def pesel_obj(pesel_value):
    return Pesel(pesel_value)


def test_correct_pesel(pesel_obj, pesel_value):
    pytest.assume(pesel_obj.value == pesel_value)


@pytest.mark.parametrize(['pesel', 'gender'], (
    (Pesel('65432101239'), 'male'),
    (Pesel('66032072666'), 'female'),
))
def test_correct_pesel_gender(pesel, gender):
    pytest.assume(pesel.gender == gender)


@pytest.mark.parametrize(['pesel', 'male'], (
    (Pesel('65432101239'), True),
    (Pesel('66032072666'), False),
))
def test_correct_pesel_male(pesel, male):
    pytest.assume(pesel.male is male)
    pytest.assume(pesel.female is not male)


@pytest.mark.parametrize(['pesel', 'year'], (
    # 1800-1899
    (Pesel('14810100023'), 1814),
    # 1900-1999
    (Pesel('66032072666'), 1966),
    # 2000-2099
    (Pesel('04251461982'), 2004),
    # 2100-2199
    (Pesel('65432101239'), 2165),
    # 2200-2299
    (Pesel('14610100034'), 2214),
))
def test_correct_pesel_year(pesel, year):
    pytest.assume(pesel.year == year)


@pytest.mark.parametrize(['pesel', 'month'], (
    # 1800-1899
    (Pesel('14810100023'), 1),
    # 1900-1999
    (Pesel('66032072666'), 3),
    # 2000-2099
    (Pesel('04251461982'), 5),
    # 2100-2199
    (Pesel('65432101239'), 3),
    # 2200-2299
    (Pesel('14610100034'), 1),
))
def test_correct_pesel_month(pesel, month):
    pytest.assume(pesel.month == month)


def test_incorrect_pesel_day(pesel_obj):
    pytest.assume(pesel_obj.day == 21)
