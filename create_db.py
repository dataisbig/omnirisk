import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Time, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine


"""
accident schema fields defined at https://ask.fmcsa.dot.gov/app/mcmiscatalog/d_crash1
vehicle and carrier fields populated from vpic database and from QCmobil API
"""

Base = declarative_base()




class Accident(Base):

    __tablename__ = 'accident'
    id = Column (Integer, primary_key=True)
    crash_event_id = Column (String (8), nullable=False)
    crash_id = Column(String (8), nullable=False)
    sequence_num = Column(Integer, nullable=False)
    event_id  = Column(String(8), nullable=False)
    event_other_desc = Column(String(50), nullable=False)


class AccidentCarrier(Base):

    __tablename__ = 'accident_carrier'
    id = Column(Integer, primary_key=True)
    crash_id = Column(String(8), nullable=False)
    crash_carrier_id = Column(String(8), nullable=False)
    carrier_name_source = Column(String(1), nullable=False)
    carrier_name = Column(String(120), nullable=True)
    carrier_street = Column(String(50), nullable=True)
    carrier_city = Column(String(25), nullable=True)
    carrier_city_code = Column(String(5), nullable=True)
    carrier_state = Column(String(2), nullable=True)
    carrier_zip = Column(String(10), nullable=True)
    colonia = Column(String(25), nullable=True)
    prefix = Column(String(2), nullable=True)
    docket_num = Column(String(8), nullable=True)
    interstate = Column(String(1), nullable=True)
    no_id_flag = Column(String(1), nullable=True)
    state_num = Column(String(12), nullable=True)
    state_issuing_num = Column(String(2), nullable=True)


class AccidentMaster(Base):

    __tablename__ = 'accident_master'
    id = Column(Integer, primary_key=True)
    crash_id = Column(String(8), nullable=False)
    report_state = Column(String(2), nullable=True)
    report_num = Column(String(12), nullable=False)
    report_date = Column(Date, nullable=True)
    report_time = Column(Integer, nullable=False)
    report_sequence_num = Column(Integer, nullable=False)
    dot_num = Column(Integer, nullable=True)
    status_code = Column(String(1), nullable=True)
    final_status_date = Column(Date, nullable=True)
    location = Column(String(250), nullable=True)
    city_code = Column(String(5), nullable=True)
    city = Column(String(25), nullable=True)
    state = Column(String(2), nullable=True)
    county_code = Column(Integer, nullable=True)
    truck_bus_ind = Column(String(1), nullable=True)
    trafficway_id = Column(String(8), nullable=True)
    road_access = Column(String(8), nullable=True)
    road_surface = Column(String(8), nullable=True)
    cargo_body_type = Column(String(8), nullable=True)
    gross_vehicle_weight_range = Column(String(6), nullable=True)
    gross_vehicle_weight_rating = Column(String(8), nullable=True)
    vin = Column(String(17), nullable=True)
    license_num = Column(String(9), nullable=True)
    license_state = Column(String(2), nullable=True)
    hazmat = Column(String(1), nullable=True)
    weather_cond = Column(String(8), nullable=True)
    vehicle_config = Column(String(8), nullable=True)
    light_cond = Column(String(8), nullable=True)
    hazmat_release = Column(String(1), nullable=True)
    reporting_agency = Column(String(35), nullable=True)
    officer_badge_num = Column(String(5), nullable=True)
    vehicles_involved = Column(Integer, nullable=True)
    fatalities = Column(Integer, nullable=True)
    injuries = Column(Integer, nullable=True)
    tow_away = Column(String(1), nullable=True)
    federally_recordable = Column(String(1), nullable=True)
    state_recordable = Column(String(1), nullable=True)
    safetynet_software_version = Column(String(10), nullable=True)
    safetynet_sequence_id = Column(String(10), nullable=True)
    transaction_code = Column(String(1), nullable=True)
    transaction_date = Column(Date, nullable=True)
    upload_byte = Column(String(1), nullable=True)
    upload_dot_num = Column(String(8), nullable=True)
    upload_search_indicator = Column(String(1), nullable=True)
    upload_date = Column(Date, nullable=True)
    related_factors = Column(String(10), nullable=True)
    census_search_date = Column(Date, nullable=True)
    add_date = Column(Date, nullable=True)
    change_date = Column(Date, nullable=True)
    changed_by_user = Column(String(30), nullable=True)
    changed_by_application = Column(String(61), nullable=True)
    safetynet_input_date = Column(Date, nullable=True)


class Carrier(Base):

    __tablename__ = 'carrier'
    id = Column(Integer, primary_key=True)
    dot_num = Column(Integer, nullable=False)
    carrier_name = Column(String(120), nullable=True)
    carrier_street = Column(String(50), nullable=True)
    carrier_city = Column(String(25), nullable=True)
    carrier_city_code = Column(String(5), nullable=True)
    carrier_state = Column(String(2), nullable=True)
    carrier_zip = Column(String(10), nullable=True)
    colonia = Column(String(25), nullable=True)
    prefix = Column(String(2), nullable=True)


class Vehicle(Base):
    __tablename__ = 'Vehicle'
    id = Column (Integer, primary_key=True)
    vin = Column(String(17), nullable=False)
    make = Column(String(255), nullable=True)
    model = Column(String(255), nullable=True)
    year = Column(Integer, nullable=True)
    plant_city = Column(String(255), nullable=True)
    plant_state = Column(String(255), nullable=True)
    plant_country = Column(String(255), nullable=True)
    engine = Column(String(255), nullable=True)
    body_class = Column(String(255), nullable=True)
    brake_system = Column(String(255), nullable=True)
    drive_type = Column(String(255), nullable=True)
    notes = Column(String(255), nullable=True)
    manufacturer = Column(String(255), nullable=True)


def create():

    # Create an engine that stores data in the local directory's
    # sqlalchemy_example.db file.
    engine = create_engine ('mysql+pymysql://alex:tygrcnt@127.0.0.1/adas')

    # Create all tables in the engine. This is equivalent to "Create Table"
    # statements in raw SQL.
    Base.metadata.create_all(engine)

if __name__ == "__main__":
    create()