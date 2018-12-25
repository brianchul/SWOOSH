from sqlalchemy import create_engine, Column, Integer, DateTime, func
from sqlalchemy.orm import scoped_session, sessionmaker
from .conf import Config
from flask_sqlalchemy import Model, DefaultMeta
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine(Config.db, echo=False)

db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))


class Default_base(Model):
    __abstract__ = True

    id = Column(Integer, primary_key=True, autoincrement=True)
    created_time = Column(DateTime(), default=func.now())
    updated_time = Column(
        DateTime(), default=func.now(), onupdate=func.now()
        )


Base = declarative_base(cls=Default_base, name='Default',
                        metaclass=DefaultMeta)
#Base = declarative_base(Default_base())
Base.query = db_session.query_property()


def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    from models import mission, client, timeline, order, rocket, location
    Base.metadata.create_all(bind=engine)


# def drop_db():
#     from models import mission, client, timeline, order, rocket, location
#     Base.metadata.drop_all(bind=engine)