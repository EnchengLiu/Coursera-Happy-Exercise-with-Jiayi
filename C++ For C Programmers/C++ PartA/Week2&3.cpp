// Encheng Liu 2023/08/19
// 
// C++ for C Programmers Part A
// 
// Dijikstra's Alogrithm for Weighted Random Graph
// 
// Coding for happy union
/*
For 20%, the answer is 5.46163
For 40%, the answer is 3.17027
*/


#include<iostream>
#include<random>
#include<ctime>
#include<queue>

using namespace std;

class adjListGraph
{
public:
	//Constructor, Node is the name of every Vertice, vSize is the bumber of the Vertices in graph
	adjListGraph(int vSize) {
		Vers = vSize;
		Edges = 0;
		verList = new verNode[vSize];
		for (int i = 0; i < Vers; ++i)verList[i].ver = i;
	}

	~adjListGraph() {
		int i;
		for(i=0;i<Vers;i++)
			if(edgeNode* p = verList[i].head) {
				edgeNode* q = p->next;
				while (q) {
					delete p;
					p = q;
					q = q->next;
				}
				delete p;
				p=nullptr;
			}	
		delete[] verList;
		verList=nullptr;


	}


	// x,y is the value of two node in the same edge, w is the weigh/light of the edge
	void insert(int x, int y, double w) {
		int u = find(x), v = find(y);
		verList[u].head = new edgeNode(v, w, verList[u].head);
		++Edges;
	}

	void remove(int x, int y) {
		int u = find(x), v = find(y);
		edgeNode* p = verList[u].head, * q;
		if (p == NULL)return;
		if (p->end == v) {
			verList[u].head = p->next;
			delete p;
			--Edges;
			return;
		}
		while (p->next != NULL && p->next->end != v)p = p->next;
		if (p->next != NULL) {
			q = p->next;
			p->next = q->next;
			delete q;
			--Edges;
		}
	}
	bool exist(int x, int y)const {
		int u = find(x), v = find(y);
		edgeNode* p = verList[u].head;
		while (p != NULL && p->end != v)p = p->next;
		if (p == NULL)return false;
		else return true;
	}

	

	//breadth first search to print the graph
	


	//������Ҫ�ĸ����ܶ�ͼ�����ù�����Ȳ������������
	void InitiallizeGraph(int density, double LengthMin, double LengthMax) {
		srand(static_cast<unsigned int>(time(NULL)));
		for (int i = 0; i < Vers; i++) {
			for (int j = 0; j < Vers; j++) {
				if (i != j) {
					if (rand() % 100 <= density ? true : false) {
						double Length = (double)rand() / RAND_MAX * (LengthMax - LengthMin) + LengthMin;
						this->insert(i, j, Length);
						this->insert(j, i, Length);
					}
				}
			}
		}
		bfs();
	}

	double dijkstra(int start, double noEdge)const {
		double* distance = new double[Vers];
		int* prev = new int[Vers];
		bool* known = new bool[Vers];

		int u, sNo, i, j;
		edgeNode* p;
		double min;
		for (i = 0; i < Vers; ++i) {
			known[i] = false;
			distance[i] = noEdge;
		}
		sNo = find(start);

		distance[sNo] = 0;
		prev[sNo] = sNo;

		for (i = 1; i < Vers; ++i) {
			min = noEdge;
			for (j = 0; j < Vers; ++j) {
				if (!known[j] && distance[j] < min) {
					min = distance[j];
					u = j;
				}
			}
			known[u] = true;
			for (p = verList[u].head; p != NULL; p = p->next)
				if (!known[p->end] && distance[p->end] > min + p->weight) {
					distance[p->end] = min + p->weight;
					prev[p->end] = u;
				}
		}

		double sum = 0;
		for (i = 0; i < Vers; ++i) {
			sum += distance[i];
			cout << "��" << start << "��" << verList[i].ver << "��·��Ϊ:" << endl;
			printPath(sNo, i, prev);
			cout << "\t ����Ϊ��" << distance[i] << endl;
		}
		return sum / double((Vers - 1));
	}

private:
	// Store the number of Vertice and Edges
	int Vers, Edges;

	struct edgeNode {
		int end;
		double weight;
		edgeNode* next;

		edgeNode(int e, double w, edgeNode* n = NULL) {
			end = e;
			weight = w;
			next = n;
		}
	};

	struct verNode {
		int ver;
		edgeNode* head;

		verNode(edgeNode* h = NULL) {
			head = h;
		}
	};

	verNode* verList;

	int find(int v)const {
		for (int i = 0; i < Vers; i++)
			if (verList[i].ver == v)return i;
	}

	//���dijkstra���Ĳ���·��
	void printPath(int start, int end, int prev[])const {
		if (start == end) {
			cout << verList[start].ver;
			return;
		}
		printPath(start, prev[end], prev);
		cout << "-" << verList[end].ver;
	}

	void bfs()const {
		bool* visited = new bool[Vers];
		int currentNode;
		queue<int> q;
		edgeNode* p;
		for (int i = 0; i < Vers; ++i)visited[i] = false;
		cout << "��ǰͼ�Ĺ�����ȱ�������Ϊ:" << endl;

		for (int i = 0; i < Vers; ++i) {
			if (visited[i] == true)continue;
			q.push(i);
			while (!q.empty()) {
				currentNode = q.front();
				q.pop();//����
				if (visited[currentNode] == true)continue;
				cout << verList[currentNode].ver << '\t';
				visited[currentNode] = true;
				p = verList[currentNode].head;
				while (p != NULL) {
					if (visited[p->end] == false)q.push(p->end);
					p = p->next;
				}
			}
			cout << endl;
		}
	}
};

int main() {
	adjListGraph Density20(50),Density40(50);
	cout << "�ܶ�Ϊ20%��ͼ�Ĺ�����ȱ���Ϊ" << endl;
	Density20.InitiallizeGraph(20, 1, 10);
	cout << "�ܶ�Ϊ20%��ͼ�����·��Ϊ" << endl;
	cout << "����ƽ�����·��������" << Density20.dijkstra(1, 255) << endl;

	cout << endl << endl << endl;
	cout << "�ܶ�Ϊ40%��ͼ�Ĺ�����ȱ���Ϊ" << endl;
	Density40.InitiallizeGraph(40, 1, 10);
	cout << "�ܶ�Ϊ40%��ͼ�����·��Ϊ" << endl;
	
	cout << "����ƽ�����·��������" << Density40.dijkstra(1, 255) << endl;
}