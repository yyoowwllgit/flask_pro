#!/root/test/0618/myflaskproject/bin/python
#encoding=utf-8
from datetime import timedelta
from flask import Flask,Blueprint,session,render_template,request
from flask_login import LoginManager,login_required,login_user,logout_user,UserMixin,current_user
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:////root/test/0618/flask_pro/mydb.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True
db= SQLAlchemy(app)

class User(db.Model,UserMixin):
	id=db.Column(db.Integer,primary_key=True)
	username=db.Column(db.String(80),unique=True)
	password=db.Column(db.String(128))
	def __init__(self,name,passwd):
		self.username=name
		self.password=passwd
	def is_authenticated(self):
		return True
	def is_active(self):
		return True
	def is_anonymous(self):
		return False
	def get_id(self):
		return unicode(self.id)
	def __repr__(self):
		return '<User>:{0}'.format(self.username)

class data(db.Model,UserMixin):
	id=db.Column(db.Integer,primary_key=True)
	itemname=db.Column(db.String(80),unique=True)
	itemvalue=db.Column(db.String(80))
	itemtimestamp=db.Column(db.String(80))
	def __init__(self,name,passwd):
		self.username=name
		self.password=passwd
	def is_authenticated(self):
		return True
	def is_active(self):
		return True
	def is_anonymous(self):
		return False
	def get_id(self):
		return unicode(self.id)
	def __repr__(self):
		return '<User>:{0}'.format(self.username)

#new code
app.secret_key='\xe1\x1a\xc7tP'
login_manager=LoginManager()
login_manager.session_protection='strong'
login_manager.login_view='auth.logi'
login_manager.login_message=u'请登录'
login_manager.login_message_category='info'
login_manager.remember_cookie_duration=timedelta(minutes=1)
login_manager.init_app(app)

#@login_manager.unauthorized_handler
#def unauth():
#	return u'请登录'

@login_manager.user_loader
def load_use(uid):
	user = User.query.filter_by(id=int(uid)).first()
	return user
#end new code

auth = Blueprint('auth',__name__)
@auth.route('/login/',methods=['GET','POST'])
def logi():
	if request.method=='POST':
		user = User.query.filter_by(username=request.form['uname'],password=request.form['passwd']).first()
		if user is not None:
			print session
			login_user(user)
			session.permanent=True
			app.permanent_session_lifetime=timedelta(minutes=1)
			print session
			return '{0} login page'.format(current_user.username)
		return render_template('login.html')
	else:
		return render_template('login.html')

@auth.route('/logout/',methods=['GET','POST'])
@login_required
def logo():
	logout_user()
	return 'logout page'

@app.route('/')
@app.route('/test/')
@login_required
def test():
	return 'yes,you are allowed,{0}'.format(current_user.username)

app.register_blueprint(auth,url_prefix='/authx')

if __name__=='__main__':
	app.run(host='0.0.0.0',debug=True)
