from flask import current_app as app
from influxdb import InfluxDBClient
import settings as settings

def fetch_trackers():
    client = InfluxDBClient(app.config['INFLUXDB_HOSTNAME'], 
                            app.config['INFLUXDB_PORT'],
                            app.config['INFLUXDB_USERNAME'],
                            app.config['INFLUXDB_PASSWORD'],
                            "trackers", 
                            True, True)
    result = client.query('select * from trackers  where latitude > 5 and latitude < 65 and longitude > 0 and longitude < 25 LIMIT 100000000000')
    trackers = result.get_points()
    return trackers
