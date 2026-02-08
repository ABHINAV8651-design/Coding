"""
A scientific calculator application with basic and advanced mathematical operations.
"""

import math


class Calculator:
    """A simple calculator class for basic arithmetic operations."""

    @staticmethod
    def add(a, b):
        """Add two numbers."""
        return a + b

    @staticmethod
    def subtract(a, b):
        """Subtract two numbers."""
        return a - b

    @staticmethod
    def multiply(a, b):
        """Multiply two numbers."""
        return a * b

    @staticmethod
    def divide(a, b):
        """Divide two numbers."""
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

    @staticmethod
    def power(a, b):
        """Raise a number to a power."""
        return a ** b

    @staticmethod
    def modulo(a, b):
        """Get the remainder of division."""
        if b == 0:
            raise ValueError("Cannot perform modulo by zero")
        return a % b

    # Trigonometric Functions (Degree mode)
    @staticmethod
    def sin_deg(angle_deg):
        """Calculate sine of an angle in degrees."""
        return math.sin(math.radians(angle_deg))

    @staticmethod
    def cos_deg(angle_deg):
        """Calculate cosine of an angle in degrees."""
        return math.cos(math.radians(angle_deg))

    @staticmethod
    def tan_deg(angle_deg):
        """Calculate tangent of an angle in degrees."""
        return math.tan(math.radians(angle_deg))

    # Trigonometric Functions (Radian mode)
    @staticmethod
    def sin_rad(angle_rad):
        """Calculate sine of an angle in radians."""
        return math.sin(angle_rad)

    @staticmethod
    def cos_rad(angle_rad):
        """Calculate cosine of an angle in radians."""
        return math.cos(angle_rad)

    @staticmethod
    def tan_rad(angle_rad):
        """Calculate tangent of an angle in radians."""
        return math.tan(angle_rad)

    # Inverse Trigonometric Functions (returns degrees)
    @staticmethod
    def asin_deg(x):
        """Calculate arcsine and return result in degrees."""
        if x < -1 or x > 1:
            raise ValueError("asin domain error: input must be between -1 and 1")
        return math.degrees(math.asin(x))

    @staticmethod
    def acos_deg(x):
        """Calculate arccosine and return result in degrees."""
        if x < -1 or x > 1:
            raise ValueError("acos domain error: input must be between -1 and 1")
        return math.degrees(math.acos(x))

    @staticmethod
    def atan_deg(x):
        """Calculate arctangent and return result in degrees."""
        return math.degrees(math.atan(x))

    # Inverse Trigonometric Functions (returns radians)
    @staticmethod
    def asin_rad(x):
        """Calculate arcsine and return result in radians."""
        if x < -1 or x > 1:
            raise ValueError("asin domain error: input must be between -1 and 1")
        return math.asin(x)

    @staticmethod
    def acos_rad(x):
        """Calculate arccosine and return result in radians."""
        if x < -1 or x > 1:
            raise ValueError("acos domain error: input must be between -1 and 1")
        return math.acos(x)

    @staticmethod
    def atan_rad(x):
        """Calculate arctangent and return result in radians."""
        return math.atan(x)

    # Hyperbolic Functions
    @staticmethod
    def sinh(x):
        """Calculate hyperbolic sine."""
        return math.sinh(x)

    @staticmethod
    def cosh(x):
        """Calculate hyperbolic cosine."""
        return math.cosh(x)

    @staticmethod
    def tanh(x):
        """Calculate hyperbolic tangent."""
        return math.tanh(x)

    # Logarithmic Functions
    @staticmethod
    def log10(x):
        """Calculate base-10 logarithm."""
        if x <= 0:
            raise ValueError("log domain error: input must be positive")
        return math.log10(x)

    @staticmethod
    def ln(x):
        """Calculate natural logarithm (base e)."""
        if x <= 0:
            raise ValueError("ln domain error: input must be positive")
        return math.log(x)

    @staticmethod
    def log_base(x, base):
        """Calculate logarithm with custom base."""
        if x <= 0:
            raise ValueError("log domain error: input must be positive")
        if base <= 0 or base == 1:
            raise ValueError("log domain error: base must be positive and not equal to 1")
        return math.log(x, base)

    # Power and Root Functions
    @staticmethod
    def sqrt(x):
        """Calculate square root."""
        if x < 0:
            raise ValueError("sqrt domain error: input must be non-negative")
        return math.sqrt(x)

    @staticmethod
    def cbrt(x):
        """Calculate cube root."""
        if x < 0:
            return -(-x) ** (1/3)
        return x ** (1/3)

    @staticmethod
    def reciprocal(x):
        """Calculate reciprocal (1/x)."""
        if x == 0:
            raise ValueError("Cannot divide by zero")
        return 1 / x

    @staticmethod
    def square(x):
        """Calculate square of a number."""
        return x ** 2

    @staticmethod
    def cube(x):
        """Calculate cube of a number."""
        return x ** 3

    # Factorial
    @staticmethod
    def factorial(n):
        """Calculate factorial of a number."""
        if not isinstance(n, int) or n < 0:
            raise ValueError("Factorial domain error: input must be a non-negative integer")
        return math.factorial(n)

    # Other Functions
    @staticmethod
    def absolute(x):
        """Calculate absolute value."""
        return abs(x)

    @staticmethod
    def negate(x):
        """Negate a number."""
        return -x

    # Constants
    @staticmethod
    def get_pi():
        """Return the value of pi."""
        return math.pi

    @staticmethod
    def get_e():
        """Return the value of e."""
        return math.e


def main():
    """Main function to run the calculator interface."""
    calc = Calculator()
    
    print("=== Simple Calculator ===")
    print("Operations: +, -, *, /, **, %")
    print("Type 'exit' to quit\n")
    
    while True:
        try:
            user_input = input("Enter expression (e.g., 10 + 5): ").strip()
            
            if user_input.lower() == 'exit':
                print("Goodbye!")
                break
            
            # Parse the input
            tokens = user_input.split()
            
            if len(tokens) != 3:
                print("Invalid input. Please enter: number operator number\n")
                continue
            
            num1 = float(tokens[0])
            operator = tokens[1]
            num2 = float(tokens[2])
            
            # Perform calculation
            if operator == '+':
                result = calc.add(num1, num2)
            elif operator == '-':
                result = calc.subtract(num1, num2)
            elif operator == '*':
                result = calc.multiply(num1, num2)
            elif operator == '/':
                result = calc.divide(num1, num2)
            elif operator == '**':
                result = calc.power(num1, num2)
            elif operator == '%':
                result = calc.modulo(num1, num2)
            else:
                print(f"Unknown operator: {operator}\n")
                continue
            
            print(f"Result: {result}\n")
        
        except ValueError as e:
            print(f"Error: {e}\n")
        except ZeroDivisionError:
            print("Error: Cannot divide by zero\n")
        except Exception as e:
            print(f"Error: Invalid input - {e}\n")


if __name__ == "__main__":
    main()
