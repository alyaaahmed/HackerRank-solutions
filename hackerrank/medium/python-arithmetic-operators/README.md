# Arithmetic Operators

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

<sub>Check [Tutorial](https://www.hackerrank.com/challenges/python-arithmetic-operators/tutorial) tab to know how to to solve.</sub>  

**Task**  
The provided code stub reads two integers from STDIN, $a$ and $b$.  Add code to print three lines where: 
<ol>

<li> The first line contains the sum of the two numbers. </li>  
<li> The second line contains the difference of the two numbers (first - second). </li>  
<li> The third line contains the product of the two numbers. </li>  
</ol>

**Example**  
$a = 3$  
$b = 5$  

Print the following:
<pre>
8
-2
15
</pre>

**Input Format**

The first line contains the first integer, $a$.  
The second line contains the second integer, $b$.  

**Constraints**

$1 \le a \le 10^{10}$  
$1 \le b \le 10^{10}$  
 

**Output Format**

Print the three lines as explained above.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-07T10:02:03.499Z  

```py
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    if a in range(1,10**10) and b in range(1,10**10):
        print(a+b)
        print(a-b)
        print(a*b)
    else:
        print("you are not in range ")    

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/python-arithmetic-operators/problem)