class LessThan50Error(Exception):
    def __init__(self, message):
        self.value = message

li=[54,67,34,98]
for i in li:
    print(i)
    if i < 50:
        raise LessThan50Error(i)


