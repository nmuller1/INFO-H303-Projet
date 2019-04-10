from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def student():
   return render_template('start.html')

@app.route('/connection',methods = ['POST', 'GET'])
def connection():
   if request.method == 'POST':
      return render_template('connection.html')

@app.route('/signIn',methods = ['POST', 'GET'])
def signIn():
   if request.method == 'POST':
      return render_template('signIn.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      return render_template("result.html",result = result)
