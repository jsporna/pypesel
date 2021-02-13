from pesel import Pesel
import pytest


@pytest.fixture(scope='session', params=[Pesel.generate() for _ in range(100)])
def pesel_obj(request):
    return request.param


def test_generated_pesel(pesel_obj):
    with pytest.assume:
        assert isinstance(pesel_obj.value, str)
        assert len(pesel_obj.value) == 11
        assert pesel_obj.value.isdigit()


def test_generated_pesel_gender(pesel_obj):
    pytest.assume(pesel_obj.gender in ('male', 'female'))


def test_generated_pesel_male(pesel_obj):
    pytest.assume(isinstance(pesel_obj.male, bool))


def test_generated_pesel_year(pesel_obj):
    pytest.assume(Pesel.YEAR_MIN <= pesel_obj.year <= Pesel.YEAR_MAX)


def test_generated_pesel_month(pesel_obj):
    pytest.assume(1 <= pesel_obj.month <= 12)


def test_generated_pesel_day(pesel_obj):
    pytest.assume(1 <= pesel_obj.day <= 31)
