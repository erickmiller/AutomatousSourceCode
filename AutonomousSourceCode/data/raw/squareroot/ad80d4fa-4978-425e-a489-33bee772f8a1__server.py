from bottle import request, route, run, static_file, post
import subprocess
import json

# OBS: For java interface:
# Another option would be,
#   A) embedding this server on java
#      Look at jepp JAVA library.
#
#   B) embedding java in this script.
#     Look at JPype PYTHON library
#     In my opinion, JPype  would be best/easier option
#
# Both would do it.
# Look this link for solutions:
#
# http://pt.slideshare.net/onyame/communication-between-java-and-python

ncalls = 0

@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='./static')


@route('/')
def index():
    return static_file('index.html', root='./static')


@post('/api/square')
def api_square():
    global ncalls
    ncalls += 1
    n = request.json['data']
    return {'number': n*n, 'comments' : 'Using python. Called {} times'.format(ncalls)}


@post('/api/squareshell')
def api_square_shell():
    outstr = subprocess.check_output(['bash', './compute_square.sh', '5'])
    return json.loads(outstr)


run(host='localhost', port=8080, debug=True)
