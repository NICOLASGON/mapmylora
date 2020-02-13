from flask import Flask, render_template
import simplejson as json
from gateways import fetch_gateways

app = Flask(__name__)

@app.route('/')
def map():
    gw = json.dumps(fetch_gateways(), iterable_as_array=True)
    return render_template('base.html', gw=gw)

if __name__ == '__main__':
    app.run(debug=True)
