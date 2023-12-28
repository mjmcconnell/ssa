# third-party imports
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine("sqlite:///database.sqlite3")
db_session = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine)
)

ModelBase = declarative_base()
ModelBase.query = db_session.query_property()
