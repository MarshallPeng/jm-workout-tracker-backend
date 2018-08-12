import unittest

class ExampleTest(unittest.TestCase):


    def test_a(self):
        self.assert_(1 == 1)

    def test_b(self):
        self.assertNotEquals(1, 2)
