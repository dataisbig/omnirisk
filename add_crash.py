from sql_alchemy_engine import session
from create_db import Accident
import pandas as pd


columns = pd.read_csv('/home/lxpollara/mcmis crash_data/crash_event_cols.csv')
file_loc = "/home/lxpollara/mcmis crash_data/CrashEvent_01012017_11082017.txt"
data = pd.read_csv(file_loc, sep='\t', header=None)
data.columns = columns.Field.values
length = str(len(data))
data.fillna('None', inplace=True)
for ix, row in data.iterrows():
    session.add(Accident(
    crash_event_id = row['CRASH_EVENT_ID '],
    crash_id = row['CRASH_ID '],
    sequence_num = row['SEQ_NO '],
    event_id = row['EVENT_ID '],
    event_other_desc = row['EVENT_OTHER_DESC '],
    ))
    if ix%1000 == 0:
        session.commit()
        print str (ix + 1) + ' out of ' + length
print str(ix+1) + ' out of ' + length
session.commit()


