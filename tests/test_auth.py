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

def setup_function(function):
    print("setting up", function)
    
def test_func1():
    assert True


def test_func2():
    assert False

    
def test_myoutput(capsys):  # or use "capfd" for fd-level
    print("hello")
    sys.stderr.write("world\n")
    captured = capsys.readouterr()
    assert captured.out == "hello\n"
    assert captured.err == "world\n"
    print("next")
    captured = capsys.readouterr()
    assert captured.out == "next\n"

if __name__ == '__main__':
    unittest.main()
