This script is pretty basic, but a way to learn some horrible python practices.

The site Ooodle is a math based wordle (no clue who was first).
https://mathszone.co.uk/resources/grid/ooodle/

The script attempts to evaluate the possible options and allow you to get to the answer...so basically cheat.

# How to Run

1. Download the code
2. Set the `targetNumber` within ooodle.py.  It can be whatever is the target.
3. Define the 3 operators: `operator1`, `operator2`, `operator3`.  These are the math operators that are used to get to the answer.
4. Verify the `start` and `end` ranges.  For the main game is looks for numbers between 1 and 12.
5. Run the script `python3 ooodle.py`

# Now What

The script will spit out all the possible option, but due to me being lazy it isn't going to remove duplicates.  For example 1 + 2 is the same as 2 + 1, but thankfully the site cares about position so maybe that a feature.
```
1 - 4 * 12 + 5
1 - 5 * 9 + 2
1 - 5 * 10 + 7
1 - 5 * 11 + 12
1 - 6 * 8 + 5
1 - 6 * 9 + 11
```
Pick a line and add it to the site and check your answer

# Got a Green!

Congrat you picked well!  In an effort to minimize cycles, add the correct value to the appropriate array: `include1`, `include2`, `include3`, `include4`.  This will ensure that the number is always in that place.
Q: Wait, why is it an array?!  
A: I have a desire to enable you to put yellow items here to make it easier, but "lazy"

# Got a Grey!

This means the number you picked isn't used within the equation, but that also means we can exclude it.  Add the number(s) to the `exclude` array.

# Got a Yellow!

Yeah, I didn't do anything fancy, but just put that number in another spot.  Don't blame me for being lazy.

# What Next?

Save and re-run the script to get the next options
```
7 - 5 * 12 + 11
8 - 5 * 12 + 10
10 - 5 * 12 + 8
11 - 5 * 12 + 7
```

Rinse and repeat until you get it right.

Congrat you took a challenge that was suppose to me a mental hurdle and decided to cheat.  Good job.
