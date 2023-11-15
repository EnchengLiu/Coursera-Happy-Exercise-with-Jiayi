# 1. Suspicious Activity From Logs
# # Application logs are useful in analyzinginteraction with an application andmay also be used to detect suspiciousactivities.
# A log file is provided as a string arraywhere each entry represents a moneytransfer in the form "sender user idrecipient user id amount. Each of thevalues is separated by a space.
# sender user id andrecipient user id both consist only ofdigits, are at most 9 digits long andstart with non-zero digit
# amount consists only of digits, is atmost 9 digits long and starts withnon-zero digit
# Logs are given in no particular order.Write a function that returns an arrayof strings denoting user id's of
# suspicious users who were involved inat least threshold' number of logentries, The id's should be orderedascending by numeric value.
# Example
# logs = ["88 99 200"88 99 300" "99 32100""12 12 15"7threshold' = 2
# The transactions count for each user,regardless of role are:
# Example
# logs = ["88 99 200""88 99 300" "99 32100" " 12 12 15"7threshold = 2
# The transactions count for each user.regardless of role are:IDTransactions--------------99488412l32
# There are two users with ateast threshold' =
# 2 transactions: 99 and 88. Inascending order, the return array
# is [88’99]
# Note: In the last log entry, user12 was on both sides of thetransaction. This counts as only1 transaction for user 12.
# Function Description
# Complete the function processlogs in
# the editor below.
# The function has the following
# parameter(s):
# string logsIn each logslij denotes
# the ith entry in the logs
# int threshola: the minimum numberof transactions that a user must have
# to be included in the result
# Returns:
# stringl: an array of user id's as
# strings, sorted ascending by numeric
# value



def processLogs(logs, threshold):
    # Write your code here
    logs = sorted(logs)
    print(logs)
    users = {}
    for log in logs:
        sender, receiver, amount = log.split(" ")
        
        if sender not in users:
            users[sender] = 1
        else:
            users[sender] += 1
        if sender == receiver:
            continue
        if receiver not in users:
            users[receiver] = 1
        else:
            users[receiver] += 1
    print(users)
    result = []
    for user in users:
        if users[user] >= threshold:
            result.append(user)
    return result

logs=["1 2 50","1 7 70", "1 3 20", "2 2 17"]
thereshold=2
print("this",processLogs(logs,thereshold))



# 3. River Records
# ALL
# Given an array of integers, without reordering, determine themaximum difference between any element and any priorsmaller element.lf there is never a lower prior element, return7
# Example
# arr = [5, 3, 6, 7 4
# There are no earlier elements than arr / 07.There is no earlier reading with a value lower than arrf17There are two lower earlier readings with a value lowerthan arrl21 = 6:
# arr[2] - arr[1] = 6  3 = 3
# arr[2] - arn07 = 6 - 5 = 1There are three lower earlier readings with a lower valuethan arr[3] = 7:
# arr[3] - arr12] = 7 - 6 = 1
# arr[3] - arr[1] = 7 - 3 = 4
# arr[3] - arr[0] = 7 - 5 = 2
# There is one lower earlier reading with a lower value than arr[4j = 4:
# arr[4] - arr[1] = 4 - 3 = 1
# The maximum trailing record is arr[37 - arr[1] = 4
# Example
# arr = [4, 3, 2, 1]
# No item in arr has a lower earlier reading, therefore return -1
# Function Description
# Complete the function maximumTrailing in the editor below.

# Returns:int : the maximum trailing difference, or -1 if no element inarr has a lower earlier value
# Constraints
# 1 <= n≤2x 10_5
# -106 <arrlil< 10 and 0<i<n

def maxTrailing(arr):
    max = 0
    min = arr[0]
    if not arr or len(arr) <2:
        return -1
    
    
    
    for i in range(1,len(arr)):
        if arr[i] < min:
            min = arr[i]
        if arr[i] - min > max:
            max = arr[i] - min
    return max

arr = [5,3,6,7,4]
print(maxTrailing(arr))

# 4. Newton's Method
# Consider the function:
# f(z)=a·z2-bexp(1 +In(a))where a > b > 0 are two arbitrary constants, exp() is theexponential function and in() is the natural log.
# We will write some code to analyze this function for values of x >0.
# In particular, you will write a method that given values of a, band an initial value of x returns the zero (root) nearest to the initiavalue of x using Newton's method.
# Newton's Method ReviewThe zero of a real-valued function fis a number x such that fx) =0Newton's method is a classic root finding algorithm.Given an initial value x, Newton's method proceeds using theiteration:
# where f'is the derivative of function f
# Your goal is to implement Newton's method for the functionalform above and given values of a, b and an initial value of x, runthe iterative procedure until lt+1 - 2t < 10-16and returnthe root value found.
import numpy as np

def newtons_method(a, b, x_init):
    # Initialize x
    x = x_init
    while True:
        # Precompute the exponential term
        exp_term = b*np.exp(1 + np.log(x))
        
        # Compute x_{t+1}
        x_new = x - (a*x**2-exp_term) / (2*a*x - exp_term/x)

        # Check the stopping condition
        if abs(x_new - x) < 1e-16:
            break

        # Update x
        x = x_new

    return x

print(newtons_method(1,2,3))



# Two Stock Trading ProblemYou are given two length T float arrays. pricesA is a float arraycontaining the prices series for stock A. pricesB is a float arraycontaining the prices series for stock B. Element t of each floatarray contains the price of each stock at the close of day t.
# Your boss wants to benchmark your team's current tradingstrategy against an optimal strategy that has knowledge of thefull prices series prior to any trading.
# Your goal is to design an algorithm to find the maximum profitgiven these two price series under the following rules!
# You can hold at most one share on each day - ie you can ownstock A, own stock B or own neither stock. You cannot own bottstock A and stock B.
# You cannot short either stock - ie. you can only sell stock A(stock B) if you own stock A (stock B).
# You can complete as many transactions as you like - ie. you canbuy stock A (stock B) and sell it multiple times
# You cannot sell stock A istock B) and buy stock B (stock A) on thesame day - i.e. you can only buy one share of stock A or oneshare of stock B on day t if you own no stock on day t-1.
# You can assume that the stock prices are non-negative
# Example 1:pricesA: [1,2,3,4,5]pricesB:[5,4,3,2,1]Output: 4Explanation: Buy stock A on day 1 and sell on day 5, profit = 5 - 1= 4.
# Example 2:pricesA: [1,2,3,2.11pricesB:[3,2,1,4,5]Ouptut: 5Explanation: Buy stock A on day 1 and sell on day 2, profit = 2 - 1= 1. Then buy stock B on day 3 and sell on day 5, profit = 5 - 1 =4. Total profit = 5.

def max_profit(prices_A, prices_B):
    n = len(prices_A)
    dp_A = [0] * n
    dp_B = [0] * n
    dp_no_stock = [0] * n

    dp_A[0] = -prices_A[0]
    dp_B[0] = -prices_B[0]
    for i in range(1, n):
        dp_A[i] = max(dp_A[i-1], dp_no_stock[i-1]  - prices_A[i-1])
        dp_B[i] = max(dp_B[i-1], dp_no_stock[i-1]  - prices_B[i-1])
        dp_no_stock[i] = max(dp_no_stock[i-1], dp_A[i-1] + prices_A[i], dp_B[i-1] + prices_B[i])

    return max(dp_A[-1], dp_B[-1], dp_no_stock[-1])

pricesA = [1,2,3,4,5]
pricesB = [5,4,3,2,1]
print(max_profit(pricesA, pricesB))


