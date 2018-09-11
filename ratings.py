"""Restaurant rating lister."""


# put your code here

import sys

def make_restaurant_ratings_dict(input_file):
    ratings_dict = {}

    file = open(input_file)
    for line in file:
        restaurant_name, rating = line.rstrip().split(":")
        ratings_dict[restaurant_name]= rating
    
    return ratings_dict

    # new_restaurant = input("What is your restaurant name?: ").title()
    # new_rating = input("What do you rate your restaurant on a scale of 1 to 5?: ")

    # ratings_dict[new_restaurant] = new_rating

    # sorted_restaurants_list = sorted(ratings_dict)

    # for restaurant in sorted_restaurants_list:
    #     rating = ratings_dict[restaurant]
    #     print("{} is rated at {}.".format(restaurant, rating))


def add_new_restaurant(ratings_dict):
    new_restaurant = input("What is your restaurant name?: ").title()
    new_rating = input("What do you rate your restaurant on a scale of 1 to 5?: ")

    ratings_dict[new_restaurant] = new_rating
    return ratings_dict


def sort_and_print_restaurants(ratings_dict):
    sorted_restaurants_list = sorted(ratings_dict)

    for restaurant in sorted_restaurants_list:
        rating = ratings_dict[restaurant]
        print("{} is rated at {}.".format(restaurant, rating))


def rating_restaurants(input_file):

    ratings_dictionary = make_restaurant_ratings_dict(input_file)

    ratings_dictionary = add_new_restaurant(ratings_dictionary)

    sort_and_print_restaurants(ratings_dictionary)


rating_restaurants(sys.argv[1])
