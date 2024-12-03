# Solve quadratic
## Require packages
pip install pytest httpx

pip freeze > requirements.txt

pip install -r requirements.txt


## Run project
uvicorn app.main:app --reload

## Run tests
pytest tests/

## Run tests in verbose mode
pytest -v tests/

## Run doctest
python -m doctest -v app/main.py

# Work with test db
## Require packages
pip install sqlalchemy pytest

## Run tests in verbose mode
pytest tests/test_api_db.py -v
