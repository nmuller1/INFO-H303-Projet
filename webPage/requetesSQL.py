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

R3 = """SELECT MAX(sub.sumDist) dist
    FROM (
    SELECT t.scooter, SUM(SQRT(ABS(t.destinationX - t.sourceX)) + SQRT(ABS(t.destinationy - t.sourcey))) sumDist
    FROM trips t
    GROUP BY t.scooter
    ) sub
"""

R4 = """SELECT scooter, COUNT(scooter)
        FROM reparations
        GROUP BY scooter
        HAVING COUNT(scooter) > 9
        """


