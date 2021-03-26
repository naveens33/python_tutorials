li = [1,2,3]
eval("li."+"append('hello')")
print(li)

command = "insert 0 'world'"
args = ','.join(command.split(' ')[1:])
eval("li."+"insert("+args+")")
print(li)