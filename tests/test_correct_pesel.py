from pesel import Pesel
import unittest


class CorrectPeselTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.value = "65432101239"
        self.pesel = Pesel(self.value)

    def test_correct_pesel(self):
        self.assertEqual(self.pesel.value, self.value)

    def test_correct_pesel_gender(self):
        self.assertEqual(self.pesel.gender, 'male')

    def test_correct_pesel_male(self):
        self.assertTrue(self.pesel.male)

    def test_correct_pesel_year(self):
        self.assertEqual(self.pesel.year, 2165)

    def test_correct_pesel_month(self):
        self.assertEqual(self.pesel.month, 3)

    def test_incorrect_pesel_day(self):
        self.assertEqual(self.pesel.day, 21)
