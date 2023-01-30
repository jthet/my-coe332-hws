#!/usr/bin/env python3

import json
import random

def random_lats(how_many: int) -> float:
    """
    This function generates random latitudes (between 16-18 for this script).

    Args:
        how_many (int): an integer value of how many longitudes you would like 

    Returns:
        latitudes (list): list of latitudes.
    """

    latitudes = []
    for i in range(how_many):
        latitudes.append(random.random()*2+16)

    return latitudes

def random_longs(how_many: int) -> float:
    '''
    Similar to random_lats method
    '''
    longitudes = []
    for i in range(how_many):
        longitudes.append(random.random()*2+82)
    return longitudes

def random_comps(how_many: int ) -> float:
    '''
    just takes one input "how_many" and returns a list of that many compositions, randomly chosen from:
    "stony","iron","stony-iron"
    '''
    list_of_comps = ["stony","iron","stony-iron"]
    rand_comp_list = []
    for i in range(how_many):
        rand_comp_list.append(list_of_comps[random.randint(0,2)])
    return rand_comp_list


def list_of_dicts_gen(how_many_sites: int) -> list:

    """
    This function creates a list of dictionaries containing the following structure:
        dictionary = {
            "site_id": site_ids[i],
            "latitude": latitudes[i],
            "longitude": longitudes[i],
            "composition": composition[i]
            }
    Each dictionary is representative of one meteorite landing site. 

    Args:
        how_many_sites (int): how many dictionaries in the list you would like

    Returns:
        list_of_dicts (list): list containing the n number of dictionaries
    """
    site_ids = list(range(1, how_many_sites+1))
    latitudes = random_lats(how_many_sites)
    longitudes = random_longs(how_many_sites)
    list_of_comps = ["stony","iron","stony-iron"]
    composition = random_comps(how_many_sites)
    list_of_dicts = []

    for i in range(how_many_sites):
        dicts_in_list = {
            "site_id": site_ids[i],
            "latitude": latitudes[i],
            "longitude": longitudes[i],
            "composition": composition[i]
        }
        list_of_dicts.append(dicts_in_list)


    return list_of_dicts



def main():
    how_many = 5
    list_of_dicts = list_of_dicts_gen(how_many)
    big_dict = {
        "sites": list_of_dicts
    }
    with open('meteorLanding_sites.json', 'w') as out:
        json.dump(big_dict, out, indent=2)


if __name__ == '__main__':
    main()
