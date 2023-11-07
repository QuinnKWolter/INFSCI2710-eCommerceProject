import pandas 
from app.models import Review, Category

reviews = pandas.read_csv('reviews.csv')

for i,row in enumerate(reviews.itertuples()):
    # if i > 10000:
    #     break
    try:
        cust = Customer.objects.get(reviewer_id = row.reviewerID)
        Product.objects.get(asin = row.asin)
    except:
        continue
    rev = Review(
        customer = cust,
        product = prod,
        rating = int(row.rating)
    )
    rev.save()