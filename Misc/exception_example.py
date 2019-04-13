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

