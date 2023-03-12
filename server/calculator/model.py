from pydantic import BaseModel

class Equation(BaseModel):
    operator: str
    num_1: int
    num_2: int
