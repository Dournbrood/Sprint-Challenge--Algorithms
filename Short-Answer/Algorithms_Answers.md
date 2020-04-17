#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a) O(n) - The loop itself is n^3 but the iterator is being increased by n^2. We do (n^3)/(n^2) to get O(n^1) or just O(n)

b) O(n log(n)) - There are two loops iterating over N here - one is nested in the other. The inner loop is iterating over n as well, with the iterator itself growing exponentially. With an inner and outer loop bound to iterate over most of n, it's n log(n)

c) O(n) - This recursive function invokes in a straight tree, no splitting or merging here. `bunnies` is evaluated n times, no more, no less.

## Exercise II

1. Start on the floor `n/2`.
2. Drop an egg.
3. If you are 1 floor above where the last egg dropped was not broken, and the egg dropped on this floor breaks, you are at floor `f`.
4. If you are 1 floor below where the last egg dropped broke, and the egg on this floor does NOT break, you are 1 floor below floor `f`.
5. If the egg breaks, go to the floor halfway between your current level and the last floor on which an egg did not break when dropped, OR floor 0 if all eggs have broken.
6. If the egg does not break, go to the floor halfway between your current level and the last floor on which an egg broke when dropped, OR floor `n` if no eggs have broken.
7. Go to step 2.

The runtime complexity of the above pseudo-algorithm is O(log n) since the number of floors to evaluate becomes halved with each iteration/recursion.
