"""Implementation module of Pesel Class"""

import random
from datetime import datetime
import calendar


class Pesel:
    """Pesel Class to serve or generate PESEL number"""
    YEAR_BASE = 1900
    YEAR_MIN = 1800
    YEAR_MAX = 2299
    CYCLE_SIZE = 500
    WEIGHTS = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]

    def __init__(self, pesel):
        """Create a new PESEL instance
        :param pesel: PESEL number
        :type pesel: str
        :raise: ValueError
        """
        if not Pesel.validate(pesel):
            raise ValueError("Provided PESEL number is not valid")
        self._pesel = pesel

    @staticmethod
    def validate(pesel):
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
        calculated_year = Pesel.YEAR_BASE + 5 * offset + year
        return calculated_year \
            if calculated_year <= Pesel.YEAR_MAX \
            else calculated_year - Pesel.CYCLE_SIZE

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
    def male(self) -> bool:
        """Get if PESEL number describes male person
        :return: True if PESEL number describes male person else False
        :rtype: bool
        """
        return bool(int(self._pesel[-2]) % 2)

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
        return f'{self.__class__.__name__}("{self._pesel}")'

    @staticmethod
    def checksum(pesel):
        """Calculate checksum for provided pesel (with or without checksum) and returns check digit
        :param pesel: PESEL number
        :type pesel: str
        :return: check digit
        :rtype str
        """
        if len(pesel) not in (10, 11):
            raise ValueError("Pesel should have 10 or 11 digits")
        checksum = 0
        for index, value in enumerate(pesel[:10]):
            checksum += Pesel.WEIGHTS[index] * int(value)
        return str((10 - (checksum % 10)) % 10)

    @staticmethod
    def __month_offset(year):
        calculated_offset = (year // 100 - 4) % 5 * 20
        return calculated_offset if calculated_offset >= 0 else 100 + calculated_offset

    @classmethod
    def generate(cls, male: bool = None,
                 year: int = None, month: int = None, day: int = None):
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
        random.seed(datetime.now())

        gender = int(male) if male is not None else random.randint(0, 1)

        _year = year if year is not None else random.randint(Pesel.YEAR_MIN, Pesel.YEAR_MAX)
        if not Pesel.YEAR_MIN <= _year <= Pesel.YEAR_MAX:
            raise ValueError(f'Year should have value between {Pesel.YEAR_MIN} & {Pesel.YEAR_MAX}')

        _month = month if month is not None else random.randint(1, 12)
        if not 1 <= _month <= 12:
            raise ValueError('Month should have value between 1 and 12')

        max_day = calendar.monthrange(_year, _month)[1]
        if day and not month and day > max_day:
            if day == 31:
                _month = random.choice((1, 3, 5, 7, 8, 10, 12))
            if day == 30:
                _month = random.choice((1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))

        if day == 29 and not year and day > max_day:
            while True:
                _year = random.randint(Pesel.YEAR_MIN, Pesel.YEAR_MAX)
                if calendar.isleap(_year):
                    break

        max_day = calendar.monthrange(_year, _month)[1]
        _day = day if day is not None else random.randint(1, max_day)
        if not 1 <= _day <= max_day:
            raise ValueError('Day should have value between 1 and {}'.format(max_day))

        pesel = "{:02d}{:02d}{:02d}{:03d}{}".format(
            _year % 100,
            _month + Pesel.__month_offset(_year),
            _day,
            random.randint(0, 999),
            random.randrange(gender, 10, 2))
        pesel += Pesel.checksum(pesel)
        return cls(pesel)
