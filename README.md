# Require packages
pip install pytest httpx

pip freeze > requirements.txt

pip install -r requirements.txt


# Run project
uvicorn app.main:app --reload

# Run tests
pytest tests/

# Run tests in verbose mode
pytest -v tests/