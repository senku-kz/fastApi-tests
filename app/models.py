from typing import Union, List
from pydantic import BaseModel

from sqlalchemy import Column, Integer, String, Date, create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


class QuadraticInput(BaseModel):
    a: float
    b: float
    c: float


class QuadraticOutput(BaseModel):
    solution: Union[str, List[float]]


Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    iin = Column(String(12), unique=True, nullable=True, index=True)
    surname = Column(String, nullable=False)
    firstname = Column(String, nullable=False)
    secondname = Column(String, nullable=True)
    birthdate = Column(Date, nullable=True)
    sex = Column(String, nullable=True)
    city = Column(String, nullable=False)


DATABASE_URL = "sqlite:///./my_app.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Создание таблиц
Base.metadata.create_all(bind=engine)
