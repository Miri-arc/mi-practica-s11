import unittest
from src.calculadora import Calculadora

class TestCalculadora(unittest.TestCase):
    def setUp(self):
        self.calc = Calculadora()

    # --- Operaciones basicas ---
    def test_sumar(self):
        self.assertEqual(self.calc.sumar(2, 3), 5)

    def test_restar(self):
        self.assertEqual(self.calc.restar(10, 4), 6)

    def test_multiplicar(self):
        self.assertEqual(self.calc.multiplicar(3, 4), 12)

    def test_dividir(self):
        self.assertEqual(self.calc.dividir(10, 2), 5)

    def test_dividir_entre_cero(self):
        with self.assertRaises(ValueError):
            self.calc.dividir(10, 0)

    # --- es_par ---
    def test_es_par_true(self):
        self.assertTrue(self.calc.es_par(4))

if __name__ == "__main__":
    unittest.main()