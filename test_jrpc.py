from flask import Flask
from flask_jsonrpc import JSONRPC
app=Flask(__name__)
jsonrpc=JSONRPC(app,'/api',enable_web_browsable_api=True)
#jsonrpc=JSONRPC(app,'/api')
@jsonrpc.method('App.index')
def index():
	return 'welecome to flask jsonrpc!'
@jsonrpc.method('App.argtest(Number,Number)->Number',validate=True)
def test(a1,a2):
	return "lala {0}--{1}".format(a1,a2) 
if __name__=='__main__':
	app.run(host='0.0.0.0',debug=True)
