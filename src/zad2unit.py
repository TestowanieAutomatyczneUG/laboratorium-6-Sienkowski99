from src.zad2 import Checker
import unittest

class CheckerTest(unittest.TestCase):
    def setUp(self):
        self.checker = Checker()

    def test_halibutZZiemniakamimmmmmmPycha_True(self):
        self.checker.ValidPassword("halibutZZiemniakamimmmmmmPycha!!!111oneone")

    def tearDown(self):
        self.checker = None