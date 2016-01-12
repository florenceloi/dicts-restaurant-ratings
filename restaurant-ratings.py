# Pseudocode:
# open file
# open an empty dictionary
# r.strip 
# split

# put everything in dictionary 
# then put in alphabetize 

# print a list of restaurants and ratings 

def print_restaurant_ratings(filename):

    restaurant_ratings = {}

    the_file = open(filename)

    for line in the_file: 
        line = line.rstrip()
        line = line.split(":")
        name = line[0]
        rating = line[1]

        restaurant_ratings[name] = rating 
        # restaurant_ratings[restaurant[0]] = line[1]

    sorted_restaurants = sorted(restaurant_ratings)
    # print sorted_restaurants

    #OPTION 1 to print sentence
    # for i in range(len(sorted_restaurants)):
        # print sorted_restaurants[i] + " is rated at " + restaurant_ratings.get(sorted_restaurants[i])
    
    #OPTION 2 to print sentence
    for restaurant_name in sorted_restaurants:
        print restaurant_name + " is rated at " + restaurant_ratings.get(restaurant_name)
            # for restaurant, ratings in restaurant_ratings.items():
                # print "%s is rated at %d." % (restaurant, ratings)

        # for line[0] not in restaurant_ratings.keys():
            # restaurant_ratings[line[0]] = restaurant_ratings.get("line[0]", 0) + 1
    
    the_file.close()

print_restaurant_ratings("scores.txt")            