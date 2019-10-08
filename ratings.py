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

    add_more = "Yes"

    while add_more == "Yes":
        new_restaurant = input("Add a new restaurant name: ")
        new_rating = input("Please type an integer rating (1-5): ")

        while not new_rating.isnumeric() or int(new_rating) < 1 or 5 < int(new_rating):
            new_rating = input("Please enter a valid integer rating between 1 and 5: ")
        
        restaurant_ratings[new_restaurant] = new_rating
        add_more = input("Would you like to add another restauarant? Yes / No ").title()

    sorted_restaurants = sorted(restaurant_ratings)

    for restaurant in sorted_restaurants:
        print(f"{restaurant}: {restaurant_ratings[restaurant]}")
    
    file.close()

"""PSEUDOCODE
open file, get restaurant ratings from file

loop until don't add more:
    input for restaurant name
    input for restaurant score (rating)
    do you want to add another?

store restaurant + rating in dic
then sort
then iterate + print
"""

