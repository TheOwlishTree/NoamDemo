""" Added args and kwargs for future implementation, if you wish to add color to the function, be my guest """
from fastapi import HTTPException


async def addition(x, y, *args, **kwargs):
    return float(x) + float(y)


async def substraction(x, y, *args, **kwargs):
    return float(x) - float(y)


async def multiplication(x, y, *args, **kwargs):
    return float(x) * float(y)


async def division(x, y, *args, **kwargs):
    if float(y) != 0:
        return float(x) / float(y)
    raise HTTPException(status_code=400, detail="Cannot divide by zero")

# The best implementation, does not support multi-method (get/post) and isn't type fluid (can't send str, must always be
# int for numbers, or it will fail).
# class Arithmetic_Operation(Enum):
#     SUBTRACT = lambda x, y: x - y
#     MULTIPLY = lambda x, y: x * y
#     ADDITION = lambda x, y: x + y
#     DIVISION = lambda x, y : x / y
