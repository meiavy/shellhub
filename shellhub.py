#!./bin/python
from bottle import route, run, template
import os

@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)

@route('/put/<cmd>')
def put(cmd):
    output = os.popen(cmd)
    result=output.read()
    output.close()
    lines=result.split('\n')

    return template('template', result=lines)


run(host='localhost', port=8080)
