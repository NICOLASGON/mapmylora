from flask import current_app as app
from influxdb import InfluxDBClient

def fetch_gateways():
    client = InfluxDBClient(app.config['INFLUXDB_HOSTNAME'], 
                            app.config['INFLUXDB_PORT'],
                            app.config['INFLUXDB_USERNAME'], 
                            app.config['INFLUXDB_PASSWORD'], 
                            "gateways", 
                            True, True)
    result = client.query('select * from gateways where lat !=0 and lon !=0 order by time LIMIT 100000000')
    gw = result.get_points()

    return gw