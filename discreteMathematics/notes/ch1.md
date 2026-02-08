# Chapter 1: Counting and Proofs

## 1.3 The Sum and Product Principles

* The sum principle - The number of elements in a finite number of disjoint finite sets A, B, ... , N is the sum of their sizes |A| + |B| + ... + |N|

* The product principle - The number of elements in the Cartesian product of a finite number of finite sets $A \times B \times ... \times N$ is the product of their sizes $|A| \cdot |B| \cdot...\cdot|N|$

## 1.4 Preliminaries on Proofs and Disproofs

* definition - a precise statement of the meaning of a term
* conjecture - a statement proposed to be true and made on the basis of intuition and/or evidence from examples
* theorem - a statement that can be demonstrated to be true
* proposition - theorem offered (proposed) or smaller theorem
* lemma - small theorem, usually stated and proven in the process of proving a regular sized theorem
* corollary - statement whose truth follows directory from a related theorem
* proof - justification of the truth of a statement using reasoning so rigorous that the argument compels assent
* an integer n>1 is prime if the only positive divisors of n are n and 1.
  * By definition, 3 is prime because $3 \times 1 = 1 \times 3 = 3$, there is no possible factorization into positive integers.
* A number is even if it is evenly divisible by 2. Equivalently, a number m is even if m = 2k for some integer k. A number m is odd if m=2k + 1 for some integer k.
  * The number 64 is even because $64 = 2 * 32$. However, the number 3 is not even because $3 = 2 * \frac{3}{2}$ and $\frac{3}{2}$ is not an integer, but $3 = 2 * 1 + 1$ so the number 3 is odd.
* A binary number is a number expressed using only digits 0 and 1, with counting proceeding as 1, 10, 11, 100, 101, 110,... and with places representing powers of two, increasing to the left and decreasing to the right.
  * Thus, the number 64 is not a binary because it uses digits other than 0 and 1, but 101 and 101011.101 can be binary numbers or decimal numbers. The binary number 101 represents $2^2 + 0 + 2^0 = 5$ in decimal notation, and the binary number 101011.101 represents $2^5 + 0 + 2^3 + 0 + 2^1 + 2^0 + 2^{-1} + 0 + 2^{-3} = 43.625$ in decimal notation.

**Template for a direct proof:**
1. Restate the theorem in the form if (conditions) are true, then (conclusion) is true. Most, but not all, theorems can be restated this way.
2. On a scratch sheet, write assume (conditions) are true or suppose (conditions) are true.
3. Take some notes on what it means for (conditions) to be true. See where they lead.
4. Attempt to argue in the direction of (conclusion) is true.
5. Repeat attempts until you are successful.
6. Write up the results on a clean sheet, as follows.
   * Theorem: (State theorem here.)
   * Proof: Suppose (conditions) are true
   * (Explain your reasoning in a logically airtight manner, so that no reader could question your statements.)
   * Therefore, (conclusion) is true. (Draw a box or check mark or write Q.E.D --the abbreviation of quod erat demonstrandum, Latin for "which was to be demonstrated"--to indicate that you're done)

## 1.5 Pigeons and Correspondences

***Theorem 1.5.2: A set with n elements has $2^n$ subsets***

**How to Apply the pigeonhole principle:**
  1. Figure out what represents the pigeons.
  2. Figure out what represents the pigeonholes
  3. Figure out how pigeons correspond to holes
* The generalized pigeonhole principle - If you have more than k times as many pigeons than pigeonholes, then if every pigeon flies into a hole, there must be a hole containing more than k pigeons.
