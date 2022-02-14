"""
TDD - TEST DRIVEN DEVELOPMENT (Desenvolvimento dirigido a testes)

RED:
1 - Criar o teste e ver falhar

GREEN:
2 - Criar o codigo e ver o teste passar

REFACTOR:
3 - Refatorar o código

"""

import unittest


class TestBaconComOvos(unittest.TestCase):
    def test_bacon_com_ovos(self):
        with self.assertRaises(AssertionError):
            bacon_com_ovos(0)