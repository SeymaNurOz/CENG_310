# CENG_310
Algorithms and  Data Structures in Python/ 2021-2022 Spring

**Textbook** Goodrich, Tamassia and Goldwasser, Data Structures and Algorithms in Python, Wiley, 2013

## PA1/

**Task1**

A stone is attached to a string and rotated with the help of the string in a horizontal circle of radius. In
this task, you are given the weight of the stone (m), the speed of the string (v), and the radius of the
horizontal circle (r) as arguments to the function tensionCalculator(m, v, r). Return the tension applied
to the string. You can use the following formula to calculate the tension in the string:

Tension = m ∗ v^2/r 

Specifications:
- The arguments will be in the following order: weight (float), speed (float) and radius (float).
- The return value will be a float.
- You cannot use conditional statements, loops, etc.
- Your function must have the same name and must preserve the order of arguments for us to grade
without any trouble

Sample Input:
> tensionCalculator(3.0, 5.0, 2.0)

Sample Output:
37.5

**Task 2**

In this task, you need to define a function named deleteConsecutiveSimilar(integerList) which takes list of
lists that contains integers. In the function you need to delete consecutive lists if both lists share at least
one common integer. This procedure should continue until there is no two consecutive lists that share a
common element. The function should return the remaining list.

For Example:
- If input list is [[2,5,10],[2,-1],[3]]
- The lists [2,5,10] and [2,-1] gets eliminated
- Input list becomes [[3]]
- If input list is [[2,5,10],[7,-1],[3,-1],[2,0]]
- In the first step lists [7,-1] and [3,-1] gets eliminated
- In the second step lists [2,5,10] and [2,0] gets eliminated
- Input list becomes []
- If input list is [[2,5,10],[7,-1],[3,-1],[2,0],[-5,0]]
- Input list becomes [[2,5,10]]

**Task 3**

In this task, you will modify a txt file which contains information about employees. The file will consist of
a unique ID number, Name, Surname, Job, and Age fields for each person. You will implement a function
named modifyTxt(filename, mode, id, field, newValue) where

- filename is the name of the file to be modified
- mode is either "update" or "delete"
- id is a unique integer value that allows you to distinguish different entries in the file
- field(optional, required only for update operation) is the field that needs to be changed
- newValue(optional, required only for update operation) is the value that will be replaced with the
field’s old value

When a delete is encountered you need to delete that person’s information altogether. In contrast updates
will be done for individual fields. For Example assume we have the following "simplefile.txt" file:
- 12 Ali Do˘gru Manager 25
- 24 Veli Yanlı¸s Secretary 29
- 30 Selami Selam Intern 20

After we call
> modifyTxt("simplefile.txt", "update", 12, "age", 26) and

> modifyTxt("simplefile.txt", "delete", 30) the file becomes

- 12 Ali Do˘gru Manager 26
- 24 Veli Yanlı¸s Secretary 29

Specifications:
- Delete operation will not be called for non existent ID numbers
- Your function does not need to return anything, however, you need to rewrite the changes into the
file
- Every field of a person will be separated with a single white space character
- Every person entry will be separated with a newline character
- After updates you must preserve the white spaces and newlines
- Your function must have the same name and must preserve the order of arguments for us to grade
without any trouble

##PA2/ Stacks and Queues

**1 Implementation of Stack**

You need to implement your stack as a class with a member variable(a container type, i.e list) and member
functions. You will initialize the stack as:

myStack = Stack()

Your Stack class will have the following member functions:
- __init__(): A function that initializes the stack object.
- push(element): inserts a particular element into the stack.
- pop(): removes element from the top of the stack and returns the element.
- top(): returns the element that is at the top of the stack without removing the element.
- isempty(): return whether the stack is empty or not. Returns True when the stack is empty, False
otherwise.


**2 Implementation of Queue**
You need to implement your queue as a class with a member variable(a container type, i.e list) and member
functions. You will initialize the queue as:

myQueue = Queue()

Your Queue class will have the following member functions:
- __init__(): A function that initializes the queue object.
- enqueue(element): inserts a particular element into the stack.
- dequeue(): removes element from the front of the queue and returns the element.
- front(): returns the element that is at the front of the queue without removing the element.
- isempty(): return whether the queue is empty or not. Returns True when the queue is empty, False
otherwise.

**3 Programming Task**

In this task, you will use the data structures from above to solve a problem. An unnamed driver in an
unnamed city is driving a car in a grid like area. The driver needs to reach to a destination by finding the
correct path yet some of the paths are surrounded with dead ends. Your job is to find a path that starts
from a position and ends with the desired position. If such a path exists you need to print that path,
otherwise print "Path not found".

*3.1 Specifications*

- Grid will be a 2-D array where each position (i,j) will be either 1 or 0 with 1 denoting a valid path
and 0 denoting an invalid path.
- Coordinate of the top left corner of the grid will be (0,0) and bottom right corner will be (n-1,n-1)
where n is height and width of the grid.
- The car can move in 4 positions: up, down, right and left.
- There can be more than 1 possible paths, however, to be consistent you should explore in the order
of down, right, up and left respectively.
- Recursion based solutions that do not use stack or queue will not be accepted. Your algorithms
must be based on these data structures.
- If there is not a path you need to print "Path not found" otherwise print the path from the start to
the end by giving the coordinate of each visited block. You should print each point as a list with
two coordinates such as [xCoord, yCoord].
- You will implement a function pathFinder(grid, startX, startY, endX, endY).

* startX: vertical coordinate of starting point.
* startY: horizontal coordinate of starting point.
* endX: vertical coordinate of ending point.
* endY: horizontal coordinate of ending point.

Figure 1: Grid Example
3.2 Example Grid
In Figure 1 you can see an example grid structure. In this grid, start position is (2,2) and end position is
(0,0). This grid will be given to you as:
grid = [[1,1,1,0,1],
[1,1,0,0,1],
[1,0,1,1,1],
[1,0,0,1,0],
[1,1,1,1,0]]
3.3 Sample I/O
Input:
>>> pathFinder([[1,1,1,0,1],
[1,1,0,0,1],
[1,0,1,1,1],
[1,0,0,1,0],
[1,1,1,1,0]], 2, 2, 0, 0)
Output:
[2,2]
[2,3]
[3,3]
[4,3]
[4,2]
[4,1]
[4,0]
[3,0]
[2,0]
3
[1,0]
[1,1]
[0,1]
[0,0]
Notice how the ordering of the moves impacts the solution.
