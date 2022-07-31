'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

# print("Hello World")
# b_num = list(input("Input a binary number: "))
# value = 0

# for i in range(len(b_num)):
# 	digit = b_num.pop()
# 	if digit == '1':
# 		value = value + pow(2, i)
# print("The decimal value of the number is", value)


import math
import os
import random
import re
import sys


#
# Complete the 'binary_converter' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER_ARRAY binary
#  2. CHARACTER base
#

def getOctal(binArray):
    i = 0
    ocatalArray = [0] * 32
    pos = 0
    count = 1
    ocatalDigit = 0
    lengthOfBinList = len(str(binArray))
    while int(binArray)!=0:
        digit = binArray % 10
        ocatalDigit += digit * pow(2,i)
        binArray = int (binArray / 10)
        i += 1
        
        ocatalArray[pos] = ocatalDigit
        
        if count % 3 == 0 or lengthOfBinList == count:
            ocatalDigit = 0
            i = 0
            pos += 1
        
        count += 1
    newArray = ocatalArray[:pos]
    newArray.reverse()
    return newArray

# 16 - 8 4 2 1
# 0-9 A B C D E F
def getHexa(binArray):
    i = 0
    hexArray = [0] * 32
    pos = 0
    count = 1
    hexDigit = 0
    lengthOfBinList = len(str(binArray))
    
    hexaObj = { 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F' }
    
    while int(binArray) != 0:
        digit = binArray % 10
        hexDigit += digit * pow(2,i)
        binArray = int (binArray / 10)
        i += 1
        
        hexArray[pos] = hexDigit

        if count%4 == 0 or lengthOfBinList == count:
            if hexDigit > 9:
                hexArray[pos] = hexaObj[hexDigit]
            i = 0
            hexDigit = 0
            pos +=1
        
        count +=1
    newArray = hexArray[:pos]
    newArray.reverse()
    return newArray 
        

def binary_converter(binary,base = 'd'):
    print(binary, base)
    value = 0
    if base == 'b':
        return "".join(map(str, binary)).lstrip('0')
    elif base == 'o':
        octalArray = getOctal(int("".join(map(str, binary)).lstrip('0')))
        return "".join(map(str, octalArray))
    elif base == 'h':
        hexArray = getHexa(int("".join(map(str, binary)).lstrip('0')))
        return "".join(map(str, hexArray))
    else:
        for i in range(len(binary)):
        	digit = binary.pop()
        	if digit == 1:
        		value = value + pow(2, i)
    print(value)
    return value
    
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

binary = [1,1,1,1,1,1,0,1]

try:
    base = 'h'
    result = binary_converter(binary, base)
except:
    result = binary_converter(binary)
print("value", result)
    # fptr.write(result + '\n')

    # fptr.close()