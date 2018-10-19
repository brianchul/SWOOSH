from sqlalchemy import create_engine, MetaData
from config.DBindex import init_db, engine

metadata=MetaData(engine)