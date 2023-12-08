
#include<iostream>
#include<fstream>
#include<istream>
#include<string>

using namespace std;
//Add Number Series II
/*
Write a program that, given an integer V, sums all the whole numbersfrom 1 through V (both inclusive). Do not include in your sum any ofthe intermediate values (1 and IV inclusive) that are divisible by 5 or 7.
*/

template<class T>class Stack
{
private:
	struct Node
	{
		T data;
		Node* next;
	};
	Node* head;
	Node* p;
	int length;

public:
	Stack()
	{
		head = NULL;
		length = 0;
	}
	void push(T n)//入栈
	{
		Node* q = new Node;
		q->data = n;
		if (head == NULL)
		{
			q->next = head;
			head = q;
			p = q;
		}
		else
		{
			q->next = p;
			p = q;
		}
		length++;
	}

	T pop()//出栈并且将出栈的元素返回
	{
		if (length <= 0)
		{
			abort();
		}
		Node* q;
		T data;
		q = p;
		data = p->data;
		p = p->next;
		delete(q);
		length--;
		return data;
	}
	int size()//返回元素个数
	{
		return length;
	}
	T top()//返回栈顶元素
	{
		return p->data;
	}
	bool isEmpty()//判断栈是不是空的
	{
		if (length == 0)
		{
			return true;
		}
		else
		{
			return false;
		}
	}
	void clear()//清空栈中的所有元素
	{
		while (length > 0)
		{
			pop();
		}
	}
};


int main()
{
	char* filePath = "input.txt";
	ifstream file;
	file.open(filePath, ios::in);

	if (!file.is_open())

		return 0;

	Stack<int>  vv;
	std::string strLine;
	while (getline(file, strLine))
	{
		std::stringstream ss(strLine);
		int i;
		while (ss >> i)
			vv.push(i);
		while (!vv.isEmpty()) {
			cout << vv.pop() << " " << endl;
		}
		

		
	}



/*
Problem1
int add1(int n) {
	if (n == 1)return 1;
	if (n % 5 == 0 || n % 7 == 0)return sum(n - 1);
	return sum(n - 1) + n;

}

int add2(int n) {

	int sum5 = (n / 5) * ((n / 5) + 1) / 2 * 5;
	int sum7 = (n / 7) * ((n / 7) + 1) / 2 * 7;
	return n * (n + 1) / 2 - sum5 - sum7;
}

int main() {
	int sum=0, input;
	while (true) {
		cin >> input;
		cout << "Use recursion:" << add1(input) << endl;
		cout << "Easy Way:" << add2(input) << endl;



	}
}

*/