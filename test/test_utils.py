import unittest
import datetime
from bot import utils


class UtilTest(unittest.TestCase):
    def test_get_quote(self):
        self.assertIsNotNone(utils.get_quote())
        self.assertNotEqual(utils.get_quote(), '')

    def test_get_key(self):
        self.assertIsNotNone(utils.get_key())
        self.assertNotEqual(utils.get_key(), '')
        self.assertEqual(utils.get_key()[0], str(datetime.datetime.now().month))


if __name__ == '__main__':
    unittest.main()
