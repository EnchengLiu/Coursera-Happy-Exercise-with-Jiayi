
#include<iostream>
#include<vector>
#include<unordered_map>
#include<algorithm>
#include<string>

using namespace std;

//这里是第一题
/*
Frequency Sort
Given an array of n item values, sort the array in ascending order, first by the frequency of each value, then by the values themselves

Example
n=6
items=[4,5,6,5,4,3]
*/
bool comp(const pair<int,int>& a, const pair<int, int>& b) {
	// 如果value相等，比较key值
	if (a.second == b.second)
		return a.first < b.first;
	else
		// 否则比较value值
		return  a.second < b.second;
}


int *itemSort(int* item,int len) {
	
	vector<int> v;
	int n[10] = { 0 };
	unordered_map<int, int> m;
	for (int i = 0; i < len; i++) {
		
		m[item[i]] = m[item[i]] + 1;
		
	}
	vector<pair<int, int>> vec(m.begin(), m.end());

	sort(vec.begin(), vec.end(), comp);
	int* result= new int[len];
	//cout << "排序之后的结果" << endl;
	unsigned int arr_length = 0;
	for (auto i : vec)
	{
		//cout << i.first << ":" << i.second << endl;
		for (int j = 0; j < i.second; j++)
		{
			
			result[arr_length++] = i.first;
		}
			
	}
	
	//for(int i=0;i<len;i++)
	//	cout << result[i] << endl;
	return result ;
}


//这里是第二题
/*
Special Sequence
*/
string GetNumber(int n) {
	if (n == 1)return "1";
	string previous= GetNumber(n - 1),result="";
	int count = 1;

	for (int i = 0; i < previous.length(); i++)
	{
		if (previous[i] == previous[i + 1])
			count++;
		else
		{
			result += to_string(count) + previous[i];
			count = 1;
		}
	}
	return result;
}

int* sumOfTheDigits(int q[],int len) {
	//cout<< len << endl;
	int * result = new int[len]();
	for (int i = 0; i < len; i++)
	{
		string str = GetNumber(q[i]);
		for (int j = 0; j < str.length(); j++) {
			result[i] += stoi(string(1, str[j]));
		}
	//	cout<< result[i] << endl;
	}
	return result;
}


//这里是第三题，结束啦
/*
* Extraordinaty Substrings
*/
int CountSubstrings(string input_str, int len) {
	//unordered_map<string, int> m = { {'a',1},{"b",1} {"c",2},{"d",2},{"e",2},{"f",3},{"g",3},{"h",3},{"i",4},{"j",4},{"k",4},{"l",5},{"m",5},{"n",5},{"o",6},{"p",6},{"q",6},{"r",7},{"s",7},{"t",7},{"u",8},{"v",8},{"w",8},{"x",9},{"y",9},{"z",9}};
	unordered_map<char, int>m = {};
	m['a'] = 1;
	m['b'] = 1;
	m['c'] = 2;
	m['d'] = 2;
	m['e'] = 2;
	m['f'] = 3;
	m['g'] = 3;
	m['h'] = 3;
	m['i'] = 4;
	m['j'] = 4;
	m['k'] = 4;
	m['l'] = 5;
	m['m'] = 5;
	m['n'] = 5;
	m['o'] = 6;
	m['p'] = 6;
	m['q'] = 6;
	m['r'] = 7;
	m['s'] = 7;
	m['t'] = 7;
	m['u'] = 8;
	m['v'] = 8;
	m['w'] = 8;
	m['x'] = 9;
	m['y'] = 9;
	m['z'] = 9;

	int result = 0;
	int sum=0;
	for (int i = 0; i < input_str.length(); i++) //遍历字符串
	{
		for (int j = 1 + i; j < input_str.length() + 1; j++)
		{
			sum = 0;
			string here = input_str.substr(i, j - i);
			//cout << here << endl;
			for (auto k : here) {
				sum += m[k];
			}
			if(sum % here.size()==0)
				result++;
		}
	}
	//cout<<result << endl;
	return result;

}


int main() {
	int item[] = { 8,5,5,5,5,1,1,1,4,4 };
	int len1 = sizeof(item) / sizeof(item[0]);
	
	
	int item2[] = {1,2,3,3,49,50};
	itemSort(item,len1);
	int len2 = sizeof(item2) / sizeof(item2[0]);
	sumOfTheDigits(item2,len2);
	string str = "asdf";
	CountSubstrings(str, 4);
	
	return 0 ;
}

