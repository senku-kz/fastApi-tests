from typing import Union, List
from pydantic import BaseModel


class QuadraticInput(BaseModel):
    a: float
    b: float
    c: float


class QuadraticOutput(BaseModel):
    solution: Union[str, List[float]]
