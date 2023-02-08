#!/usr/bin/env python3

import analyze_water
import pytest
from analyze_water import turb_Calc, turb_threshold, time_til_safe
import sys, os # kinda pointless but using to mute print output from safety check

def test_turb_calc():
    data = {"turbidity_data": [
    {"detector_current": 1,  "calibration_constant": 1},
    {"detector_current": 1,  "calibration_constant": 1}, 
    {"detector_current": 1,  "calibration_constant": 1}, 
    {"detector_current": 1,  "calibration_constant": 1}, 
    {"detector_current": 1,  "calibration_constant": 1} ]}

    assert turb_Calc(data) == 1 
    assert isinstance(turb_Calc(data), float) == True

    with pytest.raises(KeyError):
        turb_Calc({"fake Key": [0]})

def test_turb_threshold():
    assert turb_threshold(5, 1) == False
    assert turb_threshold(0, 1) == True
    assert isinstance(turb_threshold(0, 1), bool) == True


def test_time_til_safe():

    a1 = 1
    a2 = 3
    a3 = 0
    a4 = 0.999999
    a5 = -50

    b = 1
    c = 0.02

    assert isinstance(time_til_safe(a2, b, c), float)

    assert(time_til_safe(a1, b, c) == 0)
    assert(time_til_safe(a2, b, c) > 0)
    assert(time_til_safe(a3, b, c) == 0)
    assert(time_til_safe(a4, b, c) == 0)
    assert(time_til_safe(a5, b, c) == 0)


def blockPrint():
    sys.stdout = open(os.devnull, 'w')
    # blocks test_turb_threshold from printing 

def main():
    blockPrint() # muting output
    test_turb_calc()
    test_turb_threshold()
    test_time_til_safe()


if __name__ == '__main__':
    main()
