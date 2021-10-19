import googlemaps
import pandas as pd
import time


def miles_to_meter(miles):
    try:
        return miles * 1609.34

    except:
        return 0


def get_data(location, radius):
    '''
    :param location:
    :param radius (in miles):
    :param filename:
    :return: a dataframe containing restaurants in 5 miles radius
    '''
    API_KEY = open('API_key_google.txt', 'r').read()
    map_client = googlemaps.Client(API_KEY)
    # print (dir(map_client))
    # location = (39.77398068446764, -86.18492243115612)
    distance = miles_to_meter(radius)
    keyword = 'Restaurants'

    restaurant_list = []

    response = map_client.places_nearby(
        location=location,
        keyword=keyword,
        radius=distance
    )
    restaurant_list.extend(response.get('results'))
    next_page_token = response.get('next_page_token')

    while next_page_token:
        time.sleep(2)
        response = map_client.places_nearby(
            location=location,
            keyword=keyword,
            radius=distance,
            page_token=next_page_token
        )
        restaurant_list.extend(response.get('results'))
        next_page_token = response.get('next_page_token')

    df = pd.DataFrame(restaurant_list)
    return df


# get_data((39.75953002769105, -86.15810034649725), 5, "restaurants_near_launch_indy.xlsx")
# get_data((39.77261112368934, -86.15306934465066), 5, "restaurants_near_industrius_mass.xlsx")




