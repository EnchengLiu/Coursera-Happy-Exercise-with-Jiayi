import math
# Some Python Exercises Sample here



# 第一题
#A compliance system monitors incoming andoutbound calls. It sends an alert whenever theaverage number of calls over a trailing numberof minutes exceeds a threshold. If the numberof trailing minutes to consider,
#precedingMinutes = 5, at time T take theaverage the call volumes for times T-(5-1) 7-(52) ...T-(5-5)
def numberOfAlert(n, numCalls, alertThreshold, precedingMinutes):
    result = 0
    for i in range(n):
        print("i", i)
        if i < precedingMinutes - 1:
            continue
        sum = 0

        for j in range(precedingMinutes):
            sum += numCalls[i - j]
        print("sum", sum)
        if sum / precedingMinutes > alertThreshold:
            result += 1
    return result


# 第二题
#A palindrome is a string that reads the samefrom the left and from the right. For examplemom and tacocat are palindromes, as are anysingle-character strings. Given a string.determine the number of its substrings that arepalindromes.
def isPalindrome(s):
    return s == s[::-1]


def countPalindrames(s):
    result = 0
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            if isPalindrome(s[i:j]):
                result += 1
    return result



# 第三题
# Starting with an empty set of integers namede/ements, perform the following query operations:
# The command push x inserts the value of xintoelements.
# The command pop x removes the value of xfromelements.
# The integers in e/ements need to be ordered in sucha way that after each operation is performed, theproduct of the maximum and minimum values in theset can be easily calculated
def Maxmin(operations, x):
    result = []
    for i in range(len(operations)):
        if operations[i] == 1:
            x.append(x[i])
        elif operations[i] == 2:
            x.pop()
        else:
            result.append(max(x))
    return result



# 第四题
#A subarray of array a is defined as a contiguousblock of a's elements having a length that is less thanor equal to the length of the array, For example, thesubarrays of array a = 1, 2, 3/are [11 21 31 [1, 2[2, 3l and [1 2 3 Given an integer, k = 3 thesubarrays having elements that sum to a number s kare (11 [2l and [1, 2] The longest of these subarraysis [1, 2] which has a length of 2. Given an array, a,determine its longest subarray that sums to lessthan or equal to a given value k

def maxLength(a, k):
    result = 0
    subarray = [[]]
    for i in a:
        subarray.extend([j + [i] for j in subarray])
    for i in subarray:
        if sum(i) <= k:
            result = max(result, len(i))
    return result





# 第五题
#Problem5
# Consider a string, S, that is a series of characters, each followed by its frequencyas an integer. The string is not compresseocorrectly, so there may be multipleoccurrences of the same character. A
# properly compressed string will consist ofone instance of each character in alphabetical order followed by the totacount of that character within the string


def betterCompression(s):
    result = ""
    data={}

    for i in range(len(s)):
        print("i",i)
        if s[i].isalpha():
            if s[i] not in data:
                data[s[i]]=0
            print(data)


            j=i+1
            print("j",j)
            print("s[j]",s[j])
            num=""
            while(j<len(s) and s[j].isdigit()):
                num+=s[j]
                print("herenum",num)
                j+=1
            print("num",num)
            print("data[s[i]]",data[s[i]])
            data[s[i]]+=int(num)

    data=dict(sorted(data.items(),key=lambda x:x[0]))
    print(data)
    for i in data:
        result+=i+str(data[i])
    return result

print(betterCompression("a3c9b2c1"))



#Problem6
# The owner of a construction company has asurplus of rods of arbitrary lengths. A localcontractor offers to buy any of the surplus.as long as all the rods have the same exactinteger length, referred to as salelength.The number of sellable rods can beincreased by cutting each rod zero or moretimes, but each cut has a cost denoted bycostPerCut After all cuts have been made.any leftover rods having a length other thansalelength must be discarded for no profitThe owner's total profit for the sale is
# calculated as:
# totalProfit = totalUniformRoas x salelengthx salePrice - totalCuts x costPerCut
# where totalUniformRogs is the number ofsellable rods, salePrice is the per unit lengthprice that the contractor agrees to pay, anototalCuts is the total number of times therods needed to be cut.

def maxProfit(costPerCut, salePrice, lengths):
    result = 0
    for i in range(1, min(lengths) + 1):
        print("i", i)
        profit = 0
        for j in lengths:
            if j % i == 0:
                revenue = j // i * salePrice * i
                cost = costPerCut * (j // i - 1)
                if (revenue - cost < 0):
                    continue
                profit += j // i * salePrice * i - costPerCut * (j // i - 1)
            else:
                revenue = j // i * salePrice * i
                cost = costPerCut * (j // i)
                profit += j // i * salePrice * i - costPerCut * (j // i)

        print("profit", profit)
        result = max(result, profit)
    return result


print(maxProfit(25, 1, [20, 40, ]))

n = 8
numcalls = [2, 2, 2, 2, 5, 5, 5, 8]
alertThreshold = 4
precedingMinutes = 3
