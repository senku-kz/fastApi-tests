from fastapi import APIRouter
from app.models.case_2_pydantic_models import QuadraticInput, QuadraticOutput
from app.services import solve_quadratic


router = APIRouter()


@router.post("/solve", response_model=QuadraticOutput)
async def solve(input_data: QuadraticInput):
    solution = solve_quadratic(input_data.a, input_data.b, input_data.c)
    return {"solution": solution}
