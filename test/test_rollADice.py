import unittest
from scripts.rollADice import dictionaryParser


class TestRollADice(unittest.TestCase):

    def test_dictionaryParser(self):
        result = dictionaryParser(1, "inTheGarden.yaml")
        expected = "potato changes by 1"
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
