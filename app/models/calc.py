# *** imports

# ** infra
from tiferet.models import *


# *** models

# ** model: number
class Number(ValueObject):
    '''
    A value object representing a numerical value in the calculator domain.
    '''
    value = StringType(
        required=True,
        regex=r'^-?\d*\.?\d*$',
        metadata=dict(
            description='A string representing an integer or float (e.g., "123", "-123.45", "0123", ".123", "123.").'
        )
    )

    def is_float(self) -> bool:
        '''
        Check if the value is formatted as a float.

        :return: True if the value contains a decimal point and valid digits, False otherwise.
        '''
        return '.' in self.value and self.value.strip('-.').replace('.', '').isdigit()

    def format(self) -> int | float:
        '''
        Convert the string value to an integer or float.

        :return: An integer if the value represents a whole number, otherwise a float.
        '''
        if self.is_float():
            return float(self.value)
        return int(self.value)