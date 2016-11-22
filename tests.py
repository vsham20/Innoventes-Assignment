from mock import patch
import unittest
from unittest import TestCase
import ro


class Test(TestCase):

    # get_input will return 'yes' during this test
    @patch('ro.get_input', return_value=['I','I','+'])
    def test_answer_yes(self, *args):
        test_obj = ro.rom_conversions()
        self.assertEqual(test_obj.calculation(), 'II')


if __name__ == '__main__':
    unittest.main()
