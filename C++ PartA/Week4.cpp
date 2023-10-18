// Encheng Liu 2023/08/24
// 
// C++ for C Programmers Part A
// 
// Prim Method
// 
// Coding for happy union


#include<iostream>
#include<random>
#include<queue>
#include<fstream>


using namespace std;


class DisjointSet {
private:
	int size;
	int* parent;

public:
	DisjointSet(int s) {
		size = s;
		parent = new int[size];
		for (int i = 0; i < size; ++i)
			parent[i] = -1;
	}

	~DisjointSet() {
		delete[] parent;
	}

	void Union(int root1, int root2) {
		if (root1 = root2)return;
		if (parent[root1] > parent[root2]) {
			parent[root2] += parent[root1];
			parent[root1] = root2;
		}
		else {
			parent[root1] += parent[root2];
			parent[root2] = root1;
		}
	}

	int Find(int x) {
		if (parent[x] < 0)return x;
		return parent[x] = Find(parent[x]);
	}
};

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
		for (i = 0; i < Vers; i++)
			if (edgeNode* p = verList[i].head) {
				edgeNode* q = p->next;
				while (q) {
					delete p;
					p = q;
					q = q->next;
				}
				delete p;
				p = nullptr;
			}
		delete[] verList;
		verList = nullptr;


	}

	//noedge denotes the flag of infinite, namely the edge doesn't exist
	void prim(int noEdge = 255)const {
		bool* flag = new bool[Vers];
		int* lowCost = new int[Vers];
		int* startNode = new int[Vers];

		edgeNode* p;
		int min;
		int start, i, j;
		int totalweight = 0;


		for (i = 0; i < Vers; ++i) {
			flag[i] = false;
			lowCost[i] = noEdge;
		}

		start = 0;
		for (i = 1; i < Vers; ++i) {
			for (p = verList[start].head; p != NULL; p = p->next)
				if (!flag[p->end] && lowCost[p->end] > p->weight) {
					lowCost[p->end] = p->weight;
					startNode[p->end] = start;
				}

			flag[start] = true;
			min = noEdge;
			for (j = 0; j < Vers; ++j) {
				if (lowCost[j] < min) {
					min = lowCost[j];
					start = j;
				}
			}


			edgeNode* end = verList[startNode[start]].head;
			while (end) {
				if (end->end == verList[start].ver) {
					cout << "The weight is" << end->weight << endl;
					totalweight += end->weight;
					break;
				}
				else end = end->next;
			}

			cout << '(' << verList[startNode[start]].ver << ',' << verList[start].ver << ")\t";
			lowCost[start] = noEdge;

		}
		delete[] flag;
		delete[] startNode;
		delete[] lowCost;
		cout << endl << "The minimal Weight is" << totalweight << endl;
	}


	/*
	void krushal()const {
		int edgesAccepted = 0, u, v;
		edgeNode* p;
		edge e;
		DisjointSet ds(Vers);
		priority_queue<edge,vector<edge>,edge>pq;

		for (int i = 0; i < Vers; ++i) {
			for (p = verList[i].head; p != NULL; p = p->next) {
				if (i < p->end) {
					e.beg = i;
					e.end = p->end;
					e.w = p->weight;
					pq.push(e);
				}
			}

		}

		int totalweight = 0;


		while (edgesAccepted < Vers ) {
			e = pq.top();
			pq.pop();
			u = ds.Find(e.beg);
			v = ds.Find(e.end);
			if (u != v) {
				edgesAccepted++;
				ds.Union(u, v);

				edgeNode* end=verList[e.beg].head;
				while (end) {
					if (end->end == e.end) {
						cout << "The weight is" << end->weight << endl;
						totalweight += end->weight;
						break;
					}
					else end = end->next;
				}
				
				cout << "(" << verList[e.beg].ver << "," << verList[e.end].ver << ")\t";
			}
			
		}
		cout <<endl<< "The minimal Weight is" << totalweight << endl;
	}

	*/




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
	void bfs()const {
		bool* visited = new bool[Vers];
		int currentNode;
		queue<int> q;
		edgeNode* p;
		for (int i = 0; i < Vers; ++i)visited[i] = false;

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

	/*
	//Reload the operator to weight the value of two edge, in a priorityqueue
	struct edge {
		int beg, end;
		int w;
		bool operator < (const edge& rp)const {
			return w < rp.w;
		}

		
		bool operator() (const edge& a, const edge& b) {
			return a.w > b.w;  // '>' ����С��
		}
		
	};
	*/



	verNode* verList;

	int find(int v)const {
		for (int i = 0; i < Vers; i++)
			if (verList[i].ver == v)return i;
	}


	
};

int main() {
	int VerSize;
	
	
	ifstream in;
	int i, j, weight;

	in.open("data.txt",std::ios::in);
	if (!in) { cerr << "open file error\n"; return 1; }

	in >> VerSize;
	adjListGraph KruskalMST(VerSize);
	while (in >> i >> j >> weight) {
		KruskalMST.insert(i, j, weight);
	}
	in.close();
	KruskalMST.bfs();
	cout << endl << endl << endl << endl;
	KruskalMST.prim();
}