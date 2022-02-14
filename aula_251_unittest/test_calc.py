import unittest
from calc import soma

class TestCalc(unittest.TestCase):
    def test_if_soma_5_e_5_return_10(self):
        self.assertEqual(soma(x=5, y=5), 10)
    
    def test_if_soma_5_negativo_e_5_return_10(self):
        self.assertEqual(soma(x=-5, y=5), 10)

    def test_soma_varias_entradas(self):
        x_y_saidas = (
            (10, 10, 20)
            (1, 10, 11)
            (-10, 10, 0)
            (100, 10, 90)
        )
        for x_y_saida in x_y_saidas:
            x, y, saida = x_y_saida
            self.assertEqual(soma(x, y), saida)

unittest.main()