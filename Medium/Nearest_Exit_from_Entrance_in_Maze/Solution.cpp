#include <iostream>
#include <vector>
#include <queue>
#include <tuple>
using namespace std;
class Solution {
public:
    int nearestExit(vector<vector<char>>& maze, vector<int>& entrance) {
        
    

        // Initialize the variable
        int i,j,x,y,dist;
        int m = maze.size() , n = maze[0].size();
        int entrance_row = entrance[0], entrance_column = entrance[1];

        // The four directions to move in
        int directions[4][2] = {{-1,0},{1,0},{0,-1},{0,1}};

        // Initializing a queue for traversal
        queue<vector<int>> q;


        // Add the entrance values as first element to the queue
        q.push({entrance_row,entrance_column,0});
        maze[entrance_row][entrance_column] = '+';

        while (!q.empty()){
            vector<int> front = q.front();

            i = front[0];     // Getting the current values from the front of the queue
            j = front[1];
            dist = front[2];

            q.pop();  // Pop the front
            for(auto dir:directions){

                x = i + dir[0];
                y = j + dir[1]; // Checking the neighbours in all 4 directions 

                if(0<=x && x<m && 0<=y && y<n && maze[x][y] == '.'){ // Check if the indexes are valid and the point is not a wall

                    if(x==0 || y == 0 || x == m-1 || y == n-1){ // Check if the point is an exit. 
                            return dist + 1;
                    }
                    maze[x][y] = '+';
                    q.push({x,y,dist+1});

                }
            }
        }

        


        return -1;
    }
};