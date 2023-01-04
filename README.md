
<html>
   <h1>Evolutionary Algorithms - Mini Project</h1>
   <h3>Intro:</h3>
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
   using the <span><a href="https://github.com/EC-KitY/EC-KitY">EC-Kity</a> <img src="https://avatars.githubusercontent.com/u/95233107?s=200&v=4" alt="EC-Kity"        width="30" height="30"></span> library.<br />
   The algorithm takes a set of cities we want to find the shortest path between, represents by a linear vector (GA) and calculates the optimal route for X generations (X is choiceable).

   <h3>Implementation Details:</h3>
   We think about this problem as collection of two-dimensional coordinates in the first quarter of the x, y axis. Our data structures use the following:<br>
   <b>Genotype –</b> 
   We represented a route with vector, while each element is City object with two coordinates x, y.<br />
   The salesman must visit every city once except for the first city, and he can go to every city meaning that all cities are connected.<br />
   The vector is permutation of the given cities, the first element is the starting point and the ending point, the route is from city [i] to city [i+1].<br />
   <b>First generation –</b> The script can handle two scenarios:<br>
   •	The user defines the vector of the cities, and the script creates random permutation of the vector as many times as the user defines.<br>
   •	The user doesn’t define a specific vector, so the script generates a random vector of cities and then creates random permutation of the vector.<br>
   <b>Fitness evaluation –</b> The fitness will be defined as the sum of distances between the cities based on the order defined in the genotype. Best fitness    will be defined as the minimal one.<br>
   <b>Selection –</b> We used tournament selection, taking 4 individuals and choosing the one with the highest fitness.<br>
   <b>Crossover –</b> We divide the population into pairs and each pair represent parents.<br /> 
   For a given probability we randomly choose start index and end index for the first parent and take the subset [start : end].<br>
   Then, we go through the second parent vector and check every element, if the element is included in the subset we move on, else, we append it to the          subset.
   We do it to maintain the fact that the vector is a permutation of the cities.<br>
   We do the same operation for the second parent, and after the crossover we have two new individuals for the next generation.<br>
   <b>Mutation –</b> After the crossover, we take each new individual with probability of 0.1 (or anything the user wants), we randomly choose two indexes in    the individual and swap them, making a different permutation.<br>
   
   
   <h3>Using Our Solver:</h3>
   To use our TSP solver, please follow the following steps: <br>
    <details open>
<summary>Install</summary>

Clone repository and install [requirements.txt](https://github.com/ultralytics/yolov5/blob/master/requirements.txt).

```bash
git clone https://github.com/tomerzh/TSPEvol.git  # clone
cd TSPEvol
pip install -r requirements.txt  # install
```
</details>
 
•	You can change the coordinates of each city however you want, the only restriction is the value can not be larger than the maximum integer. Another option is to ignore the given vector of cities and the script will generate random cities for the vector. <br>
•	Feel free to change the max_generation and population_size variables to any positive integer. <br>
•	Run main.py. <br />
•  The results will be presented in a data.csv file with all the best fitness results of your runs, plus the best fitness of them all with the exact route. <br>

   
   
   <h3>Results:</h3>
   We wanted to give the algorithm the best parameters for a better fitness in the end of the run.<br>
   After an operation of trial and error, we discovered that the best parameters are:<br>
   •	<b>Population size –</b> The size of the population in every generation is 100, meaning we are using 100 individuals (routes) in every generation.<br>
•	<b>Number of generations –</b> The number of generations in one run is 100.<br>
•	<b>Number of iterations –</b> We run the algorithm 100 times, to try and understand what the best fitness is out of all the runs, if there is a lower bound to the best fitness and what is the average fitness.<br>
•	We tried two different crossover patterns, more about that in the next section.<br>
•	We used 0.8 probability for a crossover and 0.1 probability for a mutation.<br>
We tried our algorithms on 15 different cities with the following (X, Y):<br>
<b>(30, 17), (22, 1), (300, 45), (423, 54), (51, 26), (6, 7), (7, 8), (81, 19), (94, 10), (3, 250), (1, 666), (244, 1234), (522, 2145), (0, 21), (222, 1113)</b>.<br>
In the process of checking the best parameters we tried to run the algorithm with a small size of pipulation in each generation. We tried the algorithm with population size of 10, and found out that there is a big defference between defferent runs meaning that the standart deviation is big the average fitness was 5617.<br />
In the graph below we can see the results for a two-point crossover with population size 10: <br />
   <br />
   <img src="https://github.com/tomerzh/TSPEvol/blob/main/plots/twopoint_10_pap.png?raw=true" alt="tpc_10pop"    width="800" height="400"><br />
Now for the results of the experiment with population size of 100: <br />
After the run for 2 different crossovers, we collected the data, and the results are as follows:<br>
<b>Single point crossover –</b> A crossover point on the parent organism string is selected. All data beyond that point in the organism string is swapped between the two parent organisms.<br>
The results for single point crossover showed that the <b>best fitness for this crossover is 4765.3</b> and the <b>average fitness is 4948</b>.
We saw that a lot of the runs gave the same fitness which was 4765.3 with the same permutation. You can see the results in the graph below:<br />
<br />
<img src="https://github.com/tomerzh/TSPEvol/blob/main/plots/single.jpg?raw=true" alt="spc"    width="800" height="400"><br />
   
<b>Two-point crossover -</b> In two-point crossover, two crossover points are picked randomly from the parent chromosomes. The bits in between the two points are swapped between the parent organisms.<br>
   The results for two-point crossover showed that the <b>best fitness for this crossover is 4765.3</b> and the <b>average fitness is 4941</b>. We saw that a lot of the runs gave the same fitness which was 4765.3 with the same permutation. You can see the results in the graph below: <br />
<br />
<img src="https://github.com/tomerzh/TSPEvol/blob/main/plots/two.jpg?raw=true" alt="tpc"    width="800" height="400"><br />
   
   <h3>Conclusion:</h3>
   We expected that there will be a difference between the two crossovers, but in the end, both returned the same route with the same fitness.<br />
   The best route returned from the two crossovers: <br />
   <b> Start point (244, 1234) -> (522, 2145) -> (423, 54) -> (300, 45) -> (94, 10) -> (81, 19) -> (51, 26) -> (30, 17) -> (22, 1) -> (7, 8) -> (6, 7) -> (0, 21) -> (3, 250) -> (1, 666) -> (222, 1113) -> (244, 1234) end point.</b> <br />
   More than that, we discovered that a lot of the different runs returned the same route which is the best route in the end. <br />
We assume that this fitness is the lower bound for this input and the algorithm can’t do better than that. The reason for that can be two options, the first is that this route is the best route there is for this input, and the second option is our crossover method is stuck and can’t pass this lower bound fitness.<br />
The best route is represented by the graph below and we believe it’s the best route there is for this input:<br />
   <br />
   <img src="https://github.com/tomerzh/TSPEvol/blob/main/plots/routes.jpg?raw=true" alt="route"    width="800" height="400"><br />  
   
   <h3>Summary:</h3>
We wanted to solve the TSP problem which is considered a NP-Hard problem.<br/ >
In order to resolve the TSP problem we used evolutionary algorithm using linear vector permutation with 2 different crossovers (single-point and two-point) to examine the best fitness and check if there is a big difference in the results between the two methods.<br />
We used an input containing 15 different cities and ran different kinds of runs based on the size of the population, the number of generations, and the number of iterations.<br />
We conclude that, the most significant difference was between the population parameters.<br />
As a result, we obtained an approximate lower bound considering input that was pointed by two different methods and they didn't diverge much on average, which is quite amazing.<br />
We strongly believe this method of solution can achieve great results in such problems and can serve multiply industries to save money, time and resources.<br />
An airline delivery company is an example of such a industry. <br />

   
   <h3>Citation:</h3>
    </html> 
    
```
@misc{eckity2022git,
    author = {Sipper, Moshe and Halperin, Tomer and Tzruia, Itai and  Elyasaf, Achiya},
    title = {{EC-KitY}: Evolutionary Computation Tool Kit in {Python}},
    year = {2022},
    publisher = {GitHub},
    journal = {GitHub repository},
    howpublished = {\url{https://www.eckity.org/} }
}
```



