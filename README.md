#README

##Running the Code
The code for question 1 is in the `code/q1.py`. Before you run the code, you must install `Pandas`, and make sure the data is in the `data/` directory. To run the code, go to the main project directory and use the command \
`python code/q1.py`

You will see the following output in the terminal:\
`naive AOV is 3145.128`\
`average price per item is 357.92152221412965`

The `SQL` queries for question 2 are in teh following section.

##Answers
###Question 1
####1.a.
The naive way to calculate AOV is by summing the values in the "order_amount" column and divide the sum by the number of orders. However, this approach does not account for the number of items in each order. In the given dataset, some orders have 2000 items whereas other orders only have 1 item. The better way to evaluate the data is by calculating the average price per item (APPI). To calculate APPI, we can divide the total amount of orders by the total number of items.

####1.b.
The metric is average price per item (APPI). To calculate APPI, we can divide the total amount of orders by the total number of items.

####1.c.
The average price per item is 357.92.

###Question 2
####2.a.
The SQL query is \
`SELECT *
FROM (SELECT COUNT(OrderID) AS NumOrders, ShipperName
FROM (SELECT Orders.OrderID, Orders.ShipperID, Shippers.ShipperName
FROM Orders
INNER JOIN Shippers ON Orders.ShipperID=Shippers.ShipperID
GROUP BY Orders.OrderID)
GROUP BY ShipperName)
WHERE ShipperName='Speedy Express';`\
54 orders were shipped by Speedy Express.

####2.b.
The SQL query is \
`SELECT LastName, MAX(EmployeeOrderNum) AS MostOrderNum
FROM (SELECT *, COUNT(EmployeeID) AS EmployeeOrderNum
FROM (SELECT Employees.EmployeeID, Employees.LastName, Orders.OrderID FROM Employees
INNER JOIN Orders ON Employees.EmployeeID=Orders.EmployeeID)
GROUP BY EmployeeID);`\
The employee whose last name is Peacock has the most orders.

####2.C.
The SQL query is \
`SELECT ProductID, ProductName, MAX(TotalQuantity) AS MaxQuantity
FROM (SELECT Products.ProductID, Products.ProductName, Orders.OrderID, Orders.CustomerID, SUM(OrderDetails.Quantity) AS TotalQuantity, Customers.CustomerID, Customers.Country
FROM Products
INNER JOIN OrderDetails ON Products.ProductID=OrderDetails.ProductID
INNER JOIN Orders ON OrderDetails.OrderID=Orders.OrderID
INNER JOIN Customers ON Orders.CustomerID=Customers.CustomerID
WHERE Country='Germany'
GROUP BY Products.ProductID);`\
The most ordered product by customers in Germany is Boston Crab Meat.
