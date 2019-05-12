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



SELECT EXISTS( SELECT * FROM table_articles WHERE id=42 ) AS article_exists;


SET colonne_1 = 'valeur 1', colonne_2 = 'valeur 2', colonne_3 = 'valeur 3'
