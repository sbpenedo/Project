Right now maps like Google Maps or Apple Maps will tell you where to go in the order that you enter the buildings but it won't give you an optimal path if it doesn't matter
what order you need to visit buildings. This program implements Dijkstra's algorithm and looks at all permutations and finds the most efficient path from your starting point
to all subsequent buildings.

This program accepts a file called buildings.txt that is read in. There is an example file with the UT campus but any user can insert any buildings to calculate their own walktimes
The first line specifies the number of vertices (buildings) in the graph.
Each subsequent line represents an edge, with three comma-separated values:
  1. Building 1 name
  2. Building 2 name
  3. Weight of the edge between the two buildings (time in minutes)
If a building is entered that is not in the list the user will be prompted to re-enter a building name

The output for this program is the optimal travel path which shows the path that the user will travel to visit all buildings. This means that the output contains the
building names entered as well as buildings in between the original buildings that are passed throughout the journey. Additionally the program will also output the total
travel time to visit all buildings.
