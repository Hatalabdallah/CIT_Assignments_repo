# Country Cities Guessing Game Python Project Create a program that will ask a user to guess 
# the capital of a country. The program should have a list of at least 10 countries and their 
# capitals. The program should randomly choose a country and ask the user to guess the capital. 
# The program should tell the user if they are correct or not. The program should also keep track
#  of how many questions the user gets correct and print that out at the end. Use this link to programatically get 
#  the list of countries and their capitals: https://raw.githubusercontent.com/samayo/country-json/
#  master/src/country-by-capital-city.json

import random
import time

print('\n\nCOUNTRY CITIES GUESSING GAME!\n\n')
time.sleep(2)
country_dlist = [    {
        "country": "Zambia",
        "city": "Lusaka"
    },
    {
        "country": "Zimbabwe",
        "city": "Harare"
    },    {
        "country": "Virgin Islands, British",
        "city": "Road Town"
    },
    {
        "country": "Virgin Islands, U.S.",
        "city": "Charlotte Amalie"
    },
    {
        "country": "Wales",
        "city": "Cardiff"
    },    {
        "country": "United Arab Emirates",
        "city": "Abu Dhabi"
    },
    {
        "country": "United Kingdom",
        "city": "London"
    },
    {
        "country": "United States",
        "city": "Washington"
    },    {
        "country": "Uganda",
        "city": "Kampala"
    },
    {
        "country": "Ukraine",
        "city": "Kyiv"
    }
    ]

def run():
    tot_points = 0
    num_of_ques = len(country_dlist)

    for i in range(num_of_ques):
        choice = random.choice(country_dlist)
        que = country_dlist.remove(choice)
        capital = input("Please enter the city for country {}: ".format(choice['country']))

        if capital.lower() == choice['city'].lower(): # case insensitive match :)
            tot_points += 1
            print('Correct, the capital city of {} is {}.\n\n' .format(choice["country"],choice["city"]))
            
        else:
            print('Wrong, the capital city of {} is {}.\n\n' .format(choice["country"],choice["city"]))
           
    return tot_points

points = run()


print("You scored {} points".format(points))