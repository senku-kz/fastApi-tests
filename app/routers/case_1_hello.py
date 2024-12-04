from fastapi import APIRouter


router = APIRouter()


@router.get("/")
async def root():
    return {"message": "Hello World"}


@router.get("/hello/{name}")
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
