import MySQLdb



class AccidentDB:
    def __init__(self):
        self.db = MySQLdb.connect(host='127.0.0.1',user='alex',passwd='tygrcnt',db='adas')
        self.cursor= self.db.cursor()
        self.sql_add = (
        "INSERT INTO accidents (report_number, report_seq_num, dot_number, accident_date, state, fatalities, "
        "injuries, tow_away, hazmat, trafficway_description, access_control, road_surface_cond, weather, light_cond,"
        " vin, license_num, license_state, severity_weight, time_weight, citation_issued, sequence_num)"
        " VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}',"
        " '{}', '{}', '{}', '{}');")

    def add_accident(self, data):
        self.cursor.execute(self.sql_add.format(*data))
