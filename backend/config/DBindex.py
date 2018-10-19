from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import create_engine
import config

# engine = create_engine("mysql+pymysql://precoo:Nasa2018@104.196.179.255/project",echo=True)
engine = create_engine(config.db, echo=True)

db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    from models import mission, client, timeline, order, rocket, location
    Base.metadata.create_all(bind=engine)


def drop_db():
    import models
    Base.metadata.drop_all(bind=engine)