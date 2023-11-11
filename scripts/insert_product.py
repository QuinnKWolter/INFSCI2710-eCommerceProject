import pandas 
from app.models import Product, Category

electronics = pandas.read_csv('electronics.csv')

for row in electronics.itertuples():
    prod = Product(
        asin = row.asin,
        description = row.title,
        price = row.price,
        # stock = 10,
        category = Category.objects.get(pk = row.category_id),
        image = 'product_images/' + row.imgUrl.split('/')[-1]
    )
    prod.save()