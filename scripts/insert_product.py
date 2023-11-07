import pandas 
from app.models import Product, Category

electronics = pandas.read_csv('electronics.csv')

for row in electronics.itertuples():
    prod = Product(
        asin = row.asin,
        description = row.title,
        price = row.price,
        # stock = 10,
        category = Category.objects.get(unique_id = row.category_id),
        image = row.imgUrl
    )
    prod.save()