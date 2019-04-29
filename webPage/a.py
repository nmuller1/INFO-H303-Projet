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
   try:
      dbname=sys.argv[1]
      user=sys.argv[2]
   conn = psycopg2.connect("dbname="+dbname+" user="+user)
   cur = conn.cursor()
   app.run()   #host='0.0.0.0')
   cur.close()
   conn.close()