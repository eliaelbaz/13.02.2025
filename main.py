from adapter_float_int import AdapterFloat2Int
from factorial_calc import FactorialCalculator


def print_factorial_number(calculator, number):
    print(calculator.calc_factorial(number))


if __name__ == "__main__":
    print_factorial_number(FactorialCalculator(), 5)
    print_factorial_number(AdapterFloat2Int(), 3.0)
