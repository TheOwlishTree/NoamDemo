from enum import Enum
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

# class Arithmetic_Operation(Enum):
#     SUBTRACT = lambda x, y: x - y
#     MULTIPLY = lambda x, y: x * y
#     ADDITION = lambda x, y: x + y
#     DIVISION = lambda x, y : x / y if x != 0 else: raise ZeroDivisionError
