from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from weatherstation.data_base.settings_data_base import DATABASE

dbtype = DATABASE['type']
user = DATABASE['user']
password = DATABASE['password']
localhost = DATABASE['localhost']
data_base_name = DATABASE['database_name']

#CONNECT = f'{dbtype}://{user}:{password}@{localhost}/{data_base_name}'
CONNECT = dbtype + '://' + user + ':' + password + '@' + localhost + '/' + data_base_name
engine = create_engine(CONNECT)
Base = declarative_base()
