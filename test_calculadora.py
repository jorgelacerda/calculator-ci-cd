import unittest
from calculadora import Calculadora

class TestCalculadora(unittest.TestCase):

    def setUp(self):
        self.calc = Calculadora()

    def test_adicionar(self):
        self.assertEqual(self.calc.adicionar(2, 3), 5)
        self.assertEqual(self.calc.adicionar(-1, 1), 0)

    def test_subtrair(self):
        self.assertEqual(self.calc.subtrair(10, 5), 5)
        self.assertEqual(self.calc.subtrair(-1, -1), 0)

    def test_multiplicar(self):
        self.assertEqual(self.calc.multiplicar(3, 7), 21)
        self.assertEqual(self.calc.multiplicar(-1, -1), 1)

    def test_dividir(self):
        self.assertEqual(self.calc.dividir(10, 2), 5)
        with self.assertRaises(ValueError):
            self.calc.dividir(10, 0)

if __name__ == "__main__":
    unittest.main()
