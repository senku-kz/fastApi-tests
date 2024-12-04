import pytest
import json
from datetime import datetime
from app.models.case_3_sqlalchemy_models import User
from tests.database import TestSessionLocal, Base, test_engine


# Подготовка базы данных перед тестами
@pytest.fixture(scope="module")
def db():
    # Создаем тестовую базу данных
    Base.metadata.create_all(bind=test_engine)
    db = TestSessionLocal()

    # Загружаем данные из файла в базу
    with open("tests/test_data.json", "r") as f:
        data = json.load(f)
        for item in data:
            if item["birthdate"]:  # Преобразуем только, если дата указана
                item["birthdate"] = datetime.strptime(item["birthdate"], "%Y-%m-%d").date()
            db.add(User(**item))
    db.commit()

    yield db
    db.close()
    Base.metadata.drop_all(bind=test_engine)


def test_read_user_by_id(db):
    user = db.query(User).filter(User.id == 1).first()
    assert user is not None
    assert user.firstname == "Ivan"


def test_read_nonexistent_user(db):
    user = db.query(User).filter(User.id == 999).first()
    assert user is None


def test_filter_users_by_city(db):
    users = db.query(User).filter(User.city == "Astana").all()
    assert len(users) == 1
    assert users[0].surname == "Ivanov"


def test_users_with_missing_data(db):
    user = db.query(User).filter(User.secondname == None).first()
    assert user is not None
    assert user.surname == "Smith"


def test_count_users_in_db(db):
    users_count = db.query(User).count()
    assert users_count == 10
