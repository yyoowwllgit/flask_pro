from flask import Flask
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash,check_password_hash

app = Flask(__name__)
auth = HTTPBasicAuth()

users={
'huang':generate_password_hash('peng'),
'li':generate_password_hash('biu')
}

@auth.verify_password
def verify_passwd(uname,pword):
	if uname in users:
		return check_password_hash(users.get(uname),pword)
	return False

@app.route('/')
@auth.login_required
def index():
	print dir(auth)
	return "Hello {0},good night".format(auth.username())

if __name__=='__main__':
	app.run(host='0.0.0.0',debug=True)
