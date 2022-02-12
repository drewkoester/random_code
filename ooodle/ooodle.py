# SETUP
# Supply the target value
targetNumber = 11
# Set the first, second, and third operator (+, -, *)
operator1 = " + "
operator2 = " * "
operator3 = " - "

# If a number is flagged as grey, it gets excluded from everything
exclude = []

## Below are the potential numbers that can be added/excluded
# If number is green, add it to the include
# OPTIONAL: if something is yellow, feel free to add it to the exlude.  If you don't then track it yourself.


# First Number
include1 = [] #green
exclude1 = [] #yellow

# Second Number
include2 = [1] #green
exclude2 = [] #yellow

# Third Number
include3 = [] #green
exclude3 = [] #yellow

# Fourth Number
include4 = [] #green
exclude4 = [8] #yellow

# Basic Values -- Only change if ranges change
start = 1
# end value should be one higher
end = 13

# Dumb check to exclude items as we can only have a single number once
def safe_check(input1, input2, input3, input4):
  if(input1 == input2): return False
  if(input2 == input3): return False
  if(input3 == input4): return False
  if(input1 == input3): return False
  if(input1 == input4): return False
  if(input2 == input4): return False
  # Check for excludes
  if input1 in exclude1: return False
  if input2 in exclude2: return False
  if input3 in exclude3: return False
  if input4 in exclude4: return False

  return True

def evaluate(input1, input2, input3, input4):
  if safe_check(input1, input2, input3, input4) == False: return
  if (input1 not in include1) and (len(include1) != 0): return
  if input2 not in include2 and len(include2) != 0: return
  if input3 not in include3 and len(include3) != 0: return
  if input4 not in include4 and len(include4) != 0: return

  expression = str(input1) + operator1 + str(input2) + operator2 + str(input3) + operator3 + str(input4)
  value = eval(expression)
  if value == targetNumber:
    print(str(input1) +operator1+ str(input2) + operator2 + str(input3) + operator3 +str(input4))

for a in range(start, end):
  if a in exclude: continue

  for b in range(start,end):
      if b in exclude: continue

      for c in range(start,end):
        if c in exclude: continue

        for d in range(start,end):
          if d in exclude: continue
          evaluate(a,b,c,d)

