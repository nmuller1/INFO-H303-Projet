Installé flask2
Installé postgreSQL et le demarer avec: 
    $pg_ctl -D /usr/local/var/postgres start

Ouvrir le terminal dans le dossier base de donnée
Crée une base de donnée executer: $createdb (nom de votre db)
Executer : $python extractData
Puis     : $make ou $psql -d (nom de votre db) -f init.sql et $psql -d (nom de votre db) -f data.sql

Ouvrir le terminal dans le dossier pageWeb
Executer: $python2 server.py (nom de la db) (nom du proprietaire de la db)
Sur navigateur web : 127.0.0.1:5000