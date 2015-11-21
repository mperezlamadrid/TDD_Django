class Calculadora(object):

    def suma(self, x, y):
        return x + y

    def multiplica(self, x, y):
        return x * y

    def mayor_igual_que(self, x, y):
        return x >= y

    def par_impar(self, x):
        if x%2==0:
            return "PAR"
        else:
            return "IMPAR"
