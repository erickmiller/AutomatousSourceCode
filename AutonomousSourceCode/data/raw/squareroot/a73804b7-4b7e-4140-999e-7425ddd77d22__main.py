from flask import Flask, request, url_for, jsonify, redirect
from functools import wraps

app = Flask(__name__)

####################

def check_auth(username, password):
    return username == 'admin' and password == 'secret'

def authenticate():
    message = {'message': "Authenticate."}
    resp = jsonify(message)

    resp.status_code = 401
    resp.headers['WWW-Authenticate'] = 'Basic realm="Example"'

    return resp

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth: 
            return authenticate()

        elif not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)

    return decorated
####################

@app.route('/')
@requires_auth
def api_root():
	#return 'Welcome to WSGI python based server'
	data={'Hello':'world','I am':'testing'}
	resp = jsonify(data)
	resp.status_code = 200
	return resp

@app.route('/square/<num>/')
def api_square(num):
	return ' Square of ' + num + ' is: ' + str(int(num)*int(num))

@app.route('/secrets/')
@requires_auth
def api_hello():
    return redirect("http://www.google.com", code=302)



if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')
