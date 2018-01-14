from sql_alchemy_engine import session
from create_db import AccidentMaster
import pandas as pd


columns = pd.read_csv('/home/lxpollara/mcmis crash_data/crash_master_cols.csv')
file_loc = "/home/lxpollara/mcmis crash_data/CrashMaster_01012015_12312015.txt"
data = pd.read_csv(file_loc, sep='\t', header=None)
data.columns = columns.Field.values
length = str(len(data))
data = data.where((pd.notnull(data)), None)
for ix, row in data.iterrows():
    try:
        session.add(AccidentMaster(
                   crash_id = row['CRASH_ID '],
                   report_state = row['REPORT_STATE '],
                   report_num = row['REPORT_NUMBER '],
                   report_date = row['REPORT_DATE '],
                   report_time = row['REPORT_TIME '],
                   report_sequence_num = row['REPORT_SEQ_NO '],
                   dot_num = row['DOT_NUMBER '],
                   status_code = row['CI_STATUS_CD '],
                   final_status_date = row['FINAL_STATUS_DATE '],
                   location = row['LOCATION '],
                   city_code = row['CITY_CODE '],
                   city = row['CITY '],
                   state = row['STATE '],
                   county_code = row['COUNTY_CODE '],
                   truck_bus_ind = row['TRUCK_BUS_IND '],
                   trafficway_id = row['TRAFFICWAY_ID '],
                   road_access = row['ACCESS_CONTROL_ID '],
                   road_surface = row['ROAD_SURFACE_CONDITION_ID '],
                   cargo_body_type = row['CARGO_BODY_TYPE_ID '],
                   gross_vehicle_weight_range = row['GVW_RATING_ID '],
                   vin = row['VEHICLE_IDENTIFICATION_NUMBER '],
                   license_num = row['VEHICLE_LICENSE_NUMBER '],
                   license_state = row['VEHICLE_LIC_STATE '],
                   hazmat = row['VEHICLE_HAZMAT_PLACARD '],
                   weather_cond = row['WEATHER_CONDITION_ID '],
                   vehicle_config = row['VEHICLE_CONFIGURATION_ID '],
                   light_cond = row['LIGHT_CONDITION_ID '],
                   hazmat_release = row['HAZMAT_RELEASED '],
                   reporting_agency = row['AGENCY '],
                   officer_badge_num = row['OFFICER_BADGE '],
                   vehicles_involved = row['VEHICLES_IN_ACCIDENT '],
                   fatalities = row['FATALITIES '],
                   injuries = row['INJURIES '],
                   tow_away = row['TOW_AWAY '],
                   federally_recordable = row['FEDERAL_RECORDABLE '],
                   state_recordable = row['STATE_RECORDABLE '],
                   safetynet_software_version = row['SNET_VERSION_NUMBER '],
                   safetynet_sequence_id = row['SNET_SEQUENCE_ID '],
                   transaction_code = row['TRANSACTION_CODE '],
                   transaction_date = row['TRANSACTION_DATE '],
                   upload_byte = row['UPLOAD_FIRST_BYTE '],
                   upload_dot_num = row['UPLOAD_DOT_NUMBER '],
                   upload_search_indicator = row['UPLOAD_SEARCH_INDICATOR '],
                   upload_date = row['UPLOAD_DATE '],
                   census_search_date = row['CENSUS_SEARCH_DATE '],
                   add_date = row['ADD_DATE '],
                   change_date = row['CHANGE_DATE '],
                   changed_by_user = row['CHANGE_BY_USER '],
                   changed_by_application = row['CHANGE_BY_APPL '],
                   safetynet_input_date = row['SNET_INPUT_DATE '],
        ))
    except:
        print row
    if ix%1000 == 0:
        session.commit()
        print str (ix + 1) + ' out of ' + length
print str(ix+1) + ' out of ' + length
session.commit()


