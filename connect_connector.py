import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.pool import StaticPool

# Create an in-memory SQLite database
engine = sqlalchemy.create_engine(
    "sqlite:///:memory:", 
    echo=False, 
    connect_args={'check_same_thread': False}, 
    poolclass=StaticPool
)

# Create a sessionmaker class to create new sessions
SessionMaker = sqlalchemy.orm.sessionmaker(bind=engine)

# Create a Base class for ORM
Base = declarative_base()
