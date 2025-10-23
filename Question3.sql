-- QUESTION 3

-- We need to perform a currency exchange.
-- Without currency exchange, AUS outperforms UK, FR, DE which does not fit with rankings 
-- by units sold (historical data), customers or stores in each region (snapshot data)
SELECT cr.Name AS Country,
	SUM(CASE WHEN soh.CurrencyRateID IS NULL -- Note: AverageRate is always USD -> Another currency 
		THEN soh.SubTotal 
		ELSE soh.SubTotal / exch.AverageRate END) 
-- Did not use EndOfDayRate to account for transactions being taken at any time of day
	AS TotalRevenueUSD -- Did not used Total Due to account for Taxes + Freight Costs
FROM Sales.SalesOrderHeader AS soh 
	JOIN Sales.SalesTerritory AS st 
		ON soh.TerritoryID = st.TerritoryID 
	JOIN Person.CountryRegion AS cr
		ON st.CountryRegionCode = cr.CountryRegionCode  -- These two joins were to get the full country names
	LEFT JOIN Sales.CurrencyRate AS exch -- CRUCIAL that it is a LEFT join to prevent duplicates 
		ON exch.CurrencyRateID = soh.CurrencyRateID 
WHERE soh.ModifiedDate BETWEEN '2011-05-31' AND '2014-05-31'
-- SalesOrderHeader Data from June 2011 to July 2014 BUT CurrencyRate Data from May 2011 to May 2014 
-- Therefore we're looking at Total Revenue within this time frame. 
GROUP BY cr.Name 
ORDER BY TotalRevenueUSD; 

-- Without Exchance
SELECT cr.Name AS Country,
       SUM(soh.SubTotal) AS TotalRevenue
FROM Sales.SalesOrderHeader AS soh 
    JOIN Sales.SalesTerritory AS st 
        ON soh.TerritoryID = st.TerritoryID 
    JOIN Person.CountryRegion AS cr
        ON st.CountryRegionCode = cr.CountryRegionCode
WHERE soh.ModifiedDate BETWEEN '2011-05-31' AND '2014-05-31'
GROUP BY cr.Name 
ORDER BY TotalRevenue;

-- Follow up Question: Explain the country rankings in revenue.
-- Australia (AUS) and Germany (DE) have been operating for a shorter period of time:
-- (opening last year, mid-2013), while the others opened in mid-2011 (Mostly US) /2012 (US+CA+GB) 
-- Possibly explaining weaker revenue in DE and AUS. 
-- On a smaller note, the US had some entity closures but has the biggest operations
-- CA one closure but it seemed to be more of a relocation as another entity popped up. 
SELECT CountryRegionCode, BusinessEntityID, StartDate, EndDate  -- EndDate indicates a store closure. 
FROM Sales.SalesTerritoryHistory AS th
	JOIN Sales.SalesTerritory AS t 
		ON t.TerritoryID= th.TerritoryID 
ORDER BY StartDate;

-- Note: This is a snapshot of data as at 2014-09-12
-- How many stores are there is each region? 
-- How many customers do we get per store? 
SELECT cr.Name AS Country, 
	COUNT(DISTINCT c.StoreID) AS NumStores, 
	COUNT(DISTINCT c.CustomerID) AS NumCustomers 
-- COUNT(DISTINCT c.CustomerID) / COUNT(DISTINCT c.StoreID) AS CustomersPerStore 
-- Just to demonstrate this data is a snapshot
FROM Sales.Customer AS c
	JOIN Sales.SalesTerritory AS t 
		ON t.TerritoryID = c.TerritoryID 
	JOIN Person.CountryRegion AS cr 
		ON cr.CountryRegionCode = t.CountryRegionCode 
WHERE c.StoreID IS NOT NULL 
-- THERE ARE A LOT OF NULLS (representing customers who have not revisited recently but came at least once)
GROUP BY cr.Name
ORDER BY NumCustomers; 
-- The US has the most stores, CA is runner up. 
-- FR, DE, GB AND AU has an equal number of stores. 
-- This fits perfectly with the revenue. 
-- But still why does CA and GB have similar revenues?

-- NumUnitsSold by Country
SELECT SUM(sod.OrderQty) AS NumUnitsSold, 
	t.CountryRegionCode AS Country 
FROM Sales.SalesOrderHeader AS soh -- This table's last date is '2014-06-30'
	JOIN Sales.SalesOrderDetail AS sod 
		ON soh.SalesOrderID = sod.SalesOrderID
	JOIN Sales.SalesTerritory AS t 
		ON t.TerritoryID = soh.TerritoryID
WHERE soh.ModifiedDate BETWEEN '2011-05-31' AND '2014-05-31' 
GROUP BY t.CountryRegionCode
ORDER BY NumUnitsSold DESC;

-- What are they buying? How can we maximise revenue per country? 
-- We can do more targetted promotions.
-- note: The data in this table are pre-tax/freight cost sales. 
SELECT DISTINCT sod.UnitPrice, 
	SUM(sod.OrderQty) AS NumUnitsSold, 
	COUNT(CASE WHEN sod.UnitPriceDiscount > 0 THEN 1 END) AS NumDiscountsGiven, 
	t.CountryRegionCode AS Country 
FROM Sales.SalesOrderHeader AS soh 
	JOIN Sales.SalesOrderDetail AS sod 
		ON soh.SalesOrderID = sod.SalesOrderID
	JOIN Sales.SalesTerritory AS t 
		ON t.TerritoryID = soh.TerritoryID
GROUP BY sod.UnitPrice, t.CountryRegionCode
ORDER BY t.CountryRegionCode ASC, sod.UnitPrice DESC;
-- Note: UnitPrice in sod does not match ListPrice in PriceHistory (even when month/year modified are the same) 
-- Yet, it was never registered that a discount was given. This discrepancy needs to be followed up. 

-- TROUBLESHOOTING
SELECT 
    cr.Name AS Country,
    COUNT(*) AS TotalOrders,
    SUM(CASE WHEN soh.CurrencyRateID IS NULL THEN 0 ELSE 1 END) AS OrdersWithExchange,
    SUM(CASE WHEN soh.CurrencyRateID IS NULL THEN 1 ELSE 0 END) AS OrdersWithoutExchange,
    AVG(CASE WHEN soh.CurrencyRateID IS NOT NULL THEN exch.AverageRate END) AS AvgExchangeRate,
    AVG(CASE WHEN soh.CurrencyRateID IS NOT NULL THEN exch.EndOfDayRate END) AS AvgEndOfDayRate
FROM Sales.SalesOrderHeader AS soh 
    JOIN Sales.SalesTerritory AS st ON soh.TerritoryID = st.TerritoryID 
    JOIN Person.CountryRegion AS cr ON st.CountryRegionCode = cr.CountryRegionCode
    LEFT JOIN Sales.CurrencyRate AS exch ON exch.CurrencyRateID = soh.CurrencyRateID 
WHERE soh.ModifiedDate BETWEEN '2011-05-31' AND '2014-05-31'
GROUP BY cr.Name
ORDER BY OrdersWithoutExchange DESC;

