SELECT sp.name
FROM SalesPerson AS sp
where sp.name not in (
    SELECT sp.name 
    FROM SalesPerson AS sp 
        LEFT JOIN Orders AS o ON sp.sales_id = o.sales_id 
        LEFT JOIN Company AS c ON o.com_id = c.com_id 
    WHERE c.name = "RED"
)