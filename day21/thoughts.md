For part 2, there are too many scenarios to have a list for each one (444356092776315 is too large)

So need to store the counts of the dice...

There are 10*10 = 100 different board scenarios (p1 on 1, p2 on 1,2,3,4,5,6,7,8,9,10 ...)
There are 22*22 = 441 different score scenarios (p1 has 0, p2 has 1,2,3,...21)
So there are 44,100 different universe scenarios

Make a dictionary of the possible scenarios which stores the counts of the universes that are in that situation
4x loop to make the dictionary
Then loop through the dictionary, simulating all the universes until they reach a winning position (and adding their count to the given player) updating the entire dictionary at once to maintain player order

For part 2 do you will roll the quantum die 3 times for each turn?