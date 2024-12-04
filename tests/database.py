from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models.database import Base

# Тестовая база данных в памяти
SQLALCHEMY_TEST_DATABASE_URL = "sqlite:///:memory:"

test_engine = create_engine(SQLALCHEMY_TEST_DATABASE_URL, connect_args={"check_same_thread": False})
TestSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=test_engine)

# Создаем таблицы в тестовой базе
Base.metadata.create_all(bind=test_engine)
