'''
When a for loop is executed, for statement calls iter() on the object,
which it is supposed to loop over. If this call is successful,
the iter call will return an iterator object that defines the method __next__()
which accesses elements of the object one at a time.
The __next__() method will raise a StopIteration exception,
if there are no further elements available.
The for loop will terminate as soon as it catches a StopIteration exception.
'''

game="Soccer sport"
for ch in game:
    print(ch)

'''
iter() accept only the iterable object. In-case of non iterable object
it will throw TypeError
'''
#game=5
print(iter(game))