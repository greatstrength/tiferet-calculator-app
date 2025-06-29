from tiferet.commands import *
from ..models.calc import Number

class ValidateNumber(Command):
    '''
    A command to validate that a value can be a Number object.
    '''
    def execute(self, value: str, **kwargs) -> None:
        '''
        Validate that the input value can be used to create a Number object.

        :param value: Any string value to validate.
        :type value: str
        :param kwargs: Additional keyword arguments.
        :type kwargs: dict
        :raises TiferetError: If the value cannot be a Number.
        '''
        try:
            return ModelObject.new(Number, value=str(value))
        except Exception as e:
            self.verify(False, 'INVALID_INPUT', value)