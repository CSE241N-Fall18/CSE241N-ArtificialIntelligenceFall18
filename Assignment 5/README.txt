                              Assignment 3

----------------------------------------------------------------------------
         Artificial Intelligence (CSE-241N), IIT (BHU) Varanasi
                              20th Mar 2018
----------------------------------------------------------------------------

In this assignment, you will implement classes for Logic Programming and implement 
Resolution-Refutation for automatic theorem proving.  

Working files:
--------------
You will be restricted to work with 'logic.py’ and 'knowledge.py'. YOU ARE NOT TO MODIFY ANY CODE WRITTEN OUTSIDE OF '# BEGIN YOUR CODE #' and '# END OF YOUR CODE #' MARKERS. The scorer code we use may depend on some part of that code making any changes to which might hamper your score.

Your submission will be the code in 'logic.py' and 'knowledge.py'.

Test Cases:
-----------
Test cases are defined (hardcoded) in the file 'test.py'. You may test with your own test cases. Marks will be assigned based on private test cases. Ensure your code works.

To run tests see the 'test.py' help as follows:

python3 test.py -h 

Actual Work:
------------
- Complete the functions related to logic programming. Fill in the definitions of the functions 'toCNF' and 'truthValue' in EVERY child of 'Formula' in logic.py.
- Implement the function 'resolutionRefutation' and '__applyResolution' in knowledge.py.

Task 1:
-------
Complete the function 'truthValue' for each child of the 'Formula' class in 'logic.py'. Test this function using the 'printTruthTable' function in 'test.py'. 

Task 2:
-------
Complete the function 'toCNF' for each child of the 'Formula' class in 'logic.py'. Test this function using the 'runCNFTest' function in 'test.py'.

Task 3:
-------
Complete the function 'resolutionRefutation' and '__applyResolution in 'knowledge.py'. Test this function using the 'runResolutionTest' function in 'test.py'.

Steps:
------
0. Open 'logic.py' and 'knowledge.py' in your favorite text editor.
1. Edit it following the markers and comments -> logic.py followed by knowledge.py.
2. Test for correctness by running tests. See 'Test Cases' section for details.
3. You need to submit the files: 'logic.py', 'knowledge.py'. Do that by running './submit.sh YOUR_ROLL_NO' from the assignment folder.
(4. ???)
(5. Profit)

Hint:
-----
The major part of this assignment is implementation. This assignment involves coding complex algorithms with unique corner-cases. We have tried to do as much heavy-lifting as we can, however. Pay attention to in-code comments. Read the starter code already written along with the implementation of tests in 'test.py' so you may get the idea of the overall architecture of the code, our general way of representation and how to use the classes/functions. Play with it on terminal once you finish.

All the best.