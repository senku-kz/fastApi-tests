# Run project
uvicorn app.main:app --reload


# Require packages
pip install -r requirements.txt

pip freeze > requirements.txt

## Work with pytest lib
pip install pytest httpx

## Work with test db
pip install sqlalchemy pytest


# Case 1: Greetings
## Run doctest
python -m doctest -v app/main.py


# Case 2: Solve quadratic
## Run pytest
pytest tests/

## Run pytest in verbose mode
pytest tests/case_2_solve.py -v


# Case 3: Work with test db
## Run pytest in verbose mode
pytest tests/case_3_sqlalchemy.py -v
