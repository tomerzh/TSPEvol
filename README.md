
<html>
   <h1>Evolutionary Algorithms - Mini Project</h1>
   The Traveling Salesman Problem (TSP) is a classic problem in computer science and operations research.
   It involves finding the shortest possible route that visits a given set of cities and returns to the starting city.

   <h3>Problem Description:</h3>

   The TSP has many practical applications, including planning delivery routes, scheduling service technicians, and designing telecommunications networks.
   In the TSP, a salesman must visit a set of cities, each represented by a node in a graph.
   The salesman starts at one of the cities and must visit all the other cities exactly once before returning to the starting city.
   The goal is to find the shortest possible route that satisfies these constraints.
   The TSP is an NP-hard problem, meaning that it is very difficult to solve exactly, especially for large sets of cities.
   As a result, a variety of heuristics and approximation algorithms have been developed to find near-optimal solutions to the TSP.
   These approaches often involve finding a suboptimal solution and then improving upon it until a satisfactory solution is found.

   <h3>Solution:</h3>
   The problem is a minimization problem, therefore we used an evolutionary algorithm to solve it,
   using the <a href="https://github.com/EC-KitY/EC-KitY">EC-Kity</a> <img src="https://avatars.githubusercontent.com/u/95233107?s=200&v=4" alt="EC-Kity"        width="30" height="30" align="right"> library.
   The algorithm takes a population of permutations of the cities we want to find the shortest path between, represents by a linear vector (GA) and calculates    the optimal distance for X generations (X is choiceable).

   <h3>Implementation Details:</h3>
   We think about this problem as collection of two-dimensional coordinates in the first quarter of the x, y axis. Our data structures use the following:<br>
   <b>Genotype –</b> 
   We represented a route with vector, while each element is City object with two coordinates x, y. The salesman must visit every city once except for the        first city, and he can go to every city meaning that all cities are connected. 
   The vector is permutation of the given cities, the first element is the starting point and the ending point, the route is from city [i] to city [i+1].<br>
   <b>First generation –</b> The script can handle two scenarios:<br>
   •	The user defines the vector of the cities, and the script creates random permutation of the vector as many times as the user defines.<br>
   •	The user doesn’t define a specific vector, so the script generates a random vector of cities and then creates random permutation of the vector.<br>
   <b>Fitness evaluation –</b> The fitness will be defined as the sum of distances between the cities based on the order defined in the genotype. Best fitness    will be defined as the minimal one.<br>
   <b>Selection –</b> We used tournament selection, taking 4 individuals and choosing the one with the highest fitness.<br>
   <b>Crossover –</b> We divide the population into pairs and each pair represent parents. 
   For a given probability we randomly choose start index and end index for the first parent and take the subset [start : end].<br>
   Then, we go through the second parent vector and check every element, if the element is included in the subset we move on, else, we append it to the          subset. 
   We do it to maintain the fact that the vector is a permutation of the cities.<br>
   We do the same operation for the second parent, and after the crossover we have two new individuals for the next generation.<br>
   <b>Mutation –</b> After the crossover, we take each new individual with probability of 0.1 (or anything the user wants), we randomly choose two indexes in    the individual and swap them, making a different permutation.<br>
   
   <h3>Results:</h3>
   We wanted to give the algorithm the best parameters for a better fitness in the end of the run.<br>
   After an operation of trial and error, we discovered that the best parameters are:<br>
•	Population size – The size of the population in every generation is 100, meaning we are using 100 individuals (routes of cities) in every generation.<br>
•	Number of generations – The number of generations in one run is 100.<br>
•	Number of iterations – We run the algorithm 100 times, to try and understand what the best fitness is out of all the runs, if there is a lower bound to the best fitness and what is the average fitness.<br>
•	We tried two different crossover patterns, more about that in the next section.<br>
•	We used 0.8 probability for a crossover and 0.1 probability for a mutation.<br>
We tried our algorithms on 15 different cities with the following (X, Y):<br>
(30, 17), (22, 1), (300, 45), (423, 54), (51, 26), (6, 7), (7, 8), (81, 19), (94, 10), (3, 250), (1, 666), (244, 1234), (522, 2145), (0, 21), (222, 1113).
After the run for 2 different crossovers, we collected the data, and the results are as follows:<br>
Single point crossover – A crossover point on the parent organism string is selected. All data beyond that point in the organism string is swapped between the two parent organisms.<br>
The results for single point crossover showed that the best fitness for this crossover is 4765.3 and the average fitness is 4948. We saw that a lot of the runs gave the same fitness which was 4765.3 with the same permutation. You can see the results in the graph below:<br>


Two-point crossover - In two-point crossover, two crossover points are picked randomly from the parent chromosomes. The bits in between the two points are swapped between the parent organisms.<br>
The results for two-point crossover showed that the best fitness for this crossover is 4765.3 and the average fitness is 4941. We saw that a lot of the runs gave the same fitness which was 4765.3 with the same permutation. You can see the results in the graph below:<br>
 </html> 


