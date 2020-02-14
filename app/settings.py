import os

DEBUG = True

INFLUXDB_HOSTNAME = os.environ.get("INFLUXDB_HOSTNAME", default="localhost")
INFLUXDB_PORT = int(os.environ.get("INFLUXDB_PORT", default="8086"))
INFLUXDB_USERNAME = os.environ.get("INFLUXDB_USERNAME", default="")
INFLUXDB_PASSWORD = os.environ.get("INFLUXDB_PASSWORD", default="")