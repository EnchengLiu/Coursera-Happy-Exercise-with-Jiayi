#include<iostream>
#include<random>
#include<ctime>
#include<queue>
#include<iterator>

using namespace std;


/*
* 
* Here is the program Output 
Please type in the nodes at the edge
6
. - . - . - . - . - .
 \ / \ / \ / \ / \ / \
  . - . - . - . - . - .
   \ / \ / \ / \ / \ / \
	. - . - . - . - . - .
	 \ / \ / \ / \ / \ / \
	  . - . - . - . - . - .
	   \ / \ / \ / \ / \ / \
		. - . - . - . - . - .
		 \ / \ / \ / \ / \ / \
		  . - . - . - . - . - .
Insutrution:
The blue player must make a connected set of blue hexagons from east to west. The red player must do the same from north to south. At each turn a player chooses an unoccupied hexagon and gives it their color.  Unlike tic-tac-toe the game cannot end in a draw. Indeed it can be proven that by best play the first player wins.(John Nash). However there is no known optimal strategy.

Blue player go first
BLUE player is substitute by the computer.You have no Choice but accept
Do you want autoplay as a red player?
 Please Use 0 denote No, 1 denote Yes
1
Computer step in x=0 y=0
B - . - . - . - . - .
 \ / \ / \ / \ / \ / \
  . - . - . - . - . - .
   \ / \ / \ / \ / \ / \
	. - . - . - . - . - .
	 \ / \ / \ / \ / \ / \
	  . - . - . - . - . - .
	   \ / \ / \ / \ / \ / \
		. - . - . - . - . - .
		 \ / \ / \ / \ / \ / \
		  . - . - . - . - . - .
Computer step in x=0 y=1
B - B - . - . - . - .
 \ / \ / \ / \ / \ / \
  . - . - . - . - . - .
   \ / \ / \ / \ / \ / \
	R - . - . - . - . - .
	 \ / \ / \ / \ / \ / \
	  . - . - . - . - . - .
	   \ / \ / \ / \ / \ / \
		. - . - . - . - . - .
		 \ / \ / \ / \ / \ / \
		  . - . - . - . - . - .
Computer step in x=0 y=2
B - B - B - . - . - .
 \ / \ / \ / \ / \ / \
  . - . - . - . - . - .
   \ / \ / \ / \ / \ / \
	R - . - . - . - . - R
	 \ / \ / \ / \ / \ / \
	  . - . - . - . - . - .
	   \ / \ / \ / \ / \ / \
		. - . - . - . - . - .
		 \ / \ / \ / \ / \ / \
		  . - . - . - . - . - .
Computer step in x=0 y=3
B - B - B - B - . - .
 \ / \ / \ / \ / \ / \
  . - . - . - . - . - .
   \ / \ / \ / \ / \ / \
	R - . - . - . - . - R
	 \ / \ / \ / \ / \ / \
	  . - . - . - . - . - .
	   \ / \ / \ / \ / \ / \
		. - R - . - . - . - .
		 \ / \ / \ / \ / \ / \
		  . - . - . - . - . - .
Computer step in x=0 y=4
B - B - B - B - B - .
 \ / \ / \ / \ / \ / \
  . - . - . - . - . - .
   \ / \ / \ / \ / \ / \
	R - . - . - . - . - R
	 \ / \ / \ / \ / \ / \
	  . - . - . - . - . - .
	   \ / \ / \ / \ / \ / \
		. - R - . - . - . - .
		 \ / \ / \ / \ / \ / \
		  . - . - . - . - . - R
Computer step in x=0 y=5
B - B - B - B - B - B
 \ / \ / \ / \ / \ / \
  . - . - . - . - . - R
   \ / \ / \ / \ / \ / \
	R - . - . - . - . - R
	 \ / \ / \ / \ / \ / \
	  . - . - . - . - . - .
	   \ / \ / \ / \ / \ / \
		. - R - . - . - . - .
		 \ / \ / \ / \ / \ / \
		  . - . - . - . - . - R
Blue win
Total steps = 11
B - B - B - B - B - B
 \ / \ / \ / \ / \ / \
  . - . - . - . - . - R
   \ / \ / \ / \ / \ / \
	R - . - . - . - . - R
	 \ / \ / \ / \ / \ / \
	  . - . - . - . - . - .
	   \ / \ / \ / \ / \ / \
		. - R - . - . - . - .
		 \ / \ / \ / \ / \ / \
		  . - . - . - . - . - R

*/


