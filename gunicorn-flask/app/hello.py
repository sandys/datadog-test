""" hello.py """

import logging
import socket

from flask import Flask, jsonify
import blinker as _


from scout_apm.flask import ScoutApm
log = logging.getLogger(__name__)
app = Flask(__name__)

#from scout_apm.flask.sqlalchemy import instrument_sqlalchemy

# Setup a flask 'app' as normal

## Attaches ScoutApm to the Flask App
ScoutApm(app)

## Instrument the SQLAlchemy handle
#instrument_sqlalchemy(db)

# Scout settings
app.config['SCOUT_MONITOR'] = True
app.config['SCOUT_KEY']     = "UOoV3CDkZy3fYZYJW4Qs"
app.config['SCOUT_NAME']    = "A FRIENDLY NAME FOR YOUR APP"

@app.route('/')
def hello():
    return jsonify({
        'hello': 'world',
        'host': socket.gethostname()
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0')
