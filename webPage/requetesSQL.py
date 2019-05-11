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

R2 = """select user_id, count(scooter)              --pas fini
        from (
        select r.user_id user_id, r.scooter scooter from reloads r
        union all
        select t.userID, t.scooter scooterC from trips t
        ) c
        group by user_id
        HAVING count(c.scooter)= scooter(c.scooterC)
        ORDER BY user_id ASC
    """

"""SELECT  Amount, Date
    FROM reloads
    LEFT JOIN trips
    ON Customers.ID = Orders.Customer_id
    INTERSECT
    SELECT  ID, NAME, Amount, Date
    FROM Customers
    RIGHT JOIN Orders
    ON Customers.ID = Orders.Customer_id
    """

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
