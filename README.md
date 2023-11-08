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
5. :red_square:Renovate stylings and visualizations for the pages.
6. 🟥"REPORT: A graphical schema of the database using the E-R diagram with a short description of
each entity set, relationship set and their corresponding attributes."
7. 🟥"REPORT: A set of relational schema resulting from the E-R diagram with identification of primary
and foreign keys."

### Rody:
1. :yellow_square:Data/Script for Regions, Stores, Salespersons
2. :red_square:Very Basic Simple Product Widget
3. :red_square:Create a Google Doc skeleton for the report
   - Share with us
4. :red_square:Mock up a home page.
   - Just copy and paste your widget a few times with different images/titles/prices
5. 🟥Get the application up and running locally, get your Contact/About page served properly. (urls.py, views.py, mimic our templates)
6. 🟥Once models.py is finished and done, "REPORT: The DDL statements to create the relational schema in some appropriate Normal Form, with identification and justification of the Normal Form."

### Logan:
1. :yellow_square:Checkout/Payment interfaces.
2. :red_square:Work on models.py with Kishor to finalize transactions, carts, customers, etc.
3. :yellow_square:More logic for cart, increase quantity rather than having multiple entries. Logic for handling stock values being outdated, logic for redirects under different circumstances.
4. :red_square:Create the widget for user reviews on a given Product detail page.
5. :red_square:"REPORT: A list of assumptions that you have made about the system."
6. :red_square:"REPORT: A description of your front-end design as well as the front-end to back-end connection."

### Quinn:
1. :yellow_square:Merge Logan's frontend work + Run Kishor's scripts
2. :green_square:Products and Category Products in a DataTable
3. :green_square:Media resources
4. :yellow_square:Aggregation/Reporting dashboard
5. :red_square:Writeups for the report on technical stack, testing procedures, etc.
6. 🟥"REPORT: A short overview of the system including identification of the various types of users, administrators, etc. who will be accessing the system in various ways."
7. 🟥"REPORT: A description of your testing efforts and erroneous cases that your system can detect and handle."
8. 🟥"REPORT: A description of the system's limitations and the possibilities for improvements."
