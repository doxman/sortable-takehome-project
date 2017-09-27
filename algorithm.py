import json
from StringIO import StringIO

manufacturers = {} # keys: manufacturer names, values: products with this manufacturer
results = {} # keys: product names, values: result objects

# Loop through products
with open('products.txt', 'r') as productsFile:
    for line in productsFile:
        product = json.load(StringIO(line))

        # Add to results
        results[product['product_name']] = {
            'product_name': product['product_name'],
            'listings': []
        }

        # Add to product array for this manufacturer, or create a new entry if we didn't have it yet
        if product['manufacturer'] in manufacturers:
            manufacturers[product['manufacturer']].append(product)
        else:
            manufacturers[product['manufacturer']] = [product]



with open('listings.txt', 'r') as listingsFile:
    for line in listingsFile:
        listing = json.load(StringIO(line))
