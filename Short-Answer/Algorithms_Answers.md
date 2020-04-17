#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) The running time would be 0(n) because the while loop runs an 'n' number of times. 


b) There are too loops going here. 'n' is having to be calculated twice, so the time doubles? If n is doubling the time to perform doubles. So it would be 0(n log(n))


c) this would be O(n) because it is running ONE time for EACH value of bunnies. 

## Exercise II

I would use binary search for this one (like looking for a name in a phonebook?) Divide the floors in half to get the middle floor. Then drop the egg. If it breaks, then only use the lower half of the floors. Repeat splitting the floors and repeat dropping the egg. 

If it does not break then go to the upper half and drop the egg again. Continue until the egg does not break and the somehow return that floor? (smallest_floor)

Binary search is 0(log n)
