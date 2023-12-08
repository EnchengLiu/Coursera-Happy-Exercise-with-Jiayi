import math
# Some Python Exercises Sample here



import math
import numpy as np
from scipy import stats

# Each day, to enter their building, employees ofan e-commerce company have to type a stringof numbers into a console using a 3 x 3numeric keypad. Every day, the numbers onthe keypad are mixed up.
# Use the following rules to calculate the totalamount of time it takes to type a string:
# It takes 0 seconds to move their finger to thefirst key, and it takes 0 seconds to press thekey where their finger is located any number oftimes.
# They can move their finger from one locationto any adjacent key in one second. Adjacentkeys include those on a diagonal.
# Moving to a nonadjacent key is done as aseries of moves to adjacent keys.


#求sum内有多少2的倍数
def isPowerofTwo(n):
    if n <= 0:
        return []
    else:
        return len([2 ** pos for (pos, value) in enumerate(list(bin(n)[-1:1:-1])) if value != '0'])


def PathTime(number1,target):
    if number1==target:
        return 0
    if number1==1:
        if target==2 or target==4 or target==5: return 1;
        else: return 2
    if number1==2:
        if target==7 or target==8 or target==9: return 2;
        else: return 1
    if number1==3:
        if target==2 or target==5 or target==6: return 1;
        else: return 2
    if number1==4:
        if target==3 or target==6 or target==9: return 2;
        else: return 1
    if number1==5:
        return 1
    if number1==6:
        if target==1 or target==4 or target==7: return 2;
        else: return 1
    if number1==7:
        if target==4 or target==5 or target==8: return 1;
        else: return 2
    if number1==8:
        if target==1 or target==2 or target==3: return 2;
        else: return 1
    if number1==9:
        if target==5 or target==6 or target==8: return 1;
        else: return 2

def entryTime(s,keypad):
    NewS =list(map(int,s ))
    NewKeyboard=list(map(int,keypad ))
    #print(NewKeyboard,type(NewKeyboard[0]))

    Map=list(range(1,10))
    Dict=dict(zip(NewKeyboard,Map))
    print(Dict)
    sum=0
    time=0
    current=NewS[0]
    for i in NewS:
        sum+=PathTime(Dict[current],Dict[i])
        print("Time is",time)
        time+=1
        print(i,Dict[current],Dict[i])
        print("Cost",PathTime(Dict[current],Dict[i]))
        print("sum",sum)
        print(" ")
        current=i
    print(sum)

s="423692"
keypad="923857614"
print(PathTime(5,6))
entryTime(s,keypad)
