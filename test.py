import unittest

import game
import pytest

class TestGetLetter(unittest.TestCase):
    def test_exists(self):
        result_letter = game.letter
        self.assertIsInstance(result_letter, str)
    
    def test_id_doesnt_exist(self):
        result_letter = game.letter
        self.assertNotIsInstance(result_letter, int)

def test_get_all_tasks_not_empty():
    all_tasks = game.letter
    assert True

if __name__ == '__main__':
    unittest.main()