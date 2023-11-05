# INFSCI2710-eCommerceProject
INFSCI2710 eCommerce Project

🟥 = Not Started
🟨 = In Progress
🟩 = Functionally Done
🟦 = Done & Pretty

## Anticipated Interfaces
1. :red_square:**Home Page**
   - Top Products?
     - Search functionality built in?
2. :yellow_square:**Categories List**
3. :yellow_square:**Specific Category Page**
   - Table of products for this category
   - Search functionality
4. :yellow_square:**About Page / Contact Us**
   - Static page
5. :yellow_square:**Cart Structure**
   - On given pages that follows user around?
6. :yellow_square:**Sales Interface**
   - Shipping info? Quantities of products?
7. :yellow_square:**Payment Interface**
   - Enter some card details, hit "Checkout"
8. :red_square:**New Inventory**
   - Add Stock quantities to Regions, indicate Manager ordering?
     - PERFORMED THROUGH DJANGO ADMIN
9. :yellow_square:**New User Registration Interface**
   - Conditional Logic for Home vs. Business
10. :yellow_square:**Transaction Summary Interface**
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
1. :yellow_square:Scripts for Products, Categories, Transactions, Reviews, Customers
2. :red_square:Figure out stock/inventories/support structure in models.py with Logan for reports?
3. :red_square:[Generate Database Diagram/ERD with Django Extensions](https://www.linkedin.com/pulse/generate-database-diagramerd-django-extensions-automatically-srujan-s/)
4. :red_square:Let Quinn know your thoughts on various aggregation logic needs (from above)

### Rody:
1. :yellow_square:Data/Script for Regions, Stores, Salespersons
2. :red_square:Very Basic Simple Product Widget
3. :red_square:Create a Google Doc skeleton for the report
   - Share with us
4. :red_square:Mock up a home page.
   - Just copy and paste your widget a few times with different images/titles/prices

### Logan:
1. :red_square:Checkout/Payment interfaces
2. :red_square:Work on models.py with Kishor to finalize transactions, carts, customers, etc.
3. :red_square:More logic for cart, increase quantity rather than having multiple entries

### Quinn:
1. :red_square:Merge Logan's frontend work + Run Kishor's scripts
2. :yellow_square:Products and Category Products in a DataTable
3. :green_square:Media resources
4. :yellow_square:Aggregation/Reporting dashboard
5. :red_square:Writeups for the report on technical stack, testing procedures, etc.
