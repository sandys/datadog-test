""" hello.py """

import logging
import socket

from flask import Flask, jsonify
import blinker as _

from ddtrace import tracer
from ddtrace.contrib.flask import TraceMiddleware

from ddtrace import patch_all
patch_all()

log = logging.getLogger(__name__)
app = Flask(__name__)
tracer.configure(hostname='datadog')
traced_app = TraceMiddleware(app, tracer, service="my-flask-app", distributed_tracing=False)

@app.route('/')
def hello():
    return jsonify({
        'hello': 'world',
        'host': socket.gethostname()
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0')
