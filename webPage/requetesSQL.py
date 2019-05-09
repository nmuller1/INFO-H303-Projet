R1 = """SELECT trips.scooter, trips.destinationX, trips.destinationy  
        FROM trips  
        JOIN (SELECT scooter, max(endTime) endTime 
            FROM trips GROUP BY scooter) T 
        ON trips.endTime=T.endTime 
        ORDER BY trips.scooter ASC
        """

R2 = """select user_id, count(scooter)              --pas finie
from (
        select r.user_id user_id, r.scooter scooter from reloads r
        union all
        select t.userID, t.scooter from trips t
     ) as combined
        group by user_id
        ORDER BY user_id ASC
    """

R4 = """SELECT scooter, COUNT(scooter)
        FROM reparations
        GROUP BY scooter
        HAVING COUNT(scooter) > 9
        """


