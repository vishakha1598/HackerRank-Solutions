#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    current_position = 0
    number_of_jumps = 0
    last_cloud_postion = len(c)-1
    last_second_postion = len(c)-2
    
    while current_position<last_second_postion:
        #Checking if the cloud next to the next cloud is thunderstorm
        if c[current_position+2] == 0:
            current_position += 2
        else:
            current_position += 1
        number_of_jumps += 1
    #Checking if we are in the last cloud or the last second cloud
    if current_position != last_cloud_postion:
        number_of_jumps += 1
        
    return number_of_jumps

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
