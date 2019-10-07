"""Restaurant rating lister."""
"""
Unzip a file
Iterate over lines
split at : ==> list of 2 items
tuple the list 
dict the tuple ==> dictionary with key-value pairs
Use sorted() on the dictionary, save to a variable ==> alphabeized list of keys 
Iterate over the dictionary
    Unpacking and use item to index through dict
    print items (key + value)
"""

# put your code here
def print_restaurant_ratings(path):
    """Print restaurants alphabetically with their ratings."""

    file = open(path)

    restaurant_ratings = {}

    for line in file:
        restaurant_and_rating = line.rstrip().split(':')
        restaurant_ratings[restaurant_and_rating[0]] = restaurant_and_rating[1]

    sorted_restaurants = sorted(restaurant_ratings)

    for restaurant in sorted_restaurants:
        print(f"{restaurant}: {restaurant_ratings[restaurant]}")
    
    file.close()