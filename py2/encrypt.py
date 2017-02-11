#!/usr/bin/python

from random import randint
##from eucs import *
from fixed_points import half_interval_method as him
import math
import euclid_numbers

# found on stackoverflow by stefan edited by will ness
# I tried to use the algorithm I had written for euclid_numbers.py,
# but it got stuck in a loop somehow


def prime_factors(n):
    i = 2
    factors = []
    while i*i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

public_key = public_key = 61488978258849141
factor_list = []
factor_list = prime_factors(public_key)
factor_list_set = set(factor_list)
factor_list = list(factor_list_set)
public_key_factors = factor_list ## you will have to compute these
num_public_key_factors = int(len(factor_list_set))
# use euclid_numbers.prime_factor(n, factor_list)

code_separator = euclid_numbers.euclid_number(33)

def choose_random_factor_index(num_public_key_factors):
    return randint(0, num_public_key_factors-1)




def is_even(num):
    if(num % 2 == 0):
        return True;
    else:
        return False;


def pascal_tri_row(n):
    k = 0;
    li = []
    while (k < n):
#        #print '%d is less than %d' %(k, n)
        li.append((math.factorial(n))/(math.factorial(k)*(math.factorial(n - k))))
        k += 1;

    if(is_even(n)):
        li.append((math.factorial(n))/(math.factorial(k)*(math.factorial(n - k))))
        k = k-1;
    else:
        while (k >= n):
            li.append((math.factorial(n))/(math.factorial(k)*(math.factorial(n - k))))
            k += -1;

    return li
    pass

def pascal_tri_row_sum(n):
    answer = 2
    if(euclid_numbers.is_prime(n)):
        k = pascal_tri_row(n)
        for item in k:
            if(item != 1):
                answer += (item/n)
    else:
        answer = -1
    return answer



def encrypt_char(c):
    pi = choose_random_factor_index(num_public_key_factors)
    #print "pi: %d" % pi
    p = public_key_factors[pi]
    s = pascal_tri_row_sum(p)
    z = math.floor(him(lambda x: (x**9 - s + x)/2, 0, 1000))
    rand_factor = str(pi)
    #print(pi)
    pub_key_fac = str(public_key_factors[pi])
    tri_sum = str(s)
    algo_hash = str(int(z + ord(c)))
    #print(algo_hash)
    code_s = str(code_separator)
    full_string = rand_factor + code_s + algo_hash + code_s
    return full_string
    pass

def encrypt_text(txt):
    enc = ''
    for c in txt: enc += encrypt_char(c)
    return enc



def decrypt_text(txt):
    separator_string = str(code_separator)
    separator_length = len(separator_string)
    #print separator_string
    text_length = len(txt)
    ## TODO use regex to find separator, then replace with commas.
    ### Parsing should then be a breeze
    num_list = txt.split(separator_string);
    del num_list[-1]
    #print num_list
    #print num_list
    message = ''
    for item in xrange(len(num_list)/2):

        pi = int(num_list[2*item])
        un_ord = int(num_list[2*item+1])
#        #print "pi -- decrypt: %d" % pi
        p = public_key_factors[pi]
        s = pascal_tri_row_sum(p)
        z = math.floor(him(lambda x: (x**9 - s + x)/2, 0, 1000))
        un_ord = un_ord - z
        message += (chr(int(un_ord)))
    return message
    pass



