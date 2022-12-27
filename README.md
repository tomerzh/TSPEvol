
<html>
 <body>
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
   <p>
   We think about this problem as collection of two-dimensional coordinates in the first quarter of the x, y axis. Our data structures use the following:<br>
   <strong> Genotype </strong> – We represented a route with vector, while each element is City object with two coordinates x, y. The salesman must visit        every city once except for the first city, and he can go to every city meaning that all cities are connected. 
   The vector is permutation of the given cities, the first element is the starting point and the ending point, the route is from city [i] to city [i+1].<br>
   First generation – The script can handle two scenarios:
   •	The user defines the vector of the cities, and the script creates random permutation of the vector as many times as the user defines.
   •	The user doesn’t define a specific vector, so the script generates a random vector of cities and then creates random permutation of the vector.<br>
   Fitness evaluation – The fitness will be defined as the sum of distances between the cities based on the order defined in the genotype. Best fitness will      be defined as the minimal one.<br>
   Selection – We used tournament selection, taking 4 individuals and choosing the one with the highest fitness.<br>
   Crossover – We divide the population into pairs and each pair represent parents. 
   For a given probability we randomly choose start index and end index for the first parent and take the subset [start : end]. 
   Then, we go through the second parent vector and check every element, if the element is included in the subset we move on, else, we append it to the          subset. 
   We do it to maintain the fact that the vector is a permutation of the cities.
   We do the same operation for the second parent, and after the crossover we have two new individuals for the next generation.<br>
   Mutation – After the crossover, we take each new individual with probability of 0.1 (or anything the user wants), we randomly choose two indexes in the        individual and swap them, making a different permutation.
    </p>
  </body>
 
 </html> 


