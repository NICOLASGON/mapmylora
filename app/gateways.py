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
    gateways = result.get_points()

    filter_dict = {}
    result_list = []

    for gateway in gateways:
        if gateway['name'] not in filter_dict:
            filter_dict[gateway['name']] = gateway
            result_list.append(gateway)

    return result_list
