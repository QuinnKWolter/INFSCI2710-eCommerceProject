from app.models import *
import random
import pandas
import datetime

salespersons = Salesperson.objects.all() #salesperson
reviews = Review.objects.all() #review
reviews_data = pandas.read_csv('reviews.csv')

for review in reviews:
    prod = review.product
    cust = review.customer
    sp = random.choice(salespersons)
    timestamp = reviews_data[
        reviews_data['EMAIL'] == cust.email
    ].iloc[0]['unixReviewTime']
    # print(timestamp)

    transaction = Transaction(
        customer = cust,
        salesperson = sp,
        date_ordered = datetime.datetime.fromtimestamp(timestamp),
        status = 'Delivered',
        total_price = prod.price,
        shipping_address = cust.street_address,
        city = cust.city,
        state = cust.state,
        zipcode = cust.zip_code
    )
    transaction.save()
