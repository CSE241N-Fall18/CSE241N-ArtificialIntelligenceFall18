                              Assignment 7

----------------------------------------------------------------------------
         Artificial Intelligence (CSE-241N), IIT (BHU) Varanasi
                              4th Apr 2018
----------------------------------------------------------------------------

In this assignment, you will implement the following guided search algorithms.

- Hill climbing search
- Best first search
- Beam search
- A* search

Working files:
--------------
You will be restricted to work with 'search.py’. YOU ARE NOT TO MODIFY ANY CODE WRITTEN OUTSIDE OF '# BEGIN YOUR CODE #' and '# END OF YOUR CODE #' MARKERS. The scorer code we use may depend on some part of that code making any changes to which might hamper your score.

Your submission will be the code in 'search.py'.

Test Cases:
-----------
Tests are defined in the file 'test.py'. You may test with your own test cases. Marks will be assigned based on private test cases. Ensure your code works.

To run tests, execute in the shell:

python3 test.py

About the Code:
---------------
For further testing, you might want to look at how the graph is implemented. You can do that by looking into 'graph.py'. In 'util.py', check out how a random graph is generated. On the interpreter, create new graphs and look at your generated paths to manually see whether they are correct.

Example:
        width-+ +-Height   +----List of rectangular bounding boxes, each having
              | |          |    two coordinates, specifying an out-of-bounds region
              v v          v
>>> g = Grid(14, 17, [((2, 1), (6, 1)), ((3, 4), (5, 5)), ((7, 3), (8, 4)), ((7, 3), (8, 6)), ((7, 6), (8, 11)), ((7, 9), (10, 12)), ((8, 9), (8, 12))])
>>> print(g)
. . . . . . . . . . . . . . . . . 
. . . . . . . # # # # . . . . . . 
. . . . . . . # # # # . . . . . . 
. . . . . . . # # # # . . . . . . 
. . . . . . . # # # # . . . . . . 
. . . . . . . # # . . . . . . . . 
. . . . . . . # # . . . . . . . . 
. . . . . . . # # . . . . . . . . 
. . . # # # . # # . . . . . . . . 
. . . # # # . # # . . . . . . . . 
. . . . . . . # # . . . . . . . . 
. . . . . . . . . . . . . . . . . 
. . # # # # # . . . . . . . . . . 
. . . . . . . . . . . . . . . . .
>>> g.isOOB((3, 4))
True
>>> g.neighboursOf((2, 0))
[(3, 0), (1, 0)]

The '.' are valid regions of the graph. The '#' are blocked regions, i.e they can't be crossed. The graph is indexed by coordinated starting from (0, 0) to (width - 1, height - 1) with the origin being bottom-left.

The 'Grid.isOOB' method returns whether a coordinate is inside the grid but outside the out-of-bounds region. The 'Grid.neighboursOf' method returns the valid neighbours of a given coordinates. 

Actual Work:
------------
- Complete the functions related to search according to the given algorithms. Fill in the definitions of the functions 'searchHillClimbing', 'searchBeam', 'searchBestFirst', and 'searchAStar' in 'search.py'.

Steps:
------
0. Open 'search.py' and 'graph.py' in your favorite text editor.
1. Edit it following the markers and comments -> search.py.
2. Test for correctness by running tests. See 'Test Cases' section for details.
3. You need to submit the files: 'search.py'. Do that by running './submit.sh YOUR_ROLL_NO' from the assignment folder.
(4. ???)
(5. Profit)

IMPORTANT:
----------
We will test the correctness of your implementation by looking at the generated paths to the destination and checking whether at each step the decision was made in accordance with the policy of the target algorithm or not. Do not presume that you can implement only one algorithm and call this function for all other cases. Each algorithm is subtly different and this will reflect in the generated paths.

All the best.