import csv
# from django.db import models

from app.models import Store, Region


def import_csvdata(filepath):
    with open (filepath, 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
       

    for row in reader:

        region1, created = Region.objects.get_or_create(name=region1)
        
        sto = Store(
            #store_ID = row[0],
            address = row[1],
            manager = row[2],
            #number_of_salespersons = row[3],
            region = Region.objects.get_or_create(name=region1),
             )
        
        print(sto)
        sto.save()

#if __name__ == '__main__':
 
csv_file_path = 'store.csv'
import_csvdata(csv_file_path)

   #Region() got unexpected keyword arguments: 'region'
