# 0x08. Making Change
For the “0. Change comes from within” project, you will tackle a classic problem from the domain of dynamic programming and greedy algorithms: the coin change problem. The objective is to find the minimum number of coins required to make up a given total amount, given a list of coin denominations. This project challenges you to apply your understanding of algorithms to devise a solution that is not only correct but also efficient. Below are the key concepts and resources necessary to complete this project successfully.

Concepts Needed:
Greedy Algorithms:

Understanding how greedy algorithms work and why they are suitable for the coin change problem.
Recognizing the limitations of greedy algorithms and scenarios where they might not provide the optimal solution.
Dynamic Programming:

Basic principles of dynamic programming as a method to solve optimization problems.
The concept of overlapping subproblems and optimal substructure in the context of the coin change problem.
Algorithmic Complexity:

Analyzing the time and space complexity of algorithms.
Striving for solutions with lower complexity to meet runtime constraints.
Problem-Solving Strategies:

Breaking down the problem into smaller, manageable sub-problems.
Iterative vs recursive approaches to dynamic programming.
Python Programming:

Manipulating lists and using list comprehensions.
Implementing functions with efficient looping and conditional statements.

Tasks
0. Change comes from within
mandatory
Given a pile of coins of different values, determine the fewest number of coins needed to meet a given amount total.

Prototype: def makeChange(coins, total)
Return: fewest number of coins needed to meet total
If total is 0 or less, return 0
If total cannot be met by any number of coins you have, return -1
coins is a list of the values of the coins in your possession
The value of a coin will always be an integer greater than 0
You can assume you have an infinite number of each denomination of coin in the list
Your solution’s runtime will be evaluated in this task
