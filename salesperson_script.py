import csv
# from django.db import models
from app.models import Salesperson

def import_csvdata(filepath):
    with open (filepath, 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)

        for row in reader:
            
            sale = Salesperson(
                name = row[0],
                address = row[1],
                e_mail = row[2],
                job_title = row[3],
                store_assigned= row[4],
                salary = row[5]
            )
            print(sale)
            sale.save()

if __name__ == '__main__':

    csv_file_path = '/Users/chiedozieekeke/Documents/Database Management/Database e-commerce project/e-Commerce project/INFSCI2710-eCommerceProjectFK.salesperson.csv'
    import_csvdata(csv_file_path)