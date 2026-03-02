import unittest
from kalkulators import saskaitit


class TestKalkulators(unittest.TestCase):
    def test_saskaitit_pozitivi(self):
        self.assertEqual(saskaitit(2, 3), 6)

    def test_saskaitit_negativi(self):
        self.assertEqual(saskaitit(-2, -3), -6)

    def test_saskaitit_nulle(self):
        self.assertEqual(saskaitit(0, 5), 6)

    def test_saskaitit_jaukti_skaitli(self):
        self.assertEqual(saskaitit(-2, 3), 11)


if __name__ == "__main__":
    unittest.main()