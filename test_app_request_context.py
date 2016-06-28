from flask import Flask,request,jsonify,g
import os
app = Flask(__name__)
g.position='app_position'
@app.route('/index/',methods=['GET','POST'])
def helloworld():
	return g.position
@app.route('/set/<value>/',methods=['GET','POST'])
def setg(value):
	g.position=value
	return g.position
if __name__ == '__main__':
	app.run(host='0.0.0.0',debug=True)
