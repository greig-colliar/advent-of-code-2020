# https://adventofcode.com/2020/day/2 *-Greig Colliar-* #

with open('day-2/input.txt', 'r') as file: # open and read text file then close with 'with' when done
  lines = file.readlines() # Read each line and assign to 'lines'

class password:
  # __init__ function that initalizes/activates properties of the class with self represents the object tht inherits those properties 
  def __init__(self, line): 
    split_line = line.split(' ') # split strings into a list
    self.policy_number_1 = int(split_line[0].split('-')[0]) # split 1st number
    self.policy_number_2 = int(split_line[0].split('-')[1]) # splot 2nd number
    self.letter = split_line[1][:-1]
    self.password = split_line[2]

  def valid_part_1(self):
    occurences = count_occurences(self.letter, self.password)
    return occurences >= self.policy_number_1 and occurences <= self.policy_number_2

  def valid_part_2(self):
    symbol_pos_1 = self.password[self.policy_number_1-1]
    symbol_pos_2 = self.password[self.policy_number_2-1]
    return (symbol_pos_1 == self.letter and symbol_pos_2 != self.letter) or \
           (symbol_pos_1 != self.letter and symbol_pos_2 == self.letter)

def count_occurences(symbol, string):
  count = 0
  for i in range(len(string)):
    if string[i] == symbol:
      count += 1
  return count

## Part 1
passwords = [password(l) for l in lines]
valid_passwords = [p for p in passwords if p.valid_part_1()]
print(len(valid_passwords))

## Part 2
valid_passwords = [p for p in passwords if p.valid_part_2()]
print(len(valid_passwords))  