from sqlalchemy import Column, Integer, String, DateTime, Float, Boolean
from weatherstation.data_base.connect_database import Base, engine

"""Create table in database."""
class Temperature(Base):
    __tablename__ = 'Temperature'
    id = Column(Integer, primary_key=True)
    date = Column(DateTime, nullable=False)
    temperature = Column(Float, nullable=False)
 
class Humidity(Base):
    __tablename__ = 'Humidity'
    id = Column(Integer, primary_key=True)
    date = Column(DateTime, nullable=False)
    humidity = Column(Float, nullable=False)

class AirPressure(Base):
    __tablename__ = 'AirPressure'
    id = Column(Integer, primary_key=True)
    date = Column(DateTime, nullable=False)
    air_pressure = Column(Float, nullable=False)

class Height(Base):
    __tablename__ = 'Height'
    id = Column(Integer, primary_key=True)
    date = Column(DateTime, nullable=False)
    height = Column(Float, nullable=False)

class RainFall(Base):
    __tablename__ = 'RainFall'
    id = Column(Integer, primary_key=True)
    date = Column(DateTime, nullable=False)
    precipitation = Column(Boolean, nullable=False)
    amount_of_rainfall = Column(Float, nullable=False)

class LightInstesity(Base):
    __tablename__ = 'LightInstesity'
    id = Column(Integer, primary_key=True)
    date = Column(DateTime, nullable=False)
    light_instesity = Column(Integer, nullable=False)

class Measurements(Base):
    __tablename__ = 'Measurements'
    id = Column(Integer, primary_key=True)
    date = Column(DateTime, nullable=False)
    min_temperature = Column(String, nullable=False)
    max_temperature = Column(String, nullable=False)
    min_humidity = Column(String, nullable=False)
    max_humidity = Column(String, nullable=False)
    min_pressure = Column(String, nullable=False)
    max_pressure = Column(String, nullable=False)
    min_light_instesity = Column(String, nullable=False)
    max_light_instesity = Column(String, nullable=False)
    average_height = Column(String, nullable=False)
    precipitation = Column(Boolean, nullable=False)
    max_amount_of_rainfall = Column(String, nullable=False)
    average_amount_of_rainfall = Column(String, nullable=False)
    
Base.metadata.create_all(engine)
TEMPORARYTABLES = ["Temperature", "Humidity", "AirPressure", "Height", "RainFall", "LightInstesity"]
