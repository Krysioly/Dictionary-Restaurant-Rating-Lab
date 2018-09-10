"""Restaurant rating lister."""


# put your code here

import sys

def get_restaurant_ratings(input_file):
    ratings_dict = {}

    file = open(input_file)
    for line in file:
        restaurant_name, rating = line.rstrip().split(":")
        ratings_dict[restaurant_name]= rating
    
    new_restaurant = input("What is your restaurant name?: ").title()
    new_rating = input("What do you rate your restaurant on a scale of 1 to 5?: ")

    ratings_dict[new_restaurant] = new_rating

    sorted_restaurants_list = sorted(ratings_dict)

    for restaurant in sorted_restaurants_list:
        rating = ratings_dict[restaurant]
        print("{} is rated at {}.".format(restaurant, rating))

get_restaurant_ratings(sys.argv[1])
