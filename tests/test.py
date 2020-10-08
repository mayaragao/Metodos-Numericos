import unittest
from src.main import soma


class TestTal(unittest.TestCase):
    def test_retorno(self):
        self.assertEqual_10_10(soma(10, 10), 20)

    def test_retorno_soma_20_10(self):
        self.assertEqual(soma(20, 10), 30)
