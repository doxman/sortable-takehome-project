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
        matchingWeights = [0] * len(products)

        currentMax = 0
        maxIndex = 0

        # Evaluate how well the listing matches each product
        # Assume that product_name is never actually matched (because of underscores, etc)
        # Matching model + manufacturer is required, matching family is "nice-to-have"
        for idx, val in enumerate(products):
            if listing['title'].find(val['model']) != -1:
                matchingWeights[idx] += 2

            # The 'family' field is optional, so we need to be sure it exists
            if 'family' in val and listing['title'].find(val['family']):
                matchingWeights[idx] += 1

            if matchingWeights[idx] > currentMax:
                currentMax = matchingWeights[idx]
                maxIndex = idx

        # If we found no close matches, skip this listing
        if currentMax <= 1:
            continue

        # Now add this to the best-match product's list
        results[products[maxIndex]['product_name']]['listings'].append(listing)


# Output results
with open('results.txt', 'w') as resultsFile:
    for result in results.values():
        json.dump(result, resultsFile)
        resultsFile.write("\n")
