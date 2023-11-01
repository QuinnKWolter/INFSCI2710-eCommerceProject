# INFSCI2710-eCommerceProject
INFSCI2710 eCommerce Project

## Anticipated Interfaces

1. **Home Page**
   - Top Products?
     - Search functionality built in?
2. **Categories List**
3. **Specific Category Page**
   - Table of products for this category
   - Search functionality
4. **About Page / Contact Us**
   - Static page
5. **Cart Structure**
   - On given pages that follows user around?
6. **Sales Interface**
   - Shipping info? Quantities of products?
7. **Payment Interface**
   - Enter some card details, hit "Checkout"
8. **New Inventory**
   - Add Stock quantities to Regions, indicate Manager ordering?
     - PERFORMED THROUGH DJANGO ADMIN
9. **New User Registration Interface**
   - Conditional Logic for Home vs. Business
10. **Transaction Summary Interface**
   - For below info!!
   - **Data Aggregation**
     - The system must provide data aggregation queries:
       - What are the aggregate sales and profit of the products.
         - Aggregation of the "Transaction" objects by Product?
       - What are the top product categories.
         - Aggregation of "Transaction" objects by Category?
       - How do the various regions compare by sales volume?
         - Inventories..... something something?
       - Which businesses are buying given products the most?
         - All transactions where customer "Type" == "Business", sorted
       - Other interesting aggregate queries that you will come up with.
         - Will make up as we go

## ACTION ITEMS
### Kishor:
1. Scripts for Products, Categories, Transactions, Reviews, Customers
2. Figure out stock/inventories/support structure in models.py with Logan for reports?
3. [Generate Database Diagram/ERD with Django Extensions](https://www.linkedin.com/pulse/generate-database-diagramerd-django-extensions-automatically-srujan-s/)
4. Let Quinn know your thoughts on various aggregation logic needs (from above)

### Rody:
1. Data/Script for Regions, Stores, Salespersons
2. Very Basic Simple Product Widget
3. Create a Google Doc skeleton for the report
   - Share with us
4. Mock up a home page.
   - Just copy and paste your widget a few times with different images/titles/prices

### Logan:
1. Checkout/Payment interfaces
2. Work on models.py with Kishor to finalize transactions, carts, customers, etc.
3. More logic for cart, increase quantity rather than having multiple entries

### Quinn:
1. Merge Logan's frontend work + Run Kishor's scripts
2. Products and Category Products in a DataTable
3. Media resources
4. Aggregation/Reporting dashboard
5. Writeups for the report on technical stack, testing procedures, etc.
