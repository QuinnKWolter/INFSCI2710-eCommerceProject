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
1. :yellow_square:Scripts for Products, Categories, Transactions, Reviews, Customers.
2. :yellow_square:Figure out stock/inventories/support structure in models.py with Logan for reports?
3. :red_square:[Generate Database Diagram/ERD with Django Extensions](https://www.linkedin.com/pulse/generate-database-diagramerd-django-extensions-automatically-srujan-s/)
4. 🟩Scripts for Salespersons, Stores, and Regions from Rody.
5. 🟥Look at base.html and do any prettification/styling that you'd like.
6. 🟥Check and fill in your respective portions of the shared report Google Doc.

### Rody:
1. :yellow_square:Data/Script for Regions, Stores, Salespersons.
2. :red_square:Very Basic Simple Product Widget.
3. :red_square:Create a Google Doc skeleton for the report.
   - Share with us.
4. :red_square:Mock up a home page.
   - Just copy and paste your widget a few times with different images/titles/prices.
5. 🟥Check and fill in your respective portions of the shared report Google Doc.

### Logan:
1. :green_square:Checkout/Payment interfaces.
2. :yellow_square:Work on models.py with Kishor to finalize transactions, carts, customers, etc.
3. :green_square:More logic for cart, increase quantity rather than having multiple entries.
4. 🟨Permissions for different user authorization levels.
5. 🟥Check and fill in your respective portions of the shared report Google Doc.

### Quinn:
1. :yellow_square:Merge Logan's frontend work + Run Kishor's scripts
2. :green_square:Products and Category Products in a DataTable
3. :green_square:Media resources
4. :yellow_square:Aggregation/Reporting dashboard
5. 🟥Stripe integration.
6. 🟥Check and fill in your respective portions of the shared report Google Doc.
