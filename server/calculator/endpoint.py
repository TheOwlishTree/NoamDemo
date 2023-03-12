"""
Since I did not complete the frontend portion, I implemented both a get and post endpoint for calculator, for future use
"""
from fastapi import APIRouter, HTTPException
from server.calculator.bl import addition, substraction, division, multiplication
from server.calculator.model import Equation

from logging import getLogger
log = getLogger(__name__)

calc_router = APIRouter()

@calc_router.post("/")
async def calc_post(equation: Equation):
    """ Calculator endpoint using a post method """
    try:
        if equation.operator == "+" :
            return await addition(equation.num_1, equation.num_2)

        elif equation.operator == "-":
            return await substraction(equation.num_1, equation.num_2)

        elif equation.operator == "*":
            return await multiplication(equation.num_1, equation.num_2)

        elif equation.operator == "/":
            return await division(equation.num_1, equation.num_2)
        else:
            raise HTTPException(status_code=400, detail="Invalid Operation. You're allow to use only +, -, *, /")
    except HTTPException as e:
        log.warning(f"An error occured. status code = {e.status_code}, message={e.detail}, request={equation}")
        raise


@calc_router.get("/")
async def calc_get(eq: str):
    """ Calculator endpoint using get method - recieved as string, whitespace not relevant"""
    try:
        # easy mode
        # return eval(equation)
        if "+" in eq:
            eq = eq.split("+")
            return await addition(eq[0], eq[1])

        elif "-" in eq:
            eq = eq.split("-")
            return await substraction(eq[0], eq[1])

        elif "*" in eq:
            eq = eq.split("*")
            return await multiplication(eq[0], eq[1])

        elif "/" in eq:
            eq = eq.split("/")
            return await division(eq[0], eq[1])
        else:
            raise HTTPException(status_code=400, detail="Invalid Operation. You're allow to use only +, -, *, /")
    except HTTPException as e:
        log.warning(f"An error occured. status code = {e.status_code}, message={e.detail}, request={eq}")
        raise


