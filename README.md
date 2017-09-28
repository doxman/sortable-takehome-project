# sortable-takehome-project
Product matching challenge from Sortable

## Environment
Tested in Python 2.7.12 on Linux Mint 18.2

## Running the code
Just clone this repo and then run `python algorithm.py` in the repo folder

## Reasoning

The program is written to minimize runtime while achieving its objectives. By splitting the products by manufacturer, the number of comparisons per listing is reduced significantly.

In other words, given *m* products and *n* listings (where *n* is expected to be much bigger than *m*), the runtime is roughly as follows:
- *O(m)* to read data from the products file (accessing dictionaries is O(1) on average)
- Less than *O(mn)* to read and match listings (each listing is compared to maybe 10% of products, thanks to the manufacturer split)
- *O(m)* to write data to the results file

By ensuring that listing and product manufacturers must match and that a matched listing's title must contain either family+model or manufacturer+model, the program is well protected against false matches.

## Concern

After running the program, results.txt contains only 4184 matched listings; this is slightly less than 20% of all listings. Without examining the input files in detail it is hard to say whether this low percentage accurately represents the listings file or if the program is missing a lot of matches.
