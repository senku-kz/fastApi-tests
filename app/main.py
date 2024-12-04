from fastapi import FastAPI
from app.routers import case_1_hello, case_2_solve

app = FastAPI()

# Подключение маршрутов
app.include_router(case_1_hello.router, prefix="/greetings", tags=["Greetings"])
app.include_router(case_2_solve.router, prefix="/math", tags=["Math"])
