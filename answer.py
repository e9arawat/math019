"""importing solver function from solver file"""
from solver import solver
from datetime import date
def answer():
    """calling solver function"""
    return solver(date(1901, 1, 1), date(2000, 12, 31))

if __name__ == "__main__":
    print(answer())