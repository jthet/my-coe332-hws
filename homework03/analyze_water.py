#!/usr/bin/env python3

import requests
import math


def turb_Calc(turbDict: dict) -> float:
    """
    This function calculates the turbidity of the water, using the equation T = a0 * I90, for the 5 most recent water recordings
    
    Args:
        turbDict (dict): The first argument is a dictionary holding the information on the water sample, specifically:

                a0 = the calibration constant
                I90 = the detector current 
        
    Returns:
        (float): The function returns the average turbidity of the 5 most recent water samples.
    """
    
    dictSize = len(turbDict["turbidity_data"])
    turb_sum = 0.00

    for i in range(5): 
        turbDict['turbidity_data'][dictSize-i-1]['calibration_constant']
        calConst = turbDict['turbidity_data'][dictSize-i-1]['calibration_constant']
        detectCurrent = turbDict['turbidity_data'][dictSize-i-1]['detector_current']
        turb = calConst * abs(detectCurrent) # Turbidity can never be negative but current can
        turb_sum = turb + turb_sum

    return (turb_sum / 5)


def turb_threshold(turb_curr: float, safe_thresh: float) -> bool:

    """
    This function finds if the water is safe to use or not by comparing the current turbidity and safe turbidity levels.
    
    Args:
        turb_curr (float): The first argument is the current turbidity.
        safe_thres (str): The second argument is the turbidity threshold for safe water use.

    Returns:
        (bool): The function returns the if the water is safe to use or not.
    """
   
    if turb_curr < safe_thresh:
        print ('Turbidity is below threshold for safe use')
    else:
        print('Warning: Turbidity is above threshold for safe use')

    return turb_curr < safe_thresh


def time_til_safe(turb_curr: float, safe_thresh: float, decay_fact: float) -> float:
    """
    This function calculates the the minimum time required until the turbidity falls below the threshold using the inequality Ts > T0(1 - d)^b.
    
    Args:
        turb_curr (float): The first argument is a the current turbidity.
        safe_thresh (float): The second argument is the threshold for what is considered a safe turbidity.
        decay_fact (float): The third argument is a the decay factor associated with how the turbidity decreases over time.
        
    Returns:
        b (float): The function returns the time until the turbidity falls below the threshold. 
    """
    
    if turb_curr <= 1:
        b = 0
    else:
        b = math.log(safe_thresh/turb_curr, 1 - decay_fact)
    return b




def main():

    # Pulling data from json set and creating dict
    response = requests.get(url='https://raw.githubusercontent.com/wjallen/turbidity/main/turbidity_data.json')
    turbidityDict = response.json()

    # Finding current turbidity
    turb_curr = turb_Calc(turbidityDict)
    print(f'The current water turbidity is {turb_curr:.6} NTU')

    # variable  for safety check and time til safe calculation
    decay_fact = 0.02
    safe_thresh = 1.0
    
    # Checking safety
    turb_threshold(turb_curr, safe_thresh)

    # Finding time til safe
    safety_time = time_til_safe(turb_curr, safe_thresh, decay_fact)
    print(f'Minimum time required to return below a safe threshold = {safety_time:.3} hours')



if __name__ == '__main__':
    main()
