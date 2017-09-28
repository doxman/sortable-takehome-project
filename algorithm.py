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


# Loop through listings
with open('listings.txt', 'r') as listingsFile:
    for line in listingsFile:
        listing = json.load(StringIO(line))

        if listing['manufacturer'] not in manufacturers:
            continue # If there's no manufacturer match, skip this to be safe

        products = manufacturers[listing['manufacturer']]

        matchIndex = -1

        # Evaluate how well the listing matches each product
        # Assume that product_name is never actually matched (because of underscores, etc)
        for idx, val in enumerate(products):
            if 'family' in val:
                # family + model is sufficient in this case
                if listing['title'].find(val['family'] + " " + val['model']) != -1:
                    matchIndex = idx
                    break
            else:
                # manufacturer + model is required
                if listing['title'].find(val['manufacturer'] + " " + val['model']) != -1:
                    matchIndex = idx
                    break

        # If we found no close matches, skip this listing
        if matchIndex == -1:
            continue

        # Now add this to the best-match product's list
        results[products[matchIndex]['product_name']]['listings'].append(listing)


# Output results
with open('results.txt', 'w') as resultsFile:
    for result in results.values():
        json.dump(result, resultsFile)
        resultsFile.write("\n")
