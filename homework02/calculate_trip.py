#!/usr/bin/env python3

import json
import math


def calc_gcd(latitude_1: float, longitude_1: float, latitude_2: float, longitude_2: float) -> float:
    """
    Given two locations on mars (each with a latitude and longitude), this function will find the distance between the two using the 
    great circle distance algorithm. 

    Args:
        latitude_1 (float): The starting latitude.
        longitude_1 (float): The starting longitude.
        latitude_2 (float): The ending latitude.
        longitude_2 (float): The ending latitude.

    Returns:
        result (float): the distance between the two points taking into account mars spherical nature.
    """

    mars_radius = 3389.5
    lat1, lon1, lat2, lon2 = map( math.radians, [latitude_1, longitude_1, latitude_2, longitude_2] )
    d_sigma = math.acos( math.sin(lat1) * math.sin(lat2) + math.cos(lat1) * math.cos(lat2) * math.cos(abs(lon1-lon2)))
    return ( mars_radius * d_sigma )

def simulate_full_walk(sites: dict, total_legs: int) -> None:
    """
    Simulates a full walk between every meteor site in a input dictionary "sites". 
    Also has an input for how many legs you want to walk if you don't want to visit every site.

    Returns nothing, however prints out output from the walk between sites.
    """
    
    total_dist = 0.0
    bot_speed = 10
    total_time = 0

    for i in range(total_legs):
        if (i==0):  
            leg_distance = calc_gcd(16, 82, sites['sites'][i]['latitude'], sites['sites'][i]['longitude'])
        else:
            leg_distance = calc_gcd(sites['sites'][i-1]['latitude'], sites['sites'][i-1]['longitude'], sites['sites'][i]['latitude'], sites['sites'][i]['longitude'])
       

        leg_sample_time = sample_time(sites, i)
        travel_time = leg_distance / bot_speed
       
        total_dist += leg_distance
        total_time += (travel_time + leg_sample_time)

        print(f'leg = {i+1}, time to travel = {travel_time:.2f} hours, time to sample {leg_sample_time} hours')
    print(f'number of legs = {total_legs}, total time elapsed = {total_time:.2f} hours, total distance = {total_dist:.3f} km')


def sample_time(sites:dict, i: int) -> float:
    '''
    takes a dictionary containing meteorite sites and an index for a site.
    To answer the following:
    "When the robot stops to take a sample of each meteorite, the amount of time it stops depends on the composition of the meteorite.
    Stony meteorites take 1 hour to sample, iron meteorites take 2 hours to sample, and stony-iron meteorites take 3 hours to sample."
    '''
    # i = index for the currentLeg 
    if (sites['sites'][i]['composition'] == 'stony'):
        sample_time = 1
    elif(sites['sites'][i]['composition'] == 'iron'):
        sample_time = 2
    elif(sites['sites'][i]['composition'] == 'stony-iron'):
        sample_time = 3
        

    return sample_time





def main():
    with open('meteorLanding_sites.json', 'r') as data:
        sites = json.load(data)

    subDicts_count = len(sites['sites'])

    simulate_full_walk(sites, subDicts_count)


if __name__ == '__main__':
    main()
