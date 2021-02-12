from pesel import Pesel
import unittest


class CorrectPeselTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.value = "65432101238"

    def test_incorrect_pesel(self):
        with self.assertRaises(ValueError):
            p = Pesel(self.value)
