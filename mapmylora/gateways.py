from influxdb import InfluxDBClient

INFLUXDB_HOSTNAME = ''
INFLUXDB_PORT = 443
INFLUXDB_USERNAME = '
INFLUXDB_PASSWORD = ''
INFLUXDB_DB = ''

def fetch_gateways():
    client = InfluxDBClient(INFLUXDB_HOSTNAME, INFLUXDB_PORT, INFLUXDB_USERNAME, INFLUXDB_PASSWORD, INFLUXDB_DB, True, True)
    result = client.query('select * from gateways where lat !=0 and lon !=0 order by time LIMIT 100000000')
    gw = result.get_points()
    return gw