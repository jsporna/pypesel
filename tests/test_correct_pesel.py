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


def test_correct_pesel_gender(pesel_obj):
    pytest.assume(pesel_obj.gender == 'male')


def test_correct_pesel_male(pesel_obj):
    pytest.assume(pesel_obj.male is True)


def test_correct_pesel_year(pesel_obj):
    pytest.assume(pesel_obj.year == 2165)


def test_correct_pesel_month(pesel_obj):
    pytest.assume(pesel_obj.month == 3)


def test_incorrect_pesel_day(pesel_obj):
    pytest.assume(pesel_obj.day == 21)
