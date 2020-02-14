from flask import Flask, render_template
import simplejson as json
import os

from gateways import fetch_gateways
from trackers import fetch_trackers

app = Flask(__name__)
app.config.from_object('settings')

@app.route('/')
def map():
    gateways = json.dumps(fetch_gateways(), iterable_as_array=True)
    trackers = json.dumps(fetch_trackers(), iterable_as_array=True)
    return render_template('base.html', gateways=gateways, trackers=trackers)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
