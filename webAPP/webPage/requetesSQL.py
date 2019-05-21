R1 = """SELECT trips.scooter, trips.destinationX, trips.destinationY  
        FROM trips  
        JOIN ((SELECT scooter, max(endTime) endTime 
            FROM trips GROUP BY scooter) t1
            INNER JOIN
            (SELECT numero FROM scooters WHERE disponible = 't') t2
            ON (t1.scooter = t2.numero)
            ) T 
        ON trips.endTime=T.endTime 
        ORDER BY trips.scooter ASC
        """

R2 ="""select c.userID --, count(c.scooter)
        from (
        select DISTINCT r.scooter scooter, r.user_id userID from reloads r
        INTERSECT
        select DISTINCT t.scooter, t.userID from trips t
        ) c
        group by c.userID
        HAVING count(c.scooter) = (SELECT COUNT(DISTINCT scooter) FROM reloads where user_id = c.userID)
        ORDER BY c.userID ASC
    """

"""SELECT user_id, COUNT(DISTINCT scooter) FROM reloads GROUP by user_id --to see all scooter recharge by user"""

R3 = """SELECT trips.scooter, SUM(SQRT(ABS(trips.destinationX - trips.sourceX)) + SQRT(ABS(trips.destinationY - trips.sourceY)))
    FROM trips
    GROUP BY trips.scooter
    HAVING SUM(SQRT(ABS(trips.destinationX - trips.sourceX)) + SQRT(ABS(trips.destinationY - trips.sourceY)))  = (
    SELECT MAX(sub.sumDist) maxDist FROM ( 
    SELECT t.scooter, SUM(SQRT(ABS(t.destinationX - t.sourceX)) + SQRT(ABS(t.destinationY - t.sourceY))) sumDist FROM trips t
    GROUP BY t.scooter
    ) sub )
"""

R4 = """SELECT scooter, COUNT(scooter)
        FROM reparations
        GROUP BY scooter
        HAVING COUNT(scooter) > 9
        ORDER BY scooter ASC
        """

R5 = """ SELECT t.userID, AVG(t.endTime-t.startTime), COUNT(t.userID),
        SUM(CASE 
            WHEN EXTRACT(hour FROM t.endTime-t.startTime) < 1 THEN EXTRACT(minute FROM t.endTime-t.startTime)*0.15
            WHEN EXTRACT(hour FROM t.endTime-t.startTime) > 1 THEN EXTRACT(HOUR FROM t.endTime-t.startTime)*6.5
            WHEN EXTRACT(DAY FROM t.endTime-t.startTime) > 1 THEN EXTRACT(DAY FROM t.endTime-t.startTime)*36 
        end)+COUNT(t.userID)
        FROM trips t
        GROUP BY t.userID
        HAVING COUNT(t.userID) > 10
        ORDER BY AVG(t.endTime-t.startTime) DESC
    """