class NashsHexGame
{

private:
	// The actual size of the edges
	int vSize;
	string edges;
	const static char Blue = 'B';
	const static char Red = 'R';
	const static char Blank = '.';
	

	//Use two dimensional vector to construct the board
	vector<vector<char>>board;

	//Define the direction of movement
	const int directions[6][2] = {
		{-1, 0}, {-1, 1}, // top left, top right
		{0, -1}, {0, 1},  // left, right
		{1, -1}, {1, 0}   // buttom left, buttom right
	};

	//x,y is the cordinate of the input
	bool validmove(int x, int y)const {
		return x >= 0 && x < vSize && y >= 0 && y < vSize;
	}

	/*
	Given that blue player move horizontally, red move vertically,
	So if this step make flags[0]flag[1] both true, this step is on the border
	*/
	void checkborders (int x, int y, vector<bool>& flags, char side) const{
		if (side == Blue)
		{
			if (y == 0)
				flags[0] = true;
			if (y == vSize - 1)
				flags[1] = true;
		}
		else if (side == Red)
		{
			if (x == 0)
				flags[0] = true;
			if (x == vSize - 1)
				flags[1] = true;
		}
	}



public:
	//Constructor, Node is the name of every Vertice, vSize is the bumber of the Vertices in graph
	NashsHexGame(int size):vSize(size), board(size, vector<char>(size,'.')) {
		edges = "\\";
		for (int i = 1; i < vSize; i++)edges += " / \\";
		
	}

	//copy constructor to make space for the computer Monte Carlo Simulation
	NashsHexGame(const NashsHexGame& board2)
	{
		board = board2.board;
		edges = board2.edges;
		vSize = board2.vSize;
	}

	// Store the number of Vertice and Edges
	enum class player {
		BLUE, RED
	};

	//print the board
	void printBoardGraph()
	{
		// first line
		cout << board[0][0];
		for (int j = 1; j < vSize; j++)
			cout << " - " << board[0][j];
		cout << endl;

		//Using space to indent the output as a hex
		string space = "";
		for (int i = 1; i < vSize; i++)
		{
			space += ' ';
			cout << space << edges << endl; //No element this row
			space += ' ';
			cout << space << board[i][0];
			for (int j = 1; j < vSize; j++)
				cout << " - " << board[i][j];
			cout << endl;
		}
	}

	//deploy a color to one point and check whether this step is compliant
	bool move(int x, int y, player p) {
		if (validmove(x, y) == false)
			return false;

		if (board[x][y] != Blank)
			return false;

		if (p == player::BLUE)
			board[x][y] = Blue;
		else if (p == player::RED)
			board[x][y] = Red;

		return true;
	}

	// undo a false move
	bool CtrlZ(int x, int y)
	{
		if (validmove(x, y) == false)
			return false;

		board[x][y] = Blank;

		return true;
	}




	bool ifwin(int x, int y)const
	{
		//Check whether this move lead to winning
		if (validmove(x, y) == false || board[x][y] == Blank)
			return false;

		char side = board[x][y];

		//
		vector<bool> flags(2, false);

		vector<vector<bool> > visited(vSize, vector<bool>(vSize));
		visited[x][y] = true;


		//Use Queue to check every 
		queue<pair<int, int> > traces;
		traces.push(make_pair(x, y));
		

		while (!traces.empty())
		{
			auto top = traces.front();
			traces.pop();
			checkborders(top.first, top.second, flags, side);
			
			/*
			check all the direction of the step is the same color of this step or not,
			If so, enqueue it and continue search.
			If the search end and the final point is a border point with the same color, the corresponding players win.
			*/
			for (int n = 0; n < 6; n++)
			{
				int curX = top.first + directions[n][0];
				int curY = top.second + directions[n][1];
				if (validmove(curX, curY) && board[curX][curY] == side
					&& visited[curX][curY] == false)
				{
					visited[curX][curY] = true;
					traces.push(make_pair(curX, curY));
				}
			}
		}

		return flags[0] && flags[1];
	}

