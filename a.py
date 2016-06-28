from flask import Flask
import os
import sqlite3
app = Flask(__name__)

@app.route('/')
def helloworld():
	print os.path.realpath(__file__)
	condb = sqlite3.connect('mydb.db')
	res=condb.execute("select * from entries")
	a=res.fetchall()	
	condb.close()
	print a
	rep_str=''
	for i in a:
		rep_str=''.join([rep_str,str(i)])
	return rep_str
if __name__ == '__main__':
	app.run(host='0.0.0.0',debug=True)
