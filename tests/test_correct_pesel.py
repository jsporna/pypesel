from datetime import date, datetime

import pytest

from pesel import Pesel


@pytest.fixture(scope="session", params=["65432101239", 65432101239])
def pesel_value(request):
    return request.param


@pytest.fixture(scope="session", params=["65432101239", 65432101239])
def same_pesel_value(request):
    return request.param


@pytest.fixture(scope="session", params=["64301501235", 64301501235])
def other_pesel_value(request):
    return request.param


@pytest.fixture(scope="session")
def pesel_obj(pesel_value):
    return Pesel(pesel_value)


def test_correct_pesel(pesel_obj, pesel_value):
    pytest.assume(pesel_obj.value == str(pesel_value))


def test_correct_pesel_repr(pesel_obj, pesel_value):
    assert repr(pesel_obj) == f"Pesel({pesel_value})"


def test_correct_pesel_date(pesel_obj):
    assert pesel_obj.date == date(pesel_obj.year, pesel_obj.month, pesel_obj.day)


def test_correct_pesel_eq_pesel(pesel_value, same_pesel_value):
    assert Pesel(pesel_value) == Pesel(same_pesel_value)


def test_correct_pesel_eq_str_int(pesel_value, same_pesel_value):
    assert Pesel(pesel_value) == same_pesel_value


def test_correct_pesel_eq_date(pesel_obj):
    assert pesel_obj == date(pesel_obj.year, pesel_obj.month, pesel_obj.day)


def test_correct_pesel_eq_dateime(pesel_obj):
    assert pesel_obj == datetime(
        pesel_obj.year, pesel_obj.month, pesel_obj.day, 0, 0, 0
    )


def test_correct_pesel_eq_float(pesel_obj):
    assert pesel_obj == float(pesel_obj.value)


def test_correct_pesel_neq_other(pesel_value, other_pesel_value):
    assert Pesel(pesel_value) != other_pesel_value


def test_correct_pesel_gt_pesel(pesel_value, other_pesel_value, same_pesel_value):
    with pytest.assume:
        assert Pesel(pesel_value) > Pesel(other_pesel_value)
        assert not (Pesel(pesel_value) > Pesel(same_pesel_value))


def test_correct_pesel_gt_datetime(pesel_obj):
    assert not pesel_obj > datetime(
        pesel_obj.year, pesel_obj.month, pesel_obj.day, 0, 0, 0
    )


def test_correct_pesel_gt_float(pesel_obj):
    with pytest.raises(TypeError):
        assert pesel_obj > 1.23456789


def test_correct_pesel_gt_tuple(pesel_obj):
    with pytest.raises(TypeError):
        assert pesel_obj > (1, 2)


def test_correct_pesel_gt_list(pesel_obj):
    with pytest.raises(TypeError):
        assert pesel_obj > [1, 2]


def test_correct_pesel_gt_date(pesel_value, other_pesel_value, same_pesel_value):
    with pytest.assume:
        assert Pesel(pesel_value) > Pesel(other_pesel_value).date
        assert not (Pesel(pesel_value) > Pesel(same_pesel_value).date)


def test_correct_pesel_lt_pesel(pesel_value, other_pesel_value, same_pesel_value):
    with pytest.assume:
        assert Pesel(other_pesel_value) < Pesel(pesel_value)
        assert not (Pesel(same_pesel_value) < Pesel(pesel_value))


def test_correct_pesel_lt_date(pesel_value, other_pesel_value, same_pesel_value):
    with pytest.assume:
        assert Pesel(other_pesel_value) < Pesel(pesel_value).date
        assert not (Pesel(same_pesel_value) < Pesel(pesel_value).date)


def test_correct_pesel_ge_pesel(pesel_value, other_pesel_value, same_pesel_value):
    with pytest.assume:
        assert Pesel(pesel_value) >= Pesel(other_pesel_value)
        assert Pesel(pesel_value) >= Pesel(same_pesel_value)


def test_correct_pesel_ge_date(pesel_value, other_pesel_value, same_pesel_value):
    with pytest.assume:
        assert Pesel(pesel_value) >= Pesel(other_pesel_value).date
        assert Pesel(pesel_value) >= Pesel(same_pesel_value).date


def test_correct_pesel_le_pesel(pesel_value, other_pesel_value, same_pesel_value):
    with pytest.assume:
        assert Pesel(other_pesel_value) <= Pesel(pesel_value)
        assert Pesel(same_pesel_value) <= Pesel(pesel_value)


def test_correct_pesel_le_date(pesel_value, other_pesel_value, same_pesel_value):
    with pytest.assume:
        assert Pesel(other_pesel_value) <= Pesel(pesel_value).date
        assert Pesel(same_pesel_value) <= Pesel(pesel_value).date


@pytest.mark.parametrize(
    ["pesel", "gender"],
    (
        (Pesel("65432101239"), "male"),
        (Pesel("66032072666"), "female"),
    ),
)
def test_correct_pesel_gender(pesel, gender):
    pytest.assume(pesel.gender == gender)


@pytest.mark.parametrize(
    ["pesel", "male"],
    (
        (Pesel("65432101239"), True),
        (Pesel("66032072666"), False),
    ),
)
def test_correct_pesel_male(pesel, male):
    pytest.assume(pesel.male is male)
    pytest.assume(pesel.female is not male)


@pytest.mark.parametrize(
    ["pesel", "year"],
    (
        # 1800-1899
        (Pesel("14810100023"), 1814),
        # 1900-1999
        (Pesel("66032072666"), 1966),
        # 2000-2099
        (Pesel("04251461982"), 2004),
        # 2100-2199
        (Pesel("65432101239"), 2165),
        # 2200-2299
        (Pesel("14610100034"), 2214),
    ),
)
def test_correct_pesel_year(pesel, year):
    pytest.assume(pesel.year == year)


@pytest.mark.parametrize(
    ["pesel", "month"],
    (
        # 1800-1899
        (Pesel("14810100023"), 1),
        # 1900-1999
        (Pesel("66032072666"), 3),
        # 2000-2099
        (Pesel("04251461982"), 5),
        # 2100-2199
        (Pesel("65432101239"), 3),
        # 2200-2299
        (Pesel("14610100034"), 1),
    ),
)
def test_correct_pesel_month(pesel, month):
    pytest.assume(pesel.month == month)


def test_incorrect_pesel_day(pesel_obj):
    pytest.assume(pesel_obj.day == 21)
