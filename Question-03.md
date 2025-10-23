## Question
What is the relationship between Country and Revenue?

## Files (in chronological order of production)
- The AdventureWorks2019 file can be found [here](https://learn.microsoft.com/en-us/sql/samples/adventureworks-install-configure?view=sql-server-ver17&tabs=ssms)
- [Question3 (SQL Server Script)](/Question3.sql)
- [mainCountryRev](/mainCountryRev.csv)
- [CountryCustomers](/CountryCustomers.csv)
- [CountryUnits](/CountryUnits.csv)
- [FormingTargets](/FormingTargets.csv)
- [submit3 (Python Script)](/submit3.py)
  
## Process
### Primary Analysis
Countries were already identified in Question 1. Only three years of sales data (June 2011- 
May 2014) was used to answer the question as these dates overlapped in the tables
joined; Sales.SalesOrderHeader and Sales.CurrencyRateID. Revenue was
operationalised as SubTotal as it SubTotal = TotalDue- (TaxAmt + Freight). A crucial
methodological step was converting revenue to USD to ensure a fair comparison. It was
identified that FromCurrencyCode were all USD and the AverageRate was multiplied by
the SubTotal for transactions where the CurrencyRateID was not null (i.e. a transaction
took place). To ensure currency exchange fit, the aggregated revenue for each Country
was also calculated and evaluated against underlying drivers for revenue. A bar graph
was sufficient in representing this revenue by country as performed in Question 1.

### Follow-Up Analysis
The operational footprint (number of stores, customers) and sales volume (units sold)
were distributed amongst each country and graphed against revenue. It was found that the
converted revenues in USD were a better fit when ordered. This was most evidenced by
the rank of Australia’s revenue without currency exchange which would have outpaced
Germany, France and the United Kingdom despite being a newer store (operating for less
than a year) and holding smaller shares in the operational footprint and sales volume. A
bar graph with a line graph overlaid was utilised to emphasise the connection between
revenue and underlying factors.

Nevertheless, a discrepancy existed between Canada and the United Kingdom with CA
having equal revenue to the UK despite having double the size of operations. Product
pricing by country consumption was analysed and found no difference in distribution
among the 6 countries. A 100% stacked bar chart was utilised to more easily compare the
between price points as total consumption varied by country. Therefore, the currency
exchange process was analysed for inconsistencies in the number of recorded
transactions and conversion rates. This was not graphed but tabulated as it requires
careful consideration in further investigation by the finance department. In other words, a
graph would add no value to the case.

## Answer 
The United States is the dominant market, generating over twice the revenue of all other
countries combined. This leadership is directly explained by its larger operational scale,
having the most stores and customers. The revenue ranking is perfectly aligned with the
number of stores and customers in each country, confirming that scale is the primary
revenue driver. The lower revenue for Australia and Germany is further explained by their
later market entry in mid-2013. Prioritize marketing investment and potential store
expansion in Canada and the UK, as they are the strongest performers after the US. For
Australia and Germany, focus on customer acquisition strategies to build their market
presence post-launch.

The currency exchange process increased the accuracy of the analysis however could not
provide 100% accuracy. For the United States, there were 21 counts (0.18%) of
transactions occurred with a currency exchange despite all starting currencies within the
codes being USD. While this represents less than 1% of transaction, this indicates that
currency exchange took place where it was not necessary and must be investigated in
case of money laundering. For the UK, nearly 100% of orders used currency conversion,
missing 3 counts (0.1%) and for Canada, 98.6% of orders used currency conversion,
missing 53 counts (1.4%). While these figures are excellent, the finance department can
strive towards an achievable 100% success rate.

In Germany and France there are also missed counts; 8.53% and 4.44% respectively.
While different companies may handle these transactions due to geographical reasons,
Germany and France both entered the eurozone in 1999 and therefore should have
similar conversion rates. France’s conversion rate is an alarming 4EUR to 1USD. The
finance departments are urged to immediately investigate the issues in currency exchange
identified and renegotiate all conversion exchange rates for competitive pricing. This
would ensure that AdventureWorks does not lose money on routine procedures, such as
currency exchange, which in turn affect product pricing.

It is possible to perform imputation by pulling currency codes online but actual transactions
change among cash vendors. Furthermore, it is unreasonable that many consumers in
these territories paid in USD and thus, it can be assumed that such data is missing. To be
certain, the IT department should introduce a CurrencyCode 0 to indicate no exchange
took place and distinguish from where data is missing. Moreover, the UnitPrice in
Sales.SalesOrderDetails does not match ListPrice in Sales.SalesPriceHistory (even when
month/year modified are the same). This indicates a discount was given or a grave
discrepancy between SalesOrderDetails and ListPrice. This must be followed up to
understand why the product price was not sold at the price in which it was set to be sold.

## Visuals
- [Figure 3.1](/Fig1.png)
- [Figure 3.2](/Fig2.png)
- [Figure 3.3](/Fig3.png)
