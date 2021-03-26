# Input [[1 ,2, 3], [4, 5, 6], [7, 8, 9]]
# Output: [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
l=[[1 ,2, 3], [4, 5, 6], [7, 8, 9]]

print([[row[i] for row in l]for i in range(len(l))])

print(list(zip(l[0],l[1],l[2])))
