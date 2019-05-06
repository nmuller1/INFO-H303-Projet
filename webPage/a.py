from flask import Flask, render_template, request, flash, redirect, session
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
      cur.execute("SELECT * FROM user_ WHERE cardNum=%s",(result['CreditCardNum'],))
      res = cur.fetchone()
      if res == None:      #if credit doesn't exist already
         cur.execute("SELECT max(id) from user_ LIMIT 1");
         try:
            max_ID =  int(cur.fetchone()[0])
         except:
            max_ID = 0
         new_ID = str(max_ID+1)
         newUsername = result['newUsername']
         newPassword = result['newPassword']
         CreditCardNum = result['CreditCardNum']
         cur.execute("INSERT INTO user_ (id, pseudo,password, cardNum) VALUES (%s, %s,%s,%s)",(new_ID, newUsername,newPassword, CreditCardNum))
         conn.commit()
         if result['firstName'] != "":
            firstName=result['firstName']
            name=result['name']
            phone=result['phone']
            road=result['road']
            roadNum=result['roadNum']
            codePostal=result['codePostal']
            commune=result['commune']
            cur.execute("INSERT INTO charger_user (id,firstname,lastname,phoneNum,road,roadNum,codePostal,commune) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",(new_ID,firstName,name,phone,road,roadNum,codePostal,commune))
            conn.commit()
      return render_template("result.html",result = result)

@app.route('/connected',methods = ['POST', 'GET'])
def connected():
      result = request.form
      cardNum = result['Username']
      Password = result['Password']
      cur.execute("SELECT u.password, u.id FROM user_ u WHERE u.cardNum = %s",(cardNum,))
      fetch = cur.fetchone()
      if fetch==None or Password != fetch[0]:
         flash("This user doesn't exist")
         return redirect('/')
      session['cardNum'] = cardNum
      session['Password'] = Password
      session['userID'] = fetch[1]
      return render_template("connected.html",result = result)

@app.route('/consultScooters',methods = ['POST', 'GET'])
def consultScooters():
   users = ['maateen', 'nabin', 'shadd']
   return render_template('consultScooters.html', users=users)


@app.route('/consultTrips',methods = ['POST', 'GET'])
def consultTrips():
   users = ['maateen', 'nabin', 'shadd']
   cur.execute("SELECT * FROM trips WHERE userID=%s",(session['userID'],))
   trips = cur.fetchone()
   return render_template('consultScooters.html', trips=trips)


if __name__ == '__main__':
   try:
      dbname=sys.argv[1]
      user=sys.argv[2]
   except:
      print("Arg error")
      exit()
   conn = psycopg2.connect("dbname="+dbname+" user="+user)
   cur = conn.cursor()
   app.secret_key = 'super secret key'
   app.run()   #host='0.0.0.0')
   cur.close()
   conn.close()