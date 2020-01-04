def sample(index):
    li = [32, 43, 65]
    try:
        return li[index]
    except IndexError as err:
        print("Sorry you have entered a wrong index.", err)
    except Exception as err:
        print("Something went wrong")
    finally:
        print("Thanks for using our code!!!!")

if __name__=='__main__':
    index = int(input("Enter valid index under 2: "))
    c=sample(index)
    print(c)
'''
try:
    raise IndentationError("This error")
    fo = open("P:\outputfile.txt", "w")
    raise ArithmeticError("something")
except ArithmeticError as err:
    print(err)
except FileNotFoundError as err:
    print(err)
except Exception as err:
    print(err)
finally:
    print("this is finally")
'''

'''if __name__=='__main__':
    try:
        #fo = open("P:\outputfile.txt", "w")
        raise ArithmeticError("something")
    except Exception as err:
        print(err)
    finally:
        print("this is finally")
'''
'''#This statement will raise an error, because fname is not defined:
try:
  print(fname)
except Exception:
  print("Important: " + str(Exception.with_traceback()))
'''
'''
#Many Exceptions
try:
  print(fname)
except Exception:
  print("Important: "+str(Exception.with_traceback()))
except:
  print("Different error")

#Else

try:
  print("Hello, World")
except:
  print("Error")
else:
  print("Nothing went wrong")

#Finally
try:
  print(fname)
except:
  print("Variable fname is not defined/declared")
finally:
  print("The 'try except' is finished")

try:
  fi=open("sdf.txt","r")
except:
  print("File not found")

'''