	pair<int, int> MonteCarloChess(int maxTimes=10000) {
		//Copy an new board to codunct Monte Carlo sampling
		//Because Later will make change via function(move), the private properity would change. Must restore a new one to subustitue and refresh
		vector<vector<char>> NewBoard1 = board;
		//Initialize the bestMove and steps to win
		int wins = 0, turn = 0, lastElement;
		vector<int> bestMoves(vSize * vSize);

		//record the empty point on the board for the AI to step in
		
		vector<int> blankspot,BlankSpotCounter(vSize * vSize);
		for (int i = 0; i < vSize; ++i) {
			for (int j = 0; j < vSize; ++j) {
				if (NewBoard1[i][j] == Blank) {
					++BlankSpotCounter[i * vSize + j];
					blankspot.push_back(i * vSize + j);
				}
			}
		}

		//Make BlankspotCopy and NewBoard2 to forloop refresh
		vector<int>blankspotCopy= blankspot;
		for (int times = 0; times < maxTimes; times++) {
			board = NewBoard1;
			blankspot = blankspotCopy;
			lastElement = blankspot[blankspot.size() - 1];
			//Change the sequence of the container, mentioned that std::queue is not a container; it's a container adapter.
			random_shuffle(blankspot.begin(), blankspot.end());
			while (!blankspot.empty()) {
				turn = !turn;
				if (turn == 1) move(lastElement/vSize, lastElement % vSize, player::BLUE);
				else move(lastElement / vSize, lastElement % vSize, player::RED);
				blankspot.pop_back();
			}
			for (int i = 0; i < vSize; i++) {
				for (int j = 0; j < vSize; ++j) {
					if (board[i][j] == Blue && ifwin(i, j) && BlankSpotCounter[i * vSize + j] == 1) {
						++bestMoves[i * vSize + j];
						++wins;
					}
				}
			}
		}


		//restore the board to the original one

		if (*max_element(bestMoves.begin(), bestMoves.end()) == 0) {
			return make_pair(blankspotCopy[0] / vSize, blankspotCopy[0] % vSize);
		}
		else {
			int dist = distance(bestMoves.begin(), max_element(bestMoves.begin(), bestMoves.end()));
			return make_pair(dist / vSize, dist / vSize);
		}
	}


	~NashsHexGame() {}


};



int main() {
	int size;
	cout << "Please type in the nodes at the edge" << endl;
	cin >> size;
	NashsHexGame board(size);
	board.printBoardGraph();
	//srand(time(0));
	//USE C++11 <random> library
	std::default_random_engine engine;
	int turn = 0;
	int steps = 0;
	int x = 0, y = 0;
	pair<int, int> ComputerDecision;

	bool AutoPlayFlags[2] = { false };
	cout << "Insutrution:"<<endl << "The blue player must make a connected set of blue hexagons from east to west. The red player must do the same from north to south. At each turn a player chooses an unoccupied hexagon and gives it their color.  Unlike tic-tac-toe the game cannot end in a draw. Indeed it can be proven that by best play the first player wins.(John Nash). However there is no known optimal strategy." << endl;
	cout << endl<<"Blue player go first"<<endl;


	cout << "BLUE player is substitute by the computer.You have no Choice but accept" << endl;
	cout << "Do you want autoplay as a red player?  \n Please Use 0 denote No, 1 denote Yes" << endl;
	cin >> AutoPlayFlags[1];



	while (true)
	{
		if (board.ifwin(x, y))
		{
			cout << (turn ? "Blue" : "Red") << " win" << endl;
			cout << "Total steps = " << steps << endl;
			board.printBoardGraph();
			break;
		}
		steps++;

		turn = !turn;
		if (turn == 1)
		{
			NashsHexGame board2 = board;
			ComputerDecision = board2.MonteCarloChess();
			board.move(ComputerDecision.first, ComputerDecision.second, NashsHexGame::player::BLUE);
			x = ComputerDecision.first;
			y = ComputerDecision.second;
			cout << "Computer step in x=" << ComputerDecision.first << " y=" << ComputerDecision.second << endl;
			board.printBoardGraph();
		}
		else
		{
			while (!board.move(x, y, NashsHexGame::player::RED)) {
				if (AutoPlayFlags[1]) {
					x = engine() % size;
					y = engine() % size;
				}
				else {
					cout << "Please type in the location you want to step:";
					cin >> x >> y;
					cout << "Your step in x=" << x << " y=" << y << endl;
				}
			}
			
		}
	}
	return 0;
}