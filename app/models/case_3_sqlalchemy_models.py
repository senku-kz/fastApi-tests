from sqlalchemy import Column, Integer, String, Date
from app.models.database import Base


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
