# # your code goes here
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

        restaurant_ratings[line[0]] = line[1]

    sorted_restaurants = sorted(restaurant_ratings)
        # print sorted_restaurants

    for i in range(len(sorted_restaurants)):
        print sorted_restaurants[i] + " is rated at " + restaurant_ratings.get(sorted_restaurants[i])
        # for restaurant in sorted_restaurants:
            # print restaurant + " is rated at " + restaurant_ratings.get(restaurant)
            # for restaurant, ratings in restaurant_ratings.items():
                # print "%s is rated at %d." % (restaurant, ratings)

        # for line[0] not in restaurant_ratings.keys():
            # restaurant_ratings[line[0]] = restaurant_ratings.get("line[0]", 0) + 1
    
    the_file.close()

print_restaurant_ratings("scores.txt")            









    