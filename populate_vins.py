from create_db import Accident
from sql_alchemy_engine import session
from vin_lookup import add_vin

for vin, in session.query(Accident.vin).distinct():
    if vin is not None:
        if (len(vin) == 17) and (' ' not in vin):
            try:
                add_vin(vin)
            except ValueError:
                pass
