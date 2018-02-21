import sys
sys.path.append('/home/lxpollara/pyvpic')
sys.path.append('/home/lxpollara/Adas_Proj')
from sql_alchemy_engine import session, Base
from create_db import AccidentMaster, Vehicle
from vpicwrapper import pyvpic

# list unique vins currently in db
vins = [v[0] for v in session.query(AccidentMaster.vin).distinct() if v[0] is not None]
vins_clean = [v for v in vins if len(v)==17]

vins_clean = set(vins_clean)-set([v[0] for v in session.query(Vehicle.vin).distinct() if v[0] is not None])
n=0
for v in vins_clean:
    try:
        vin_data = pyvpic.Vehicle(v)
        vin_data.decode()
    except ValueError:
        pass
    
    if vin_data.message == 'Results returned successfully':
        # new vehicle object
        new_vehicle = Vehicle(
            vin = v,
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
            notes = ' ',
            manufacturer= vin_data.listing['Manufacturer Id'])
        session.add(new_vehicle)
        n+=1

session.commit()

