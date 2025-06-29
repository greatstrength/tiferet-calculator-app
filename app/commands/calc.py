# *** imports

# ** infra
from tiferet.commands import *

# ** app
from ..models.calc import Number

class AddNumber(Command):
    '''
    A command to perform addition of two numbers.
    '''
    def execute(self, a: Number, b: Number, **kwargs) -> Number:
        '''
        Execute the addition command.

        :param a: A Number object representing the first number.
        :type a: Number
        :param b: A Number object representing the second number.
        :type b: Number
        :param kwargs: Additional keyword arguments.
        :type kwargs: dict
        :return: A Number object representing the sum of a and b.
        :rtype: Number
        '''

        # Add formatted values of a and b.
        result = a.format() + b.format()

        # Return a new Number object with the result.
        return result

class SubtractNumber(Command):
    '''
    A command to perform subtraction of two numbers.
    '''
    def execute(self, a: Number, b: Number, **kwargs) -> Number:
        '''
        Execute the subtraction command.

        :param a: A Number object representing the first number.
        :type a: Number
        :param b: A Number object representing the second number.
        :type b: Number
        :param kwargs: Additional keyword arguments.
        :type kwargs: dict
        :return: A Number object representing the difference of a and b.
        :rtype: Number
        '''
        
        # Subtract formatted values of b from a.
        result = a.format() - b.format()

        # Return a new Number object with the result.
        return result

class MultiplyNumber(Command):
    '''
    A command to perform multiplication of two numbers.
    '''
    def execute(self, a: Number, b: Number, **kwargs) -> Number:
        '''
        Execute the multiplication command.

        :param a: A Number object representing the first number.
        :type a: Number
        :param b: A Number object representing the second number.
        :type b: Number
        :param kwargs: Additional keyword arguments.
        :type kwargs: dict
        :return: A Number object representing the product of a and b.
        :rtype: Number
        '''
        
        # Multiply the formatted values of a and b.
        result = a.format() * b.format()

        # Return a new Number object with the result.
        return result

class DivideNumber(Command):
    '''
    A command to perform division of two numbers.
    '''
    def execute(self, a: Number, b: Number, **kwargs) -> Number:
        '''
        Execute the division command.

        :param a: A Number object representing the first number.
        :type a: Number
        :param b: A Number object representing the second number, must be non-zero.
        :type b: Number
        :param kwargs: Additional keyword arguments.
        :type kwargs: dict
        :return: A Number object representing the quotient of a and b.
        :rtype: Number
        '''
        # Check if b is zero to avoid division by zero.
        self.verify(b.format() != 0, 'DIVISION_BY_ZERO')

        # Divide the formatted values of a by b.
        result = a.format() / b.format()

        # Return a new Number object with the result.
        return result


class ExponentiateNumber(Command):
    '''
    A command to perform exponentiation of two numbers.
    '''
    def execute(self, a: Number, b: Number, **kwargs) -> Number:
        '''
        Execute the exponentiation command.

        :param a: A Number object representing the base number.
        :type a: Number
        :param b: A Number object representing the exponent.
        :type b: Number
        :param kwargs: Additional keyword arguments.
        :type kwargs: dict
        :return: A Number object representing a raised to the power of b.
        :rtype: Number
        '''
        
        # Exponentiate the formatted value of a by b.
        result = a.format() ** b.format()

        # Return a new Number object with the result.
        return result