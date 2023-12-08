#include<iostream>
#include<vector>
#include<unordered_map>
#include<algorithm>
#include<string>

using namespace std;

/*

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
*/

int maxTrailing(int arr_count, int* arr) {
	int max = -1;
	int min = arr[0];
	for (int i = 1; i < arr_count; i++) {
		if (arr[i] < min) {
			min = arr[i];
		}
		else if (arr[i] - min > max) {
			max = arr[i] - min;
		}
	}
	return max;
}


#include <cmath>



inline double f(double a, double b, double x) {
	return a * x * x - b * std::exp(1 + std::log(x));
}

inline double df(double a, double b, double x) {
	return 2 * a * x - b * std::exp(1 + std::log(x)) / x;
}
inline double abs1(double x) {
	if (x < 0) {
		return -x;
	}
	else {
		return x;
	}
}

double newton(double a, double b, double x)
{
	double eps = 1e-16;
	double m;
	do
	{
		m = f(a, b, x) / df(a, b, x);
		x = x - m;
	} while (abs1(m) > eps);
	return x;
}








int main() {
	int a = 1, b = 2, x = 3;

	cout << newton(a, b, x) << endl;

	return 0;
}

