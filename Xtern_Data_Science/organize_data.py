import geopandas
import googlemaps
import pandas as pd
import geopandas as gpd
import ast
import json
import matplotlib.pyplot as plt
from pandas import read_excel
from restaurants_nearby import *


def add_latitude_longitude(restaurants_df):
    # print (restaurants_df)
    for index, row in restaurants_df.iterrows():
        dict1 = (row['geometry'])
        restaurants_df.at[index, 'Latitude'] = dict1['location']['lat']
        restaurants_df.at[index, 'Longitude'] = dict1['location']['lng']
    return restaurants_df


def cleanup(df):
    # print(df.columns)
    cleaned_up_df = df[['name', 'price_level', 'rating', 'types', 'user_ratings_total', 'vicinity', 'Latitude',
                        'Longitude']].copy()

    return cleaned_up_df


def write_on_file(df, filename):
    df.to_csv(filename)


def add_Bayesian_average(df):
    '''
    :param df:
    :return: df with Bayesian average column
    '''
    average_rating_for_all = df['rating'].mean()
    # print (average_rating_for_all)
    confidence_level = df['user_ratings_total'].quantile(0.25)
    # print (confidence_level)
    df['bayes_avg'] = ""
    for index, row in df.iterrows():
        review_count = row['user_ratings_total']
        rating = row['rating']
        df.at[index, 'bayes_avg'] = (review_count * rating + confidence_level * average_rating_for_all)/(review_count + confidence_level)
    return df


if __name__ == '__main__':
    # launch_indy = (39.75953002769105, -86.15810034649725)
    # launch_indy_df = get_data(launch_indy, 5)
    # launch_indy_with_lat_long = add_latitude_longitude(launch_indy_df)
    # clean_launch_indy_df = cleanup(launch_indy_with_lat_long)
    # bayes_avg_launch_indy = add_Bayesian_average(clean_launch_indy_df)
    # write_on_file(bayes_avg_launch_indy, 'restaurants_near_launch_indy_geometry.xlsx')

    industrious_mass = (39.77261112368934, -86.15306934465066)
    industrious_mass_df = get_data(industrious_mass, 5)
    industrious_mass_with_lat_long = add_latitude_longitude(industrious_mass_df)
    clean_industrious_mass = cleanup(industrious_mass_with_lat_long)
    bayes_avg_industrious_mass = add_Bayesian_average(clean_industrious_mass)
    write_on_file(bayes_avg_industrious_mass, 'restaurants_near_industrious_mass.csv')

    # create_map(industrious_mass, bayes_avg_industrious_mass)


