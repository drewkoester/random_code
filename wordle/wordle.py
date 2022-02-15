import enchant
from string import ascii_lowercase


dictionary = enchant.Dict("en_US") 

# If a letter is flagged as grey, it gets excluded from everything
exclude = []
# If a letter is flagged as yellow, it gets included
include = []

# If letter is green, add it to the include
# OPTIONAL: if something is yellow, feel free to add it to the exlude.  If you don't then track it yourself.
# First Letter
include1 = [] #green
exclude1 = [] #yellow

# # Second Letter
include2 = [] #green
exclude2 = [] #yellow

# # Third Letter
include3 = [] #green
exclude3 = [] #yellow

# # Fourth Letter
include4 = [] #green
exclude4 = [] #yellow

# # Fifth Letter
include5 = [] #green
exclude5 = [] #yellow

# Dumb check to exclude items as we can only have a single number once
def safe_check(input1, input2, input3, input4, input5):
  # Check for excludes
  if input1 in exclude1: return False
  if input2 in exclude2: return False
  if input3 in exclude3: return False
  if input4 in exclude4: return False
  if input5 in exclude5: return False

  if len(include) != 0:
    if input1 not in include and input2 not in include and input3 not in include and input4 not in include and input5 not in include: return False

  return True

def evaluate(dictionary, input1, input2, input3, input4, input5):
  tmpWord = input1 + input2 + input3 + input4 + input5
  
  if safe_check(input1, input2, input3, input4,input5) == False: return
  if input1 not in include1 and len(include1) != 0: return
  if input2 not in include2 and len(include2) != 0: return
  if input3 not in include3 and len(include3) != 0: return
  if input4 not in include4 and len(include4) != 0: return
  if input5 not in include5 and len(include5) != 0: return

  if dictionary.check(tmpWord) == True:
    print(tmpWord)

for a in ascii_lowercase:
  if a in exclude: continue

  for b in ascii_lowercase:
      if b in exclude: continue

      for c in ascii_lowercase:
        if c in exclude: continue

        for d in ascii_lowercase:
          if d in exclude: continue

          for e in ascii_lowercase:
            if e in exclude: continue
            evaluate(dictionary, a,b,c,d,e)
            # print(maxResults)

