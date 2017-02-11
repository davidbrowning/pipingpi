#!/usr/bin/python

#########################################
## CS 3430: S2017: HW02: Fixed Points
## Author: Vladimir Kulyukin
## Modified by David Browning
#########################################

from __future__  import  division
import math

def close_enough(x, y, error = 0.0000001):
    return abs(x - y) < error

def search_for_midpoint(f, neg_point, pos_point):
    midpoint = (neg_point + pos_point)/2
    if close_enough(neg_point, pos_point):
        return midpoint
    else:
        if(f(midpoint) < 0):
            return search_for_midpoint(f,midpoint,pos_point)
        elif(f(midpoint) > 0):
            return search_for_midpoint(f, neg_point, midpoint)


def half_interval_method(f, a, b):
    a_val = f(a)
    b_val = f(b)
    if a_val < 0 and b_val > 0:
        return search_for_midpoint(f, a, b)
    elif b_val < 0 and a_val > 0:
        return search_for_midpoint(f, b, a)
    else:
        raise Exception('Values are not of oppositive sign')

def fixed_point(f, guess, error=0.0000000000001):
    prev_guess = guess
    curr_guess = f(prev_guess)
    num_iters = 0
    while not close_enough(prev_guess, curr_guess, error=error):
        prev_guess = curr_guess
        curr_guess = f(curr_guess)
        num_iters += 1
    return (num_iters, curr_guess)

def fixed_point_sqrt(x):
    return fixed_point(lambda y: (y + x/y)/2, 1.0)

def fixed_point_golden_ratio():
    return fixed_point(lambda x: 1 + 1/x, 1.0)

def fixed_point_golden_ratio_with_avrg_damping():
    return fixed_point(lambda x: (x + 1 + 1/x)/2, 1.0)
    pass

def fixed_point_log(y, guess):
    return fixed_point(lambda x: y**(1/x), guess)
    pass

def fixed_point_log_with_avrg_damping(y, guess):
    return fixed_point(lambda x: (x + y**(1/x))/2 , guess)
    pass

def getKey(myList):
    return myList[1][1][0]

def fixed_point_logs_with_avrg_damping(x, y, guess):
    i = 0;
    toReturn = []
    for i in xrange(1, int(math.floor (y/x)+1)):
        toReturn.append([((i)*x), fixed_point_log_with_avrg_damping(((i)*x), guess)]);
    from operator import itemgetter
    return(sorted(toReturn, key=getKey));
    pass



##F1: Returned none type
##F2: 27.32050928255947
##F3: -1.4908409440295145e-07
##F4: -3.638441885556176e-07

##I'm fairly certain I haven't implimented that last function correctly, it was a touch confusing. 
