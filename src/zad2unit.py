from src.zad2 import Checker
import unittest

class CheckerTest(unittest.TestCase):
    def setUp(self):
        self.checker = Checker()

    def test_halibutZZiemniakamimmmmmmPycha_true(self):
        self.assertEqual(self.checker.ValidPassword("halibutZZiemniakamimmmmmmPycha!!!111oneone"), True)

    def test_HumanistaBeletrysta2137_true(self):
        self.assertEqual(self.checker.ValidPassword("HumanistaBeletrysta2137()"), True)

    def test_HassaN0_true(self):
        self.assertEqual(self.checker.ValidPassword("HassaN0)"), True)

    def test_HASLo_true(self):
        self.assertEqual(self.checker.ValidPassword("HASLo!23"), True)

    def test_Haslo123_true(self):
        self.assertEqual(self.checker.ValidPassword("Haslo123@"), True)

    def test_haaaaaaaaaaaaaaaa_false(self):
        self.assertEqual(self.checker.ValidPassword("haaaaaaaaaaaaaaaa)"), False)

    def test_many_exclamation_marks_false(self):
        self.assertEqual(self.checker.ValidPassword("!!!!!!!!!!!!!!!!"), False)

    def test_237942789374892738_false(self):
        self.assertEqual(self.checker.ValidPassword("237942789374892738"), False)

    def test_haslomalarskie128e_false(self):
        self.assertEqual(self.checker.ValidPassword("haslomalarskie128e"), False)

    def test_haslo_false(self):
        self.assertEqual(self.checker.ValidPassword("haslo"), False)

    def test_ARBITER_false(self):
        self.assertEqual(self.checker.ValidPassword("ARBITER"), False)

    def test_23_error(self):
        with self.assertRaisesWithMessage(ValueError):
            self.checker.ValidPassword(23)

    def test_None_error(self):
        with self.assertRaisesWithMessage(ValueError):
            self.checker.ValidPassword(None)

    def test_False_error(self):
        with self.assertRaisesWithMessage(ValueError):
            self.checker.ValidPassword(False)

    def assertRaisesWithMessage(self, exception):
        return self.assertRaisesRegex(exception, r".+")

    def tearDown(self):
        self.checker = None