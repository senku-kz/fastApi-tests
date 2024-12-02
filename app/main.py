from fastapi import FastAPI
from app.models import QuadraticInput, QuadraticOutput
from app.services import solve_quadratic


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.post("/solve", response_model=QuadraticOutput)
async def solve(input_data: QuadraticInput):
    solution = solve_quadratic(input_data.a, input_data.b, input_data.c)
    return {"solution": solution}
