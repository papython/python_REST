#!/bin/python
################################################################
# Simple example code to run a rest-api interface that returns #
# the result of ls -l /tmp back to the requestor.              #
################################################################
import commands
from flask import Flask 
from flask import jsonify
from flask import request
from flask import render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap


app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
bootstrap = Bootstrap(app)

class NameForm(FlaskForm):   
 name = StringField('What is your name?', validators=[DataRequired()])
 submit = SubmitField('Submit')

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

@app.route('/h/<name>')
def default(name=None):
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
    return render_template('index.html', form=form, name=name)

@app.route('/headers')
def headers():
    c = []
    c.append(request.headers)
    c.append(request.endpoint)
    c.append(request.path)
    c.append(request.method)
    c.append(request.host)
    return '<h1>{}</h1>'.format(c)

@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html',name=name)

if __name__ == '__main__':
    ls_request = 0
    ps_request = 0
    app.run(host='0.0.0.0',port=8081,debug=False)
