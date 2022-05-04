import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.config import settings
from app.main import app
from app.database import get_db, Base
from fastapi.testclient import TestClient


SQLALCHEMY_DATABASE_URL = f'{settings.DATABASE_TYPE}://' \
                          f'{settings.DATABASE_USERNAME}:' \
                          f'{settings.DATABASE_PASSWORD}@' \
                          f'{settings.DATABASE_HOSTNAME}:' \
                          f'{settings.DATABASE_PORT}/' \
                          f'{settings.DATABASE_NAME}_test_db'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture()
def session():
    print("my session fixture ran")
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


@pytest.fixture()
def client(session):
    def override_get_db():
        try:
            yield session
        finally:
            session.close()
    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)
