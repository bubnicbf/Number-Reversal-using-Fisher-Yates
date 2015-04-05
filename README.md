# Fisher-Yates-shuffle
an algorithm for generating a random permutation of a finite set—in plain terms, for randomly shuffling the set.

The Fisher–Yates shuffle is unbiased, so that every permutation is equally likely. The modern version of the algorithm is also rather efficient, requiring only time proportional to the number of items being shuffled and no additional storage space.

Fisher–Yates shuffling is similar to randomly picking numbered tickets (combinatorics: distinguishable objects) out of a hat without replacement until there are none left.

##Fisher and Yates' original method
The Fisher–Yates shuffle, in its original form, was described in 1938 by Ronald A. Fisher and Frank Yates in their book Statistical tables for biological, agricultural and medical research. Their description of the algorithm used pencil and paper; a table of random numbers provided the randomness. The basic method given for generating a random permutation of the numbers 1 through N goes as follows:

1. Write down the numbers from 1 through N.
2. Pick a random number k between one and the number of unstruck numbers remaining (inclusive).
3. Counting from the low end, strike out the kth number not yet struck out, and write it down elsewhere.
4. Repeat from step 2 until all the numbers have been struck out.
5. The sequence of numbers written down in step 3 is now a random permutation of the original numbers.

Provided that the random numbers picked in step 2 above are truly random and unbiased, so will the resulting permutation be. Fisher and Yates took care to describe how to obtain such random numbers in any desired range from the supplied tables in a manner which avoids any bias. They also suggested the possibility of using a simpler method — picking random numbers from one to N and discarding any duplicates—to generate the first half of the permutation, and only applying the more complex algorithm to the remaining half, where picking a duplicate number would otherwise become frustratingly common.

//To shuffle an array a of n elements (indices 0..n-1):
  for i from n − 1 downto 1 do
       j ← random integer with 0 ≤ j ≤ i
       exchange a[j] and a[i]

####Number Reversal
Given a jumbled list of the numbers 1 to 9 that are definitely not in ascending order, show the list then ask the player how many digits from the left to reverse. Reverse those digits, then ask again, until all the digits end up in ascending order.
The score is the count of the reversals needed to attain the ascending order.
Note: Assume the player's input does not need extra validation.
