import os

DEBUG = True

INFLUXDB_HOSTNAME = os.environ.get("INFLUXDB_HOSTNAME", default="influxdb.lora.tetaneutral.net")
INFLUXDB_PORT = int(os.environ.get("INFLUXDB_PORT", default="443"))
INFLUXDB_USERNAME = os.environ.get("INFLUXDB_USERNAME", default="student")
INFLUXDB_PASSWORD = os.environ.get("INFLUXDB_PASSWORD", default="student")