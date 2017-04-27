import newrelic.agent
newrelic.agent.initialize('newrelic.ini')

import sys
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Index'

@app.route('/error')
def value_error():
    raise ValueError()

@app.route('/crash')
def crash():
    sys.exit(100)

def exception_handler(e, event, context):
    application = newrelic.agent.application()
    application.activate()
    newrelic.agent.record_exception(*sys.exc_info(), application=application)

if __name__=='__main__':
    app.run()
