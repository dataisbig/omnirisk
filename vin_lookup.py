from sql_alchemy_engine import session
from create_db import Vehicle
from vpicwrapper import pyvpic


def add_vin(vin):
    # check if we already have the vin
    exists = session.query(Vehicle.vin).filter_by(vin=vin).scalar() is not None
    if exists:
        return

    else:
        # if not retrieve the vin from the vpic
        vin_data = pyvpic.Vehicle(vin)
        vin_data.decode()
        if vin_data.message == 'Results returned successfully':
            # new vehicle object
            new_vehicle = Vehicle(
            vin = vin,
            make = vin_data.listing['Make'],
            model = vin_data.listing['Model'],
            year = vin_data.listing['Model Year'],
            plant_city = vin_data.listing['Plant City'],
            plant_state = vin_data.listing['Plant State'],
            plant_country = vin_data.listing['Plant Country'],
            engine = vin_data.listing['Engine Manufacturer'],
            body_class = vin_data.listing['Body Class'],
            brake_system = vin_data.listing['Brake System Type'],
            drive_type = vin_data.listing['Drive Type'],
            notes = ' '
            )
        session.add(new_vehicle)
        session.commit()


def test():
    add_vin('1M1AA09Y43W026760')
