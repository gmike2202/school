4. Prove that the sum of two odd numbers $n_1$ and $n_2$ is even.
7. Prove that every binary number n that ends in 0 is even.
10. Prove, or find a counterexample: the difference of two consecutive perfect squares is odd
17. At Chicago O’Hare International Airport, there are an average of 1,185 direct flights per day (source: http://www.w3.org/1999/xlink). Prove that at least two of these flights must take off within 90 seconds of each other.  

1. Given any list of 25 numbers, each of which has at most five digits,
two subsets of the list have the same sum. Again, intuition first:
Any one of the numbers is less than 100,000, so the sum of all 25 of them is
less than 2,500,000. Therefore any subset of the 25 numbers also has sum less
than 2,500,000. (We will ignore the empty set, even though it is a subset of the
numbers.)
To find the lowest sum possible, consider the case of a subset that’s just the
number 00001. It has sum 1. Therefore, there are at most 2,500,000 different
possible sums the subsets could have.
Now, how many subsets are there? We know this from Theorem 1.5.2—there
are 2^25 = 33,554,432 possible subsets. (Actually, because we have ignored the
empty set, we are only considering 2^25
− 1= 33,554,431 subsets.)
There are way more subsets than sums, so two of the subsets must have the
same sum. In terms of pigeons, we represent the subsets by pigeons and the
subset-sums by pigeonholes; a pigeon flies to the pigeonhole labeled with its
subset’s sum.
 a. Does a list of distinct five-digit numbers of length 20 have the property that there must be two subsets of the list with the same sum
 b. What is the smallest list of distinct five-digit numbers such that there must be two subsets of the list with the same sum?

2. Prove that if n is any integer, then $3n^3 + n + 5$ is odd. (Suggestion: do one case for n odd and one case for n even.)

