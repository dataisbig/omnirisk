from sql_alchemy_engine import session
from create_db import AccidentCarrier
import pandas as pd


columns = pd.read_csv('/home/lxpollara/mcmis crash_data/crash_carrier_cols.csv')
file_loc = "/home/lxpollara/mcmis crash_data/CrashCarrier_01012017_11082017.txt"
data = pd.read_csv(file_loc, sep='\t', header=None)
data.columns = columns.Field.values
length = str(len(data))
data.fillna('N', inplace=True)
for ix, row in data.iterrows():

    session.add(AccidentCarrier(
    crash_carrier_id = row['CRASH_CARRIER_ID '],
    crash_id = row['CRASH_ID '],
    carrier_name_source = row['CARRIER_SOURCE_CODE '],
    carrier_name = row['CRASH_CARRIER_NAME '],
    carrier_street = row['CRASH_CARRIER_STREET '],
    carrier_city = row['CRASH_CARRIER_CITY '],
    carrier_city_code = row['CRASH_CARRIER_CITY_CODE '],
    carrier_state = row['CRASH_CARRIER_STATE '],
    carrier_zip = row['CRASH_CARRIER_ZIP_CODE '],
    colonia = row['CRASH_COLONIA '],
    prefix = row['PREFIX '],
    docket_num = row['DOCKET_NUMBER '],
    interstate = row['CRASH_CARRIER_INTERSTATE '],
    no_id_flag = row['NO_ID_FLAG '],
    state_num = row['STATE_NUMBER '],
    state_issuing_num = row['STATE_ISSUING_NUMBER ']
    ))
    if ix%1000 == 0:
        session.commit()
        print str (ix + 1) + ' out of ' + length
print str(ix+1) + ' out of ' + length
session.commit()


