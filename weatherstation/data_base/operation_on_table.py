from sqlalchemy import func
from sqlalchemy.orm import sessionmaker 
from weatherstation.data_base.connect_database import engine

Session = sessionmaker(bind=engine)
session = Session()

def insert_value(table_name, session=session, **kwargs):
    """Insert value on table."""
    session.add(table_name(**kwargs))
    session.commit()

def get_max_column(column, session=session):
    """Return max data in column."""
    return session.query(func.max(column)).scalar()

def get_min_column(column, session=session):
    """Return min data in column."""
    return session.query(func.min(column)).scalar()

def get_avg_column(column, session=session):
    """Return avg data in column."""
    return session.query(func.avg(column)).scalar()

def clear_table(tables, session=session):
    """Clear data in column"""
    for table in tables:
        session.execute('''TRUNCATE TABLE "{}"'''.format(table))
    session.commit()
    session.close()