"""
A brute force solution to Xenophage quest
"""
import random

# Symbols are coded as the most similar letters, namely X, E, V, A
# Shooting a symbol converts it from one shape (letter) to another
trans_dict = {
  'X': 'E', 
  'E': 'V',
  'V': 'A',
  'A': 'X'
}

# These are the target symbols, not used in the code, added for reference
k1_logistics = {'A': 'EEEAEEEEE'}
k1_crew = {'E': 'AXVAXXAAA'}
k1_revelation = {'X': 'EAVVXVEAV'}
k1_communion = {'V': 'AXAEXEXVX'}

""" 
Shooting one symbol in the 3x3 matrix changes other symbols in the same row and column
The matrix below keeps track of these changes, each entry refers to the symbol being shot
Symbols start at 1 (top left) and increase by 1 from left to right and top to bottom, up to 9 (bottom right)
For example: shooting the first symbol (the 1st list in the matrix below) will change 
symbols in locations 1, 2, 3, 4 and 7
"""
conversion_matrix = [
  [1, 2, 3, 4, 7],
  [1, 2, 3, 5, 8],
  [1, 2, 3, 6, 9],
  [1, 4, 5, 6, 7],
  [2, 4, 5, 6, 8],
  [3, 4, 5, 6, 9],
  [1, 4, 7, 8, 9],
  [2, 5, 7, 8, 9],
  [3, 6, 7, 8, 9]
]

# Start the simulation

MAX_STEPS = 10000 # simulate this many random shots
ITERATIONS = 1000 # run the simulation this many times
TARGET = ['X']*9 # the target symbol(letter) we want

"""
Shooting the same symbol 4 times, regardless of the order, brings the board to a previous state
So in the worst case scenario we have to shoot each symbol 3 times to find the solution, i.e. 9X3
"""
optimal = 27 # set the optimal to the worst initially
optimal_shots = []
for i in range(ITERATIONS):
  steps = 1
  shooted = []
  current = ['E', 'A', 'V', 'V', 'X', 'V', 'E', 'A', 'V']
  while current != TARGET and steps < MAX_STEPS:
    selection = random.randint(1, 9)
    shooted.append(selection)
    changed = conversion_matrix[selection - 1]
    for number in changed:
      current[number - 1] = trans_dict[current[number - 1]]
    steps += 1
  shots = [[x, shooted.count(x)%4] for x in set(shooted)]
  num_shots = sum([x[1] for x in shots])
  if current == TARGET and num_shots < optimal:
    optimal = num_shots
    optimal_shots = shots
    print(optimal, optimal_shots)
