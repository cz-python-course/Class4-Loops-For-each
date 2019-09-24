# Class4-Loops-For-each
- [Class4-Loops-For-each](#class4-loops-for-each)
  - [Introduction to loops](#introduction-to-loops)
  - [For each Loop](#for-each-loop)
    - [Understanding the for loop](#understanding-the-for-loop)

## Introduction to loops
Imagine the following exercise:

Develop a program that asks the number of children the user has. Then asks the name of every child.

How would you implement this code? 

To solve problems like this, we use *Loops*. A loop allows us to repeat the execution of a block of code for a finite, or infinite number of times.

## For each Loop
We are going to use a *for each* loop to execute a block of code a certain number of times. This loop work in a slight more complex way, that we are going to see in details in the next class. For now, we will use it just to execute a block of code for a defined number of times.

### Understanding the for loop
```python
for counter in range(3):
    print('hello world')
```
Let's break the first line into small pieces, so we can understand everything that is happening.
- **range(3)**: creates a numeric array, that contains 3 values (0,1,and 2).
- **for counter in**: Declares a variable *counter*, that will only exist inside this block of code. 

The variable *counter* will get the fist value from the range function, which is *0*. when we reach the end of the block of code, the value of the *counter* will change for the next value in the range, until we run out of numbers. This means that the loop will be executed three times, in this example.
