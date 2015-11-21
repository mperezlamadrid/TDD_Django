import unittest
from calculadora import Calculadora

class CalculadoraTest(unittest.TestCase):

    # Retorna la suma de dos numeros
    def suma_test(self):
        calc = Calculadora()
        result = calc.suma(2,5)
        self.assertEqual(result, 7)

    # Retorna la multiplicacion de dos numeros
    def multiplicacion_test(self):
        calc = Calculadora()
        result = calc.multiplica(3,5)
        self.assertEqual(result, 15)

    # Retorna FALSE si el primer numero es mayor que el ultimo
    def mayor_igual_que_test_return_false(self):
        calc = Calculadora()
        result = calc.mayor_igual_que(3,5)
        self.assertFalse(result)

    # Retorna TRUE si el primer numero es mayor que el ultimo
    def mayor_igual_que_test_return_true(self):
        calc = Calculadora()
        result = calc.mayor_igual_que(10,5)
        self.assertTrue(result)

    # Retorna PAR
    def par_impar_test(self):
        calc = Calculadora()
        result = calc.par_impar(10)
        self.assertEqual(result, "PAR")

    # Retorna IMPAR
    def par_impar_test(self):
        calc = Calculadora()
        result = calc.par_impar(11)
        self.assertEqual(result, "IMPAR")

# if __name__ == '__main__':
#     unittest.main()
