# INFSCI2710-eCommerceProject
INFSCI2710 eCommerce Project

## Interfaces
1. Home Page (Top Products?)
	- Search functionality built in?
2. Categories List
3. Specific Category Page
	- Table of products for this category
	- Search functionality
4. About Page / Contact Us
	- Static page
5. Cart structure on given pages that follows user around?
6. Sales Interface (Shipping info? Quantities of products?)
7. Payment Interface (Enter some card details, hit "Checkout")
8. New Inventory (Add Stock quantities to Regions, indicate Manager ordering?)
	- PERFORMED THROUGH DJANGO ADMIN
9. New User Registration Interface
	- Conditional Logic for Home vs. Business
10. Transaction Summary Interface for below info!!
	
Data Aggregation The system must provide data aggregation queries:
1. What are the aggregate sales and profit of the products.
	- Aggregation of the "Transaction" objects by Product?
2. What are the top product categories.
	- Aggregation of "Transaction" objects by Category?
3. How do the various regions compare by sales volume?
	- Inventories..... something something?
4. Which businesses are buying given products the most?
	- All transactions where customer "Type" == "Business", sorted
5. Other interesting aggregate queries that you will come up with.
	- Will make up as we go
	
## ACTION ITEMS
### Kishor: 
[x] Continue to work on Product and Category processing/population
[] Script for Transactions
[] Script for Reviews
[] Script for Customers
[] Inventories?

### Rody
1. Data/Script for Regions (3ish regions?)
2. Data/Script for Stores (X stores per region)
3. Data/Script for Salespersons (A few mangers, a few associates)
4. About Page / Contact Us
5. Do the Django Tutorial!

### Logan
1. Login System & Sessions (forms.py)
2. Populate some fake data in Django Admin
3. Very Basic Simple Widgets (Product Widget, etc.)
4. Basic skeleton examples for home page, product page, category, sign in/new user, etc.
5. Learn about forms.py (will help with adding functionality to skeleton pages)
   
### Quinn
1. More skeleton pages (whatever is left)
2. Aggregation dashboard
3. CRUD interfaces for all models
4. Transaction + Checkout/Payment interfaces + Cart
5. Finish models.py
