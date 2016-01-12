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

        restaurant_ratings["line[0]"] = line[1]

        print restaurant_ratings

        # for line[0] not in restaurant_ratings.keys():
            # restaurant_ratings[line[0]] = restaurant_ratings.get("line[0]", 0) + 1
       
            









    filename.close()