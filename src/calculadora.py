class Calculadora:
    """Calculadora con operaciones y validaciones."""
    
    def sumar(self, a, b):
        return a + b

    def restar(self, a, b):
        return a - b

    def multiplicar(self, a, b):
        return a * b

    def dividir(self, a, b):
        if b == 0:
            raise ValueError("No se puede dividir entre cero")
        return a / b

    def potencia(self, base, exponente):
        if exponente < 0:
            raise ValueError("Exponente negativo no soportado")
        resultado = 1
        for _ in range(exponente):
            resultado *= base
        return resultado

    def es_par(self, n):
        return n % 2 == 0

    def factorial(self, n):
        if n < 0:
            raise ValueError("No existe factorial de negativos")
        if n == 0 or n == 1:
            return 1
        resultado = 1
        for i in range(2, n + 1):
            resultado *= i
        return resultado

    def promedio(self, numeros):
        if not numeros:
            raise ValueError("Lista vacia")
        return sum(numeros) / len(numeros)

    def maximo(self, numeros):
        if not numeros:
            raise ValueError("Lista vacia")
        max_val = numeros[0]
        for n in numeros[1:]:
            if n > max_val:
                max_val = n
        return max_val

    def clasificar_nota(self, nota):
        if nota < 0 or nota > 20:
            raise ValueError("Nota fuera de rango (0-20)")
        if nota >= 18:
            return "Excelente"
        elif nota >= 15:
            return "Bueno"
        elif nota >= 11:
            return "Aprobado"
        else:
            return "Desaprobado"
        