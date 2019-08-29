# Threading, Event Loop and multiprocessing

Cpu bound and I/O Bound programs

For I/O bound programs if a thread is waiting for io it is switched out and comes back after IO is completed, hence there is overlapping IO which improves the speed

# Time and Space Complexity


Big O time is the language and metric we use to describe the efficiency of algorithms

Sometimes, there are more than one way to solve a problem. We need to learn how to compare the performance different algorithms and choose the best one to solve a particular problem. 

Time complexity of an algorithm quantifies the amount of time taken by an algorithm to run as a function of the length of the input. Similarly, Space complexity of an algorithm quantifies the amount of space or memory taken by an algorithm to run as a function of the length of the input.

n = 10 
for i in range(10):
    print(i)
	
T = O(n) here n = 10

S = O(1)

  

n = 10

out = []

for i in range(10):

​	out.append(i)

print(out)

T = O(n)

S=O(n)

#### Properties

O(2n) = O(n)

O(n^2+n) = O(n^2)



for i in range(n):

​	print(i)

for j in range(n):

​	print(j)

O(2n) = O(n)



for i in range(n):

​	for j in range(n):

​		print(i, j)

O(n^2)



O(log(n)) example

Binary Search

a = [1, 3, 5, 7, 10, 34, 67, 90, 153]

Find 5 in a

Find 5 in [1,3,5,7]

T(n) = T(n/2) + 1 = T(n/4) + 2 = T(n/8) + 3 .... = T(1) + log(n) = O(log(n))



def f(n):

​	return f(n-1) + f(n-1)

T(n) = 2T(n-1) = 4T(n-2) = ..... 2^nT(1) = O(2^n) 