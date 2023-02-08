# Homework 3: "The World Has Turned and Left Me Turbid" 
### Scenario: Your robot has finished collecting its five meteorite samples and has taken them back to the Mars lab for analysis. In order to analyze the samples, however, you need clean water. You must check the latest water quality data to assess whether it is safe to analyze samples, or if the Mars lab should go on a boil water notice.

#### Objective: Gain familiarity with requests module, getting data from the web, and unit testing.

### Data:
The data for this homework set is a json file that contains information on water quality and various other pieces of information. The data can be viewed here: [Turbidity Data](https://raw.githubusercontent.com/wjallen/turbidity/main/turbidity_data.json).
A sample of the data looks like:

```
{
  "turbidity_data": [
    {
      "datetime": "2023-02-01 00:00",
      "sample_volume": 1.19,
      "calibration_constant": 1.022,
      "detector_current": 1.137,
      "analyzed_by": "C. Milligan"
    },
    {
      "datetime": "2023-02-01 01:00",
      "sample_volume": 1.15,
      "calibration_constant": 0.975,
      "detector_current": 1.141,
      "analyzed_by": "C. Milligan"
    },
    ... etc
```


### Scripts:

`analyze_water.py`:
Pulls data from a water quality data set, [Turbidity Data](https://raw.githubusercontent.com/wjallen/turbidity/main/turbidity_data.json), from the internet and creates a python dictionary of the data. It then preforms various functions to analyze the quality of the water, check the safety of the water based on a safety threshold, and calculate how long until the water is safe to use if the water is unsafe.


`test_analyze_water.py`:
Applys common pytest unit tests to each function in `analyze_water.py` to confirm the functions are acting as expected. 


### Instructions:
Download all files in homework03 folder and proceed.

#### Step 1: Analyze water quality. 
Run `analyze_water.py` with the following command:
``` 
$ python3 analyze_water.py 
```
This will execute the file, reading in the water quality data set and printing 3 key pieces of information to screen: (1) the current water turbidity (taken as the average of the most recent five data points), (2) whether that turbidity is below a safe threshold, and (3) the minimum time required for turbidity to fall below the safe threshold (if it is already below the safe threshold, the script would report “0 hours” or similar).

An example of this output is as follows:
```
$ python3 analyze_water.py 
The current water turbidity is 1.1212 NTU
Warning: Turbidity is above threshold for safe use
Minimum time required to return below a safe threshold = 5.66 hours

```

#### Step 2: Test the functions are working correctly

Run pytest on the script with the following command:

``` 
$ pytest test_analyze_water.py
```
*** Note: you can also simply run the following to execute all test files beingin with "test_[].py"
``` 
$ pytest 
```

This will produce an output similar to the following:
  
 ```
$ pytest test_analyze_water.py 
================================================================================ test session starts ================================================================================
platform linux -- Python 3.8.10, pytest-7.2.1, pluggy-1.0.0
rootdir: /home/jacksont/coe-332/my-coe332-hws/homework03
collected 3 items                                                                                                                                                                   

test_analyze_water.py ...                                                                                                                                                     [100%]

================================================================================= 3 passed in 0.07s =================================================================================
