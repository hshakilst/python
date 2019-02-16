#!/usr/bin/python
from random import randint
import random
import string

def random_with_N_hex(n):
    return ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(n))

def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

def id_gen_hex(pattern, num_of_ids):      #pattern xxxx-xxx-xx, num = no. of ids to be generated
    file = open('uuid.txt', 'wb')
    pat = pattern.split('-')
    i = 0
    while(i < num_of_ids):
        id = ''
        for p in pat:
            rnd = random_with_N_hex(len(p))
            id = id + str(rnd) + '-'
        id = id[:-1]
        i+=1
        print str(i) + ': ' + id
        file.writelines(id + '\n')
    file.close()

def id_gen_int(pattern, num_of_ids):      #pattern xxxx-xxx-xx, num = no. of ids to be generated
    file = open('id.txt', 'wb')
    pat = pattern.split('-')
    i = 0
    while(i < num_of_ids):
        id = ''
        for p in pat:
            rnd = random_with_N_digits(len(p))
            id = id + str(rnd) + '-'
        id = id[:-1]
        i+=1
        print str(i) + ': ' + id
        file.writelines(id + '\n')
    file.close()

def main():
    id_gen_hex("xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx", 65)

main()
    

