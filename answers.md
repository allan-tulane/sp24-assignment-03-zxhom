# CMPS 2200 Assignment 3
## Answers

**Name:** Zach Hom

Place all written answers from `assignment-03.md` here for easier grading.

**1a)** Starting with the largest feasible value of k for this economy, my greedy criteria would be to find the maximum k value from the possible $2^k$ coin solutions such that 2^k <= N; then, (N - 2^k) until N <= 1, decrementing k each time without revisiting higher k values. (Each possible coin value of $2^k$ will be considered only once.)

**1b)** The greedy choice is the maximum k such that the coin value $2^k$ <= N, decrementing N accordingly each time. Each optimal substructure considers one solution for k from the set of potential solutions that will not be revisited, breaking down the problem into smaller parts at the sublink level to achieve the overall optimal solution.

**1c)** Since each possible coin value of $2^k$ is considered only once and N is decremented each time by a denomination of 2, W = O(log(n)); however, because these k values cannot be evaluated in parallel, S = O(log(n)).

**2a)** Let's say the denominations in Fortuito are $1, $5, $8 and let's assume N = $15. Using the greedy algorithm of Geometrica, we find that the "optimal" solution output is, in fact, not optimal.
Geometrica Solution: $8, $5, $1, $1 --> 4 coins
Actual Optimal Solution: $5, $5, $5 --> 3 coins

**2b)** The optimal substructure property would be to run all possible combinations by evaluating the highest possible denomination and the second highest denomination. At each level, you have two children nodes considering the parent denomination once again — reducing N accordingly — and the next highest denomination. The left side of the tree represents a Geometrica-type approach using each denomination once and decrementing accordingly. The right side of the tree represents solely using the highest possible denomination without considering smaller value denominations. Each previously calculated substructure is then stored into an array. The optimal substructure paths are the ones where N evaluates to 0. This does not follow the greedy algorithm because all possibilities are considered not just local optimal solutions at each level.

**2c)** Using a top-down memoized dynamic approach, we would store each substructure into an array to avoid recomputing past considerations between denominations. Since redundancy is eliminated but the serial nature of the algorithm is conserved, the Work = O(nw) = O(n) and the Span = O(n) where span is the longest path in the DAG.


