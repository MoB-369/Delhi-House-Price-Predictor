'''
This file implements the custom exception handling code.
For this we use sys library as it provides us error details.

First we have implemented an error_message_detail() function.
It takes two arguments the error and error_detail.
we generate a custom error message from it and return that.

Then we have our CustomException class.

'''

import sys
from src.logger import logging
def error_message_detail(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message="Error occured in python script name [{0}] line number [{1}] error message[{2}]".format(
        file_name,exc_tb.tb_lineno,str(error)
    )

    return error_message

class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys ):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message,error_detail=error_detail)
    def __str__(self):
        return self.error_message