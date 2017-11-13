from create_db import Accident
from sql_alchemy_engine import session
from vin_lookup import add_vin

for vin, in session.query(Accident.vin).distinct():
    if (len(vin)==17) and (' ' not in vin):
        add_vin(vin)

