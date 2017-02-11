#!/usr/bin/python

#########################################
## CS 3430: S2017: HW01: Euclid Numbers
## David Browning
## A01256705
#########################################

import math
import sys

def is_prime(n):
    '''is_prime(n) ---> True if n is prime; False otherwise. '''
    #if n == 25
    if(n <= 1): #pass
        ##('false');
        return False;
    elif(n <= 3): #pass
        ##('true');
        return True;
    elif(n % 2 == 0 or n % 3 == 0): #pass
        ##('false');
        return False;
    i = 5;
    while(i * i <= n): # 5 * 5 = 25 <= 25
        if (n%i == 0 or n % (i+2) == 0):
            ##('false');
            return False;
        i = i + 6;
    ##('true');
    return True;
    pass 

## is_prime() was Modeled after the pseudo code found on wikipedia.
## https://en.wikipedia.org/wiki/Primality_test#Pseudocode

def next_prime_after(p):
    '''computes next prime after prime p; if p is not prime, returns None.'''
    if not is_prime(p): return None
    ## your code here
    p += 1;
    while (not is_prime(p)):
        p += 1;
    return p;
    pass

def euclid_number(i):
    '''euclid_number(i) --> i-th Euclid number.'''
    if i < 0: return None
    ## your code here
    prime = 2;
    eu_num = 2;
    for num in xrange(i):
        prime = next_prime_after(prime);
        eu_num = eu_num*prime; 
    
    eu_num = eu_num + 1;
    return eu_num;
    pass

def compute_first_n_eucs(n):
    '''returns a list of the first n euclid numbers.'''
    eucs = []
    ## your code here? if the above functions
    ## are implimented correctly, it already
    ## works. 
    for eu_num in xrange(n):
        eucs.append(euclid_number(eu_num));

    return eucs



import itertools
def prime_factor(n, factor_list):
    #print '.'
    if(is_prime(n)):
        factor_list.append(n);
        return n;
    else:
        for num in itertools.count(2,n):
            if (n % num == 0):
                #print '.'
                sys.stdout.flush()
                return (prime_factor(n/num, factor_list)
                    and prime_factor(num, factor_list));

def prime_factors_of(n):
    '''returns a list of prime factors of n if n > 1 and [] otherwise.'''
    if n < 2: return []
    factors = []
    prime_factor(n, factors);3
    return factors

def tabulate_euc_factors(n):
    '''returns a list of 3-tuples (i, euc, factors).'''
    euc_factors = []
    for i in xrange(n+1):
        tup = (i, euclid_number(i), prime_factors_of(euclid_number(i)));
        euc_factors.append(tup);                 
    return euc_factors

##Extra Credit point: trick question, euclid_number(10) is prime!
## so the prime_factors_of(euclid_number(10)) is [200560490131]





                     

    

