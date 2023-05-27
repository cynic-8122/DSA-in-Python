'''
There are a total of n tasks you have to pick, labeled from 0 to n-1. 
Some tasks may have prerequisites tasks, for example to pick task 0 you have to first finish tasks 1, 
which is expressed as a pair: [0, 1]
Given the total number of n tasks and a list of prerequisite pairs of size m. 
Find a ordering of tasks you should pick to finish all tasks.
Note: There may be multiple correct orders, you just need to return one of them. 
If it is impossible to finish all tasks, return an empty array.

'''

'''
APPROACH:
# Consider this problem to be a graph where this is an directed edge from u to v iff u is a prerequisite for v.
# Now, it will be impossible to order the tasks if the graph contains a cycle.
# Else, a topological sort of the graph will give us the answer.

'''

