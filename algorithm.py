import json
from StringIO import StringIO

products = []
listings = []

with open("products.txt", "r") as productsFile:
    for line in productsFile:
        products.append(json.load(StringIO(line)))


with open("listings.txt", "r") as listingsFile:
    for line in listingsFile:
        listings.append(json.load(StringIO(line)))

