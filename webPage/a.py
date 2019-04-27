from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def student():
   return render_template('start.html')

@app.route('/signIn',methods = ['POST', 'GET'])
def signIn():
   if request.method == 'POST':
      return render_template('signIn.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      return render_template("result.html",result = result)

if __name__ == '__main__':
    app.run(host='0.0.0.0')