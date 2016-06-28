from flask import Flask,request,jsonify
import os
app = Flask(__name__)

@app.route('/index/',methods=['GET','POST'])
def helloworld():
	print dir(request)
	print type(request.form)
	print type(request.get_json())
	json_data=request.get_json()
	for i in json_data:
		print i.get('path'),'===',i.get('value'),"===",i.get('timestamp')
	print type(request.get_data())
	return jsonify({"jian":"zhi","a":'k'})
if __name__ == '__main__':
	app.run(host='0.0.0.0',debug=True)
