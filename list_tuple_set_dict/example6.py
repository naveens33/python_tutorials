# Rotate elements to left by 3 positions

# input [45, 60, 70, 33, 2]
# output [33, 2, 45, 60, 70]

"""
input = [45, 60, 70, 33, 2]
print(input[3:]+input[:3])
"""

input = [45, 60, 70, 33, 2]

for i in range(len(input)-3+1):
    first  = input[0]
    for j in range(len(input)-1):
        input[j] = input[j+1]
    input[len(input)-1] = first
print(input)
