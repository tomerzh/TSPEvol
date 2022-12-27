
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
using the <a href="https://github.com/EC-KitY/EC-KitY">EC-Kity</a> <img src="https://avatars.githubusercontent.com/u/95233107?s=200&v=4" alt="EC-Kity" style="float:right;width:30px;height:30px;"> library.

The algorithm takes a population of permutations of the cities we want to find the shortest path between, represents by a linear vector (GA) and calculates the optimal distance for X generations (X is choiceable).

