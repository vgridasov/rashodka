import csv, sys, os

project_dir = "/home/gva/PycharmProjects/rashodka/rashodka/"

sys.path.append(project_dir)

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

import django

django.setup()

from wares.models import Ware, Vendor

data = csv.reader(open("/home/gva/PycharmProjects/rashodka/data.csv"), delimiter=",")

for row in data:
    if row[0] != "Наименование":
        ware = Ware()
        ware.ware_name = row[0]
        ware.ware_code = row[1]
        # ware.ware_vendor = Vendor.vendor_name[int(row[2])]
        ware.ware_description = row[3]
        ware.save()
