# https://adventofcode.com/2020/day/1 *-Greig Colliar-* #

with open('day-1/input-1.txt', 'r') as file: # open and read text file then close with 'with' when done
  lines = file.readlines() # Read each line and assign to 'lines'

expenses = [int(line) for line in lines] # iterate through each line and convert to int 


def find_two_expenses_with_sum(expenses, sum): # function and 2 paras
  for i in range(len(expenses)): # traverse through all array elements
    exp1 = expenses[i] #assign [list] to new variable
    for j in range(i, len(expenses)): # traverse through list in expenses
      if i == j: # if i matches/equal to j
        continue # return
      exp2 = expenses[j] # list result of j assign to exp2
      if exp1 + exp2 == sum: # if 1 + 2 is equal to the sum
        return exp1 * exp2 # return the amount by multiplication

found = find_two_expenses_with_sum(expenses, 2020) #assign function and parameters to found
print(found) #output: 485739

def find_three_expenses_with_sum(expenses, sum):
  for i in range(len(expenses)):
    exp1 = expenses[i]
    for j in range(len(expenses)):
      exp2 = expenses[j]
      for k in range(len(expenses)):
        exp3 = expenses[k]
        if i == j == k:
          continue
        if exp1 + exp2 + exp3 == sum:
          return exp1 * exp2 * exp3

found = find_three_expenses_with_sum(expenses, 2020) #assign function and parameters to found
print(found) #output: 161109702 