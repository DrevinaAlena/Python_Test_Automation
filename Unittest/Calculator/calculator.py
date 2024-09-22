import math

class Calculator:
    def add(self, a, b):
        """addition"""
        return a + b

    def multiply(self, a, b):
        """multiplication"""
        return a * b

    def subtract(self, a, b):
        """subtraction"""
        return a - b

    def divide(self, a, b):
        """division"""
        if b != 0:
            return a / b
        else:
            return 'Error: Division by zero'

    def sqrt(self, number):
        """square root of number"""
        return math.sqrt(number)

    def pi(self):
        """constant π."""
        return math.pi