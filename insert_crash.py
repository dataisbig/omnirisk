from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from create_db import Base, Vehicle, Accident
from ftp_retrieval import AccidentArchiveFTP

archive = AccidentArchiveFTP()

engine = create_engine('mysql+pymysql://alex:tygrcnt@127.0.0.1/adas')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()
for document in archive.files.file.values:
    data = archive.get_file(document)
    print document
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
            trafficway_description=row.TRAFFIC_DESC,
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