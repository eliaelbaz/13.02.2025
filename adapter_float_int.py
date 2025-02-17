from factorial_calc import FactorialCalculator

class AdapterFloat2Int:
    def calc_factorial(self, float_number):
        int_number = int(float_number)
        return FactorialCalculator().calc_factorial(int_number)
