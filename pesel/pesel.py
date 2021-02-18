"""Implementation module of Pesel Class"""

import random
import time
import calendar
from datetime import date, datetime
from typing import Union, Optional
from enum import Enum


class PeselConst(Enum):
    """PeselConst Class contains magic numbers for Pesel Class"""
    YEAR_BASE = 1900
    YEAR_MIN = 1800
    YEAR_MAX = 2299
    CYCLE_SIZE = 500
    WEIGHTS = (1, 3, 7, 9, 1, 3, 7, 9, 1, 3)


class Pesel:
    """Pesel Class to serve or generate PESEL number"""

    def __init__(self, pesel: Union[str, int]):
        """Create a new PESEL instance
        :param pesel: PESEL number
        :type pesel: str
        :raise: ValueError
        """
        if not Pesel.validate(pesel):
            raise ValueError("Provided PESEL number is not valid")
        self._pesel = str(pesel)

    @staticmethod
    def validate(pesel: Union[str, int]) -> bool:
        """Validate given PESEL number
        :param pesel: PESEL number
        :type pesel: str
        :return: True if PESEL number is valid else False
        :rtype: bool
        """
        if isinstance(pesel, int):
            pesel = str(pesel)
        if not (pesel.isdigit() and len(pesel) == 11):
            return False
        if Pesel.checksum(pesel) != pesel[-1]:
            return False
        return True

    @property
    def year(self) -> int:
        """Get year of birth
        :return: Year of birth
        :rtype: int
        """
        year = int(self._pesel[:2])
        month = int(self._pesel[2:4])
        offset = month - month % 20
        calculated_year = PeselConst.YEAR_BASE.value + 5 * offset + year
        return calculated_year \
            if calculated_year <= PeselConst.YEAR_MAX.value \
            else calculated_year - PeselConst.CYCLE_SIZE.value

    @property
    def month(self) -> int:
        """Get month of birth
        :return: Month of birth
        :rtype: int
        """
        return int(self._pesel[2:4]) % 20

    @property
    def day(self) -> int:
        """Get day of birth
        :return: Day of birth
        :rtype: int
        """
        return int(self._pesel[4:6])

    @property
    def date(self) -> date:
        return date(self.year, self.month, self.day)

    @property
    def male(self) -> bool:
        """Get if PESEL number describes male person
        :return: True if PESEL number describes male person else False
        :rtype: bool
        """
        return self.gender == "male"

    @property
    def female(self) -> bool:
        """Get if PESEL number describes female person
        :return: True if PESEL number describes female person else False
        :rtype: bool
        """
        return self.gender == "female"

    @property
    def gender(self) -> str:
        """Get gender of person described by PESEL number
        :return: Gender of person ('male' or 'female')
        :rtype: str
        """
        return "male" if int(self._pesel[-2]) % 2 else "female"

    @property
    def value(self) -> str:
        """Get value of PESEL number
        :return: PESEL number
        :rtype: str
        """
        return self._pesel

    def __str__(self):
        return self._pesel

    def __repr__(self):
        return f'{self.__class__.__name__}({self._pesel})'

    def __eq__(self, other):
        if isinstance(other, Pesel):
            return self.value == other.value
        if isinstance(other, (str, int)):
            return self.value == str(other)
        if isinstance(other, datetime):
            other = other.date()
        if isinstance(other, date):
            return self.date == other
        return False

    def __ne__(self, other):
        return not self == other

    def __gt__(self, other):
        if isinstance(other, Pesel):
            return self.date > other.date
        if isinstance(other, datetime):
            other = other.date()
        if isinstance(other, date):
            return self.date > other
        return False

    def __ge__(self, other):
        return self == other or self > other

    def __le__(self, other):
        return not self > other

    def __lt__(self, other):
        return not self >= other


    @staticmethod
    def checksum(pesel: Union[str, int]) -> str:
        """Calculate checksum for provided pesel (with or without checksum) and returns check digit
        :param pesel: PESEL number
        :type pesel: str
        :return: check digit
        :rtype str
        """
        pesel = str(pesel)
        if len(pesel) not in (10, 11):
            raise ValueError("Pesel should have 10 or 11 digits")
        checksum = 0
        for index, value in enumerate(pesel[:10]):
            checksum += PeselConst.WEIGHTS.value[index] * int(value)
        return str((10 - (checksum % 10)) % 10)

    @staticmethod
    def __month_offset(year: int) -> int:
        calculated_offset = (year // 100 - 4) % 5 * 20
        return calculated_offset if calculated_offset >= 0 else 100 + calculated_offset

    @classmethod
    def generate(cls, male: Optional[bool] = None,
                 year: Optional[int] = None, month: Optional[int] = None, day: Optional[int] = None):
        """Generate random PESEL number and create instance of class Pesel

        :param male: True for male, False for female
        :type male: bool
        :param year: The year of birth
        :type year: int
        :param month: The month of birth
        :type month: int
        :param day: The day of birth
        :type day: int
        :return: instance of class Pesel
        :rtype: pesel.Pesel
        """
        if year and day == 29 and month == 2 and not calendar.isleap(year):
            raise ValueError(f'Year {year} is not leap so February has only 28 days')

        random.seed(time.time())
        gender = int(male) if male is not None else random.randint(0, 1)

        _year = year if year is not None else random.randint(PeselConst.YEAR_MIN.value, PeselConst.YEAR_MAX.value)
        if not PeselConst.YEAR_MIN.value <= _year <= PeselConst.YEAR_MAX.value:
            raise ValueError(
                f'Year should have value between {PeselConst.YEAR_MIN.value} & {PeselConst.YEAR_MAX.value}')

        if day is None:
            _month = month if month is not None else random.randint(1, 12)
            if not 1 <= _month <= 12:
                raise ValueError('Month should have value between 1 and 12')

            max_day = calendar.monthrange(_year, _month)[1]
            _day = random.randint(1, max_day)
        else:
            if not month:
                try:
                    _month = random.choice([idx for idx, days in enumerate(calendar.mdays) if days >= day > 0])
                except IndexError as err:
                    raise ValueError('Day should have value between 1 and 31') from err
            else:
                _month = month

            if not 1 <= _month <= 12:
                raise ValueError('Month should have value between 1 and 12, {}'.format(_month))

            _day = day

        max_day = calendar.monthrange(_year, _month)[1]
        if not 1 <= _day <= max_day:
            raise ValueError('Day should have value between 1 and {} for month {}'.format(max_day, _month))

        pesel = "{:02d}{:02d}{:02d}{:03d}{}".format(
            _year % 100,
            _month + Pesel.__month_offset(_year),
            _day,
            random.randint(0, 999),
            random.randrange(gender, 10, 2))
        pesel += Pesel.checksum(pesel)
        return cls(pesel)
