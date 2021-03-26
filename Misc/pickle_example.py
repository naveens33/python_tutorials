import pickle

class Sample:
    name=""
'''
obj=Sample()
obj.name="Hello"

# Its important to use binary mode
dbfile = open('examplePickle', 'ab')

# source, destination
pickle.dump(obj, dbfile)
dbfile.close()
'''
def loadData():
    # for reading also binary mode is important
    dbfile = open('examplePickle', 'rb')
    db = pickle.load(dbfile)
    '''for keys in db:
        print(keys, '=>', db[keys])
    dbfile.close()'''
    pass
    print(db.name)


if __name__ == '__main__':
    #storeData()
    loadData()