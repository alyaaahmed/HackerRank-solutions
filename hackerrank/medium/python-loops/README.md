# Loops

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

<sub>Check [Tutorial](https://www.hackerrank.com/challenges/python-loops/tutorial) tab to know how to to solve.</sub>  

**Task**  
The provided code stub reads an integer, $n$, from STDIN. For all non-negative integers $i \lt n$, print $i^2$.  

**Example**  
$n = 3$  

The list of non-negative integers that are less than $n = 3$ is $[0, 1, 2]$.  Print the square of each number on a separate line.

<pre>
0
1
4
</pre>




**Input Format**

The first and only line contains the integer, $n$. 

**Constraints**

$1 \le n \le 20$  

**Output Format**

Print $n$ lines, one corresponding to each $i$.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-07T10:04:28.005Z  

```py
if __name__ == '__main__':
    n = int(input())
    if n >= 1 and n <=20 :
        for i in range(n) :
            print (i**2)
    else  :
        print("your Constaints is n>=1 and n<=20 ") 
        print("please Renter our number ") 
        

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/python-loops/problem)