This script is pretty basic, but a way to learn some horrible python practices.

The site wordle is a word based game
https://www.nytimes.com/games/wordle/index.html

The script attempts to evaluate the possible options and allow you to get to the answer...so basically cheat.

# How to Run

1. Download the code
2. Play the first word on the site else the script is going to spit out all 5-letter words
3. Update the script (see below) based on the letters you played.
4. Repeat

# Evaluating the Tiles

## Got a Green!

Congrat you picked well!  In an effort to minimize cycles, add the correct value to the appropriate array: `include1`, `include2`, `include3`, `include4`, `include5`.  This will ensure that the letter is always in that place.
Q: Wait, why is it an array?!  
A: Lazy coding

## Got a Grey!

This means the letter you picked isn't used within the equation, but that also means we can exclude it.  Add the number(s) to the `exclude` array.

## Got a Yellow!

Cool, we are going to add it to two places
1. Add to the poorly named `include` which is going to ensure that all words provided contain that letter.
2. There are 5 excludes (ex. exclude1, exclude2) - add the letter to the correct spot.  This will ensure that a word with that letter in that spot won't be suggested again.



# Example

Lets pretend you played CRANE
C: Green
R: Grey
A: Grey
N: Yellow
E: Grey

Update the script like this
```
# If a letter is flagged as grey, it gets excluded from everything
exclude = ["r","a","e"]
# If a letter is flagged as yellow, it gets included
include = ["n"]

# First Letter
include1 = ["c"] #green
...
exclude4 = ["n"] #yellow
```

Save and re-run the script

It will spit out some extra words -- pick one and try it
```
chink
chino
chins
chunk
cling
clink
clonk
clown
clung
clunk
codon
coins
```

Let's pick CLOWN
C: Green
L: Grey 
O: Grey
W: Grey
N: Yellow

Update the script again
```
exclude = ["r","a","e","l","o","w"]
include = ["n"]

include1 = ["c"] #green
exclude4 = ["n"] #yellow
exclude5 = ["n"] #yellow
```

Save and re-run
```
cinch
<not a nice word :)>
cynic
```

Pick one and give it a shot


Congrat you took a challenge that was suppose to me a mental hurdle and decided to cheat.  Good job.
