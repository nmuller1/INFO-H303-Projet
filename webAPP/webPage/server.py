from requetesSQL import *
from flask import Flask, render_template, request, flash, redirect, session, url_for
import sys
import psycopg2
import datetime
app = Flask(__name__)

@app.route('/')
def accueil():
   session.clear()
   return render_template('start.html')

@app.route('/signIn',methods = ['POST', 'GET'])
def signIn():
   if request.method == 'POST':
      return render_template('signIn.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
   """Function to register users account.
   """
   if request.method == 'POST':
      if len(request.form)>=2:
         result = request.form
         cur.execute("SELECT * FROM nUser WHERE cardNum=%s",(result['CreditCardNum'],))
         res = cur.fetchone()
         if res == None:      #if credit card doesn't exist already
            cur.execute("SELECT max(id) from nUser LIMIT 1")
            try:
               max_ID =  int(cur.fetchone()[0])
            except:
               max_ID = 0
            new_ID = str(max_ID+1)
            newPassword = result['newPassword']
            CreditCardNum = result['CreditCardNum']
            cur.execute("INSERT INTO nUser (id,password, cardNum) VALUES (%s,%s,%s)",(new_ID,newPassword, CreditCardNum))
            conn.commit()
            if len(request.form)>2:
               if len(request.form)==9:
                  firstName=result['firstName']
                  name=result['name']
                  phone=result['phone']
                  road=result['road']
                  roadNum=result['roadNum']
                  codePostal=result['codePostal']
                  commune=result['commune']
                  cur.execute("INSERT INTO charger_user (id,firstname,lastname,phoneNum,road,roadNum,codePostal,commune) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",(new_ID,firstName,name,phone,road,roadNum,codePostal,commune))
                  conn.commit()
               else :
                  return render_template("loginFailed.html",result = "Please complete all the input fields")
            return render_template("loginFailed.html",result = "Congratulations ! Your has been created.")
         return render_template("loginFailed.html",result = "CardNum already exits !")
      return render_template("loginFailed.html",result = "Please complete all the input fields")

@app.route('/connected',methods = ['POST', 'GET'])
def connected():
   """Function to start session.
   """
   hasCharger = "False"
   result = request.form
   cardNum = result['Username']
   Password = result['Password']
   cur.execute("SELECT u.password, u.id FROM nUser u WHERE u.cardNum = %s",(cardNum,))
   fetch = cur.fetchone()
   if fetch==None:
      cur.execute("SELECT m.password, m.id, m.firstname, m.lastname FROM mechanic m WHERE m.cardNum = %s",(cardNum,))
      fetch = cur.fetchone()
      if fetch==None:
         return render_template("loginFailed.html",result = "User doesn't exist, try again !")
      if Password != fetch[0]:
         return render_template("loginFailed.html",result = "Wrong password, try again !")
      session['userID'] = str(fetch[1])
      session['firstname'] = fetch[2]
      session['lastname'] = fetch[3]
      return render_template("mechanic.html")
      
   if Password != fetch[0]:
      return render_template("loginFailed.html",result = "Wrong password, try again !")
   session['cardNum'] = cardNum
   session['Password'] = Password
   session['userID'] = fetch[1]
   cur.execute("SELECT u.lastname FROM CHARGER_USER u WHERE u.id = %s",(session['userID'],))
   fetch = cur.fetchone()
   if fetch!=None:
      hasCharger = "True"
   return render_template("connected.html", hasCharger = hasCharger)

#==============================USER PAGES=======================================================================
@app.route('/consultScooters',methods = ['POST', 'GET'])
def consultScooters():
   cur.execute(R1)
   trips = cur.fetchall()
   return render_template('consultScooters.html', users=trips)

@app.route('/infoScooters',methods = ['POST', 'GET'])
def infoScooters():
   cur.execute("SELECT numero, plainte, charge FROM scooters ORDER BY numero ASC")
   trips = cur.fetchall()
   return render_template('infoScooters.html', users=trips)

@app.route('/introPlainte',methods = ['POST', 'GET'])
def introPlainte():
   return render_template('introPlainte.html')

@app.route('/infoPlainte',methods = ['POST', 'GET'])
def infoPlainte():
   numTrottinette = request.form['numTrottinette']
   result = "Une demande a deja ete introduite ou la trottinette n'existe pas."
   cur.execute("SELECT s.plainte FROM scooters s WHERE s.numero=%s",(numTrottinette,))
   scooter = cur.fetchone()
   if scooter != None and not scooter[0] :
      cur.execute("UPDATE scooters SET plainte=%s WHERE numero=%s",("t",numTrottinette,))
      conn.commit()
      cur.execute("INSERT INTO reparations (scooter, userID, complainTime) VALUES (%s, %s, to_timestamp('"+datetime.datetime.now().isoformat()+"','YYYY-MM-DD\"T\"HH24:MI:SS\'))",(numTrottinette, session['userID']))
      conn.commit()
      result = 'La demande de plainte pour la trottinette numero: '  + numTrottinette + ' a ete introduite.'
   return render_template('printMessage.html', result = result)

@app.route('/consultTrips',methods = ['POST', 'GET'])
def consultTrips():
   userID = session['userID']
   cur.execute("SELECT * FROM trips t WHERE t.userID=%s ORDER BY t.endTime ASC",(userID,))
   trips = cur.fetchall()
   return render_template('consultTrips.html', users=trips)

#========================================USER WITH CHARGE RIGHTS========================================================
@app.route('/manageCharge',methods = ['POST', 'GET'])
def manageCharge():
   return render_template('manageCharge.html')

@app.route('/loadingScooter',methods = ['POST', 'GET'])
def loadingScooter():
    form = request.form
    numTrottinette = form['numTrottinette']
    result = "La trottinette numero: "  + numTrottinette + " n'existe pas ou n'est pas disponible."
    cur.execute("SELECT s.numero FROM scooters s WHERE s.numero=%s AND s.disponible=%s",(numTrottinette,"t"))
    scooter = cur.fetchone()
    if scooter != None:
        cur.execute("SELECT trips.destinationX, trips.destinationY FROM trips  JOIN (SELECT max(endTime) endTime FROM trips WHERE scooter=%s) t1 ON trips.endTime=t1.endTime", (scooter,))
        res=cur.fetchone()
        sourceX = res[0]
        sourceY = res[1]
        cur.execute("SELECT s.charge FROM scooters s WHERE s.numero=%s",(numTrottinette,))
        initialLoad=cur.fetchone()
        cur.execute("INSERT INTO reloads(scooter,user_id,initialLoad,sourceX,sourceY,startTime) VALUES (%s,%s,%s,%s,%s,to_timestamp('"+datetime.datetime.now().isoformat()+"','YYYY-MM-DD\"T\"HH24:MI:SS\'))",(numTrottinette,session['userID'],initialLoad,sourceX,sourceY,))
        conn.commit()
        cur.execute("UPDATE scooters SET disponible=%s WHERE numero=%s",("f",numTrottinette,))
        conn.commit()
        result = 'La trottinette numero: '  + numTrottinette + ' est en cours de chargement.'
    return render_template('printMessage.html', result = result)
                    
@app.route('/loadedScooter',methods = ['POST', 'GET'])
def loadedScooter():
    form = request.form
    numTrottinette = form['numTrottinette']
    destinationX=form['destinationX']
    destinationY=form['destinationY']
    result = "La trottinette numero: "  + numTrottinette + " n'est pas en chargement."
    cur.execute("SELECT reloads.scooter FROM reloads WHERE scooter=%s AND reloads.endTime IS NULL AND reloads.user_id =%s",(numTrottinette,session['userID'], ))
    scooter = cur.fetchone()
    if scooter != None:
        cur.execute("UPDATE reloads SET finalLoad=4,destinationX=%s,destinationY=%s,endTime=to_timestamp('"+datetime.datetime.now().isoformat()+"','YYYY-MM-DD\"T\"HH24:MI:SS\') WHERE scooter=%s AND endTime IS NULL",(destinationX,destinationY,numTrottinette,))
        conn.commit()
        cur.execute("UPDATE scooters SET disponible=%s WHERE numero=%s",("t",numTrottinette,))
        conn.commit()
        result = 'La trottinette numero: '  + numTrottinette + ' a bien ete remise en service.'
    return render_template('printMessage.html', result = result)

#========================================MECHANIC PAGES=================================================================
@app.route('/mechanic',methods = ['POST', 'GET'])
def mechanic():
    
    return render_template('mechanic.html', users=trips)

@app.route('/manageScooter',methods = ['POST', 'GET'])
def manageScooter():
    return render_template('manageScooter.html')

@app.route('/introScooter',methods = ['POST', 'GET'])
def introScooter():
    modeleTrottinette = request.form['modeleTrottinette']
    cur.execute("SELECT MAX(s.numero) FROM scooters s")
    numTrottinette=int(cur.fetchone()[0])
    numTrottinette = str(numTrottinette+1)
    cur.execute("INSERT INTO scooters(numero,miseEnService,modele,plainte,charge,disponible) VALUES (%s, to_timestamp('"+datetime.datetime.now().isoformat()+"','YYYY-MM-DD\"T\"HH24:MI:SS\'),%s,%s,%s,%s)",(numTrottinette, modeleTrottinette,"f",4,"t"))
    conn.commit()
    result = 'La trottinette numero: '  + numTrottinette + ' a bien ete ajoutee au systeme.'
    return render_template('printMessage.html', result = result)

@app.route('/deleteScooter',methods = ['POST', 'GET'])
def deleteScooter():
    numTrottinette = request.form['numTrottinette']
    result = "La trottinette numero: "  + numTrottinette + " n'existe pas."
    cur.execute("SELECT s.numero FROM scooters s WHERE s.numero=%s",(numTrottinette,))
    scooter = cur.fetchone()
    if scooter != None:
        cur.execute("DELETE FROM scooters WHERE numero = %s",(numTrottinette,))
        conn.commit()
        result = 'La trottinette numero: '  + numTrottinette + ' a bien ete supprimee du systeme.'
    return render_template('printMessage.html', result = result)

@app.route('/actuScooter',methods = ['POST', 'GET'])
def actuScooter():
    return render_template('actuScooter.html')

@app.route('/manageComplaints',methods = ['POST', 'GET'])
def manageComplaints():
    return render_template('manageComplaints.html')

@app.route('/scooterRepaired',methods = ['POST', 'GET'])
def scooterRepaired():
    numTrottinette = request.form['numTrottinette']
    commentaire= request.form['commentaire']
    result = "Aucune plainte n'a ete introduite pour cette trottinette."
    cur.execute("SELECT s.scooter FROM reparations s WHERE s.scooter=%s AND s.repaireTime IS NULL",(numTrottinette,))
    plainte = cur.fetchone()
    if plainte != None :
        cur.execute("UPDATE scooters SET plainte=%s,disponible=%s WHERE numero=%s",("f","t",numTrottinette,))
        conn.commit()
        cur.execute("UPDATE reparations SET repaireTime=to_timestamp('"+datetime.datetime.now().isoformat()+"','YYYY-MM-DD\"T\"HH24:MI:SS\'), mechanic=%s,commentaire=%s WHERE scooter=%s AND repaireTime IS NULL",(session['userID'],commentaire,numTrottinette,))
        conn.commit()
        result = 'La trottinette numero: '  + numTrottinette + ' a bien ete reparee.'
        return render_template('printMessage.html', result = result)

@app.route('/promoteUser',methods = ['POST', 'GET'])
def promoteUser():
   return render_template('promoteUser.html')

@app.route('/requetePromoteUser',methods = ['POST', 'GET'])
def requetePromoteUser():
    form = request.form
    userID = form['UserID']
    result="L'utilisateur dispose deja du droit de recharge ou n'existe pas."
    cur.execute("SELECT s.id FROM nUser s WHERE s.id=%s AND s.id not in ( SELECT id FROM CHARGER_USER)",(userID,))
    res = cur.fetchone()
    if res != None :
        result = "L'utilisateur : "+ userID + " dipose maintenant des droits de recharge."
        firstName=form['firstName']
        name=form['name']
        phone=form['phone']
        road=form['road']
        roadNum=form['roadNum']
        codePostal=form['codePostal']
        commune=form['commune']
        cur.execute("INSERT INTO charger_user (id,firstname,lastname,phoneNum,road,roadNum,codePostal,commune) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",(userID,firstName,name,phone,road,roadNum,codePostal,commune,))
        conn.commit()
    return render_template('printMessage.html', result=result)

@app.route('/printRequests',methods = ['POST', 'GET'])
def printRequests():
   cur.execute(R1)
   Re1 = cur.fetchall()
   cur.execute(R2)
   Re2 = cur.fetchall()
   cur.execute(R3)
   Re3 = cur.fetchall()
   cur.execute(R4)
   Re4 = cur.fetchall()
   cur.execute(R5)
   Re5 = cur.fetchall()
   return render_template('printRequests.html', R1=Re1, R2=Re2, R3=Re3, R4=Re4, R5=Re5)

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
