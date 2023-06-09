from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from app.settings import BASE_DIR

engine = create_engine(f'sqlite:///{BASE_DIR}/db.db')
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    from app.recognizer.models import Face
    Base.metadata.create_all(bind=engine)