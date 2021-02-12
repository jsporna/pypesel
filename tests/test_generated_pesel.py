from pesel import Pesel
import unittest


class GeneratedPeselTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.pesel = Pesel.generate()

    def test_generated_pesel(self):
        self.assertIsInstance(self.pesel.value, str)

    def test_generated_pesel_gender(self):
        self.assertIn(self.pesel.gender, ('male', 'female'))

    def test_generated_pesel_male(self):
        self.assertIsInstance(self.pesel.male, bool)

    def test_generated_pesel_year(self):
        self.assertTrue(Pesel.YEAR_MIN <= self.pesel.year <= Pesel.YEAR_MAX)

    def test_generated_pesel_month(self):
        self.assertTrue(1 <= self.pesel.month <= 12)

    def test_generated_pesel_day(self):
        self.assertTrue(1 <= self.pesel.day <= 31)
