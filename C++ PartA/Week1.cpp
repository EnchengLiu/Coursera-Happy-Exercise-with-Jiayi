#include<iostream>
#include<vector>
using namespace std;

const int N = 40;

inline void sum(int& p, vector<int> &d) {
	for (auto i = d.begin(); i != d.end(); i++)p += *i;
}


int main() {
	int accum = 0;
	vector<int> data;
	for (int i = 0; i < N; ++i) {
		data.push_back(i);
	}
	sum(accum, data);
	cout << "sum is \n" << accum;
	return 0;

}