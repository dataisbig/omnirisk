import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Vehicle(Base):
    __tablename__ = 'vehicles'
    vin = Column(String(250), primary_key=True, autoincrement=False)
    make = Column(String(250), nullable=True)
    model = Column(String (250), nullable=False)
    year = Column(Integer, nullable=True)
    plant_city = Column(String(250), nullable=True)
    plant_state = Column(String(250), nullable=True)
    plant_country = Column(String(250), nullable=True)
    engine = Column(String(250), nullable=True)
    body_class = Column(String(250), nullable=True)
    brake_system = Column(String(250), nullable=True)
    drive_type = Column(String(250), nullable=True)
    notes = Column(String(250), nullable=True)


class Accident(Base):
    __tablename__ = 'accidents'
    id = Column(Integer, primary_key=True)
    report_number = Column(String(250), nullable=False)
    report_seq_num = Column(Integer, nullable=False)
    dot_number = Column(String(250), nullable=False)
    accident_date = Column(Date, nullable=False)
    state = Column(String(250), nullable=False)
    fatalities = Column(Integer, nullable=True)
    injuries = Column(Integer, nullable=True)
    tow_away = Column(Integer, nullable=True)
    hazmat = Column(String(250), nullable=True)
    trafficway_description = Column(String(250), nullable=True)
    access_control = Column(String(250), nullable=True)
    road_surface_cond = Column(String(250), nullable=True)
    weather = Column(String(250), nullable=True)
    light_cond = Column(String(250), nullable=True)
    vin = Column(String(250), nullable=True)
    license_num = Column(String(250), nullable=True)
    license_state = Column(String(250), nullable=True)
    severity_weight = Column(Integer, nullable=True)
    time_weight = Column(Integer, nullable=True)
    citation_issued = Column(String(250), nullable=True)
    sequence_num = Column(String(250), nullable=True)




def main():

<<<<<<< HEAD
def main():

    # Create an engine that stores data in the local directory's
    # sqlalchemy_example.db file.
    engine = create_engine ('mysql+pymysql://alex:tygrcnt@127.0.0.1/adas')

    # Create all tables in the engine. This is equivalent to "Create Table"
    # statements in raw SQL.
    Base.metadata.create_all(engine)
=======
    # Create an engine that stores data in the local directory's
    # sqlalchemy_example.db file.
    engine = create_engine ('mysql+pymysql://alex:tygrcnt@127.0.0.1/adas')

    # Create all tables in the engine. This is equivalent to "Create Table"
    # statements in raw SQL.
    Base.metadata.create_all(engine)

>>>>>>> 350c32beb75e5e26126de1811d7c1a56031f5f09
