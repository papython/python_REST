#!/bin/python
################################################################
# Simple example code to run a rest-api interface that returns #
# the result of ls -l /tmp back to the requestor.              #
################################################################
import commands
from flask import Flask 
from flask import jsonify

app = Flask(__name__)

@app.route('/ls')
def ls():
    global ls_request
    ls_request = ls_request + 1
    print "number of /ls requests = " + str(ls_request)
    return jsonify(commands.getoutput("ls -l /tmp"))

@app.route('/ps')
def ps():
    global ls_request
    ps_request = ps_request + 1
    print "number of /ps requests = " + str(ps_request)
    return jsonify(commands.getoutput("ps -ef"))

if __name__ == '__main__':
    ls_request = 0
    ps_request = 0
    app.run(host='0.0.0.0',port=81,debug=False)
