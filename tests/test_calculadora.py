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

    # --- Potencia ---
    def test_potencia_positiva(self):
        self.assertEqual(self.calc.potencia(2, 3), 8)

    def test_potencia_negativa(self):
        with self.assertRaises(ValueError):
            self.calc.potencia(5, -1)

    # --- Par / Impar ---
    def test_es_par_true(self):
        self.assertTrue(self.calc.es_par(4))

    def test_es_par_false(self):
        self.assertFalse(self.calc.es_par(7))

    # --- Factorial ---
    def test_factorial_positivo(self):
        self.assertEqual(self.calc.factorial(5), 120)

    def test_factorial_cero(self):
        self.assertEqual(self.calc.factorial(0), 1)

    def test_factorial_negativo(self):
        with self.assertRaises(ValueError):
            self.calc.factorial(-1)

    # --- Promedio ---
    def test_promedio_lista(self):
        self.assertEqual(self.calc.promedio([10, 20, 30]), 20.0)

    def test_promedio_vacio(self):
        with self.assertRaises(ValueError):
            self.calc.promedio([])

    # --- Maximo ---
    def test_maximo_lista(self):
        self.assertEqual(self.calc.maximo([3, 7, 1, 9]), 9)

    def test_maximo_vacio(self):
        with self.assertRaises(ValueError):
            self.calc.maximo([])

    # --- Clasificar Nota ---
    def test_clasificar_nota_excelente(self):
        self.assertEqual(self.calc.clasificar_nota(19), "Excelente")

    def test_clasificar_nota_bueno(self):
        self.assertEqual(self.calc.clasificar_nota(16), "Bueno")

    def test_clasificar_nota_aprobado(self):
        self.assertEqual(self.calc.clasificar_nota(12), "Aprobado")

    def test_clasificar_nota_desaprobado(self):
        self.assertEqual(self.calc.clasificar_nota(8), "Desaprobado")

    def test_clasificar_nota_fuera_de_rango(self):
        with self.assertRaises(ValueError):
            self.calc.clasificar_nota(-5)
        with self.assertRaises(ValueError):
            self.calc.clasificar_nota(25)

if __name__ == "__main__":
    unittest.main()