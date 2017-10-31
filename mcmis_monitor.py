from sql_alchemy_engine import session
from create_db import Accident
from ftp_retrieval import AccidentArchiveFTP
from os.path import expanduser



def add_new_accident_file(data):
    for ix, row in data.iterrows():
        # Insert a Person in the person table
        new_accident = Accident(
            report_number=row.REPORT_NUMBER,
            report_seq_num=row.REPORT_SEQ_NO,
            dot_number=row.DOT_NUMBER,
            accident_date=row.REPORT_DATE,
            state=row.REPORT_STATE,
            fatalities=row.FATALITIES,
            injuries=row.INJURIES,
            tow_away=row.TOW_AWAY,
            hazmat=row.HAZMAT_RELEASED,
            trafficway_description=row.TRAFFICWAY_DESC,
            access_control=row.ACCESS_CONTROL_DESC,
            road_surface_cond=row.ROAD_SURFACE_CONDITION_DESC,
            weather=row.WEATHER_CONDITION_DESC,
            light_cond=row.LIGHT_CONDITION_DESC,
            vin=row.VEHICLE_ID_NUMBER,
            license_num=row.VEHICLE_LICENSE_NUMBER,
            license_state=row.VEHICLE_LICENSE_STATE,
            severity_weight=row.SEVERITY_WEIGHT,
            time_weight=row.TIME_WEIGHT,
            citation_issued=row.CITATION_ISSUED_DESC,
            sequence_num=row.SEQ_NUM,
        )
        session.add(new_accident)
        session.commit()

def main():
    with open(expanduser('~')+'/mcmis_last.txt', 'rb') as last:
        last_read = last.readline()[:-1]

    archive = AccidentArchiveFTP()

    if archive.latest_upload.file.values[0] == last_read:
        print 'up to date'
        return
    else:
        data = archive.get_file(archive.latest_upload.file.values[0])
        add_new_accident_file(data)
        with open(expanduser('~')+'/mcmis_last.txt', 'w') as last:
            last.write(archive.latest_upload.file.values[0])
        print 'new data!'

if __name__ == '__main__':
    main()
