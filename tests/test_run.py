import unittest
from main.run import main_func

class TestRun(unittest.TestCase):
    def runTest(self):
        main_func(args=None)
