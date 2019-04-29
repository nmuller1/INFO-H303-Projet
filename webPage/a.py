from flask import Flask, render_template, request
import sys
import psycopg2
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
      cur.execute("SELECT * FROM user WHERE cardNum=%s",(result['CreditCardNum'],))
      res = cur.fetchone()
      if res == None:      #if credit doesn't exist already
         cur.execute("SELECT max(id) from user_");
         max_ID =  int(cur.fetchone()[0])
         new_ID = str(max_ID+1)
         newUsername = result['newUsername']
         newPassword = result['newPassword']
         CreditCardNum = result['CreditCardNum']
         cur.execute("INSERT INTO user (id, pseudo,password, cardNum<) VALUES (%s, %s,%s,%s)",(new_ID, newUsername,newPassword, CreditCardNum))
         conn.commit()
         if vendeur:
            firstName=result['firstName']
            name=result['name']
            phone=result['phone']
            road=result['road']
            roadNum=result['roadNum']
            codePostal=result['codePostal']
            commune=result['commune']
            cur.execute("INSERT INTO CHARGER_USER (id,firstname,name,phone,road,roadNum,codePostal,commune) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",(new_ID,firstname,name,phone,road,roadNum,codePostal,commune))
            conn.commit()
      return render_template("result.html",result = result)

if __name__ == '__main__':
   try:
      dbname=sys.argv[1]
      user=sys.argv[2]
   except:
      print("Arg error")
      exit()
   conn = psycopg2.connect("dbname="+dbname+" user="+user)
   cur = conn.cursor()
   app.run()   #host='0.0.0.0')
   cur.close()
   conn.close()