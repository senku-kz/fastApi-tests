from fastapi import FastAPI
from app.models import QuadraticInput, QuadraticOutput
from app.services import solve_quadratic


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
def say_hello(name: str):
    """
    >>> say_hello('Senku')
    {'message': 'Hello Senku'}

    >>> say_hello("")
    {'message': 'Hello '}
    >>> say_hello("@user123")
    {'message': 'Hello @user123'}

    >>> say_hello("12345")
    {'message': 'Hello 12345'}

    >>> say_hello("John Doe")
    {'message': 'Hello John Doe'}

    >>> say_hello("a" * 1000)
    {'message': 'Hello ' + 'a' * 1000}

    >>> say_hello(" Alice ")
    {'message': 'Hello  Alice '}
    """
    return {"message": f"Hello {name}"}


@app.post("/solve", response_model=QuadraticOutput)
async def solve(input_data: QuadraticInput):
    solution = solve_quadratic(input_data.a, input_data.b, input_data.c)
    return {"solution": solution}
