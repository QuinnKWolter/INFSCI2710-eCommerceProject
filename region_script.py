import csv
#import sys
#from django.db import models
from app.models import Region



def import_csv_data(filepath):
    with open (filepath, 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        
        for row in reader:
            
            obj = Region(
               #region_ID = row[0],
                name = row[1],
                region_manager = row[2])
            
            print(obj)
            #sys.stdout.flush()
            obj.save()
          
#if __name__ == '__main__':
csv_file_path = 'region.csv'
import_csv_data(csv_file_path)


