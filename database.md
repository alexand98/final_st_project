task #1

SELECT login, COUNT("Orders"."inDelivery")
FROM "Couriers"
INNER JOIN "Orders" ON "Couriers".id = "Orders"."courierId"
GROUP BY 1,"Orders"."inDelivery"
HAVING "Orders"."inDelivery" = true;


task #2

SELECT track,
CASE
    WHEN finished = true THEN '2'
    WHEN cancelled = true THEN '-1'
    WHEN "inDelivery" = true THEN '1'
    ELSE '0'
END AS Статус
FROM "Orders";