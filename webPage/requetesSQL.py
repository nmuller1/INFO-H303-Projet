R1 = """SELECT trips.scooter, trips.destinationX, trips.destinationy  
        FROM trips  
        JOIN (SELECT scooter, max(endTime) endTime FROM trips GROUP BY scooter) T 
        ON trips.endTime=T.endTime 
        ORDER BY trips.scooter ASC"""