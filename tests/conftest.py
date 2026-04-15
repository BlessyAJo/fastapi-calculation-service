import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from app.database import Base, SessionLocal, get_db, get_engine, get_sessionmaker
from main import app
import logging
from faker import Faker
from app.models.user import User
from app.models.calculation import Calculation, Addition, Subtraction, Multiplication, Division
import uuid
from app.core.config import settings
from contextlib import contextmanager
from typing import Generator
logger = logging.getLogger(__name__)
fake = Faker()
Faker.seed(12345)

logger.info(f"Using database URL: {settings.DATABASE_URL}")

# Create an engine and sessionmaker based on DATABASE_URL using factory functions
test_engine = get_engine(database_url=settings.DATABASE_URL)
TestingSessionLocal = get_sessionmaker(engine=test_engine)

@pytest.fixture()
def db():
    connection = test_engine.connect()
    transaction = connection.begin()

    session = SessionLocal(bind=connection)

    yield session

    session.close()

    if transaction.is_active:
        transaction.rollback()

    connection.close()

@pytest.fixture(scope="session", autouse=True)
def setup_db():
    Base.metadata.create_all(bind=test_engine)
@pytest.fixture
def db_session(request) -> Generator[Session, None, None]:

    session = TestingSessionLocal()
    try:
        yield session
    finally:
        logger.info("db_session teardown: about to truncate tables.")
        preserve_db = request.config.getoption("--preserve-db")
        if preserve_db:
            logger.info("Skipping table truncation due to --preserve-db flag.")
        else:
            logger.info("Truncating all tables now.")
            for table in reversed(Base.metadata.sorted_tables):
                logger.info(f"Truncating table: {table}")
                session.execute(table.delete())
            session.commit()
        session.close()
        logger.info("db_session teardown: done.")
@contextmanager
def managed_db_session():

    session = TestingSessionLocal()
    try:
        yield session
    except SQLAlchemyError as e:
        logger.error(f"Database error: {str(e)}")
        session.rollback()
        raise
    finally:
        session.close()


@pytest.fixture
def client():
    return TestClient(app)

@pytest.fixture()
def test_user(db):
    user = User(
        id=uuid.uuid4(),
        username=f"user_{uuid.uuid4()}",
        email=f"test_{uuid.uuid4()}@test.com"
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user