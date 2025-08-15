#defining the data  type
#x = 5
#y = "john pogi"
#print (type(x))
#print (type(y))

#ASSIGN MULTIPLE VALUES
# -----------------------------------------------------------------
#Many values to multiple variables
#x, y, z, w, t=  "Orange", "Banana", "Cherry", "Grapes", "Apple"
#print (x)
#print (y)
#print (z)
#print (w)
#print (t)

#Assign same value in multiple variables in one line
#x = y = z = "Orange"
#print (x)
#print (y)
#print (z)

#Unpack a collection
#fruits = ["Orange", "Apple", "Avocado"]
#x, y, z, =  fruits
#print (x)
#print (y)
#print (z)
# -----------------------------------------------------------------

#OUTPUT VARIABLES
# -----------------------------------------------------------------

#x = "Python is Awesome!"
#print (x)

#x = "Python"
#y = "is"
#z = "Awesome"

#print (x, y ,z)

#x = "Python "
#y = "is "
#z = "awesome"
#print(x + y + z)

#x = 55
#y = 45
#print (x + y)

#if  you want to print str
#x = 4
#y = "Allvey"
#print (x, y)
# -----------------------------------------------------------------

#GLOBAL VARIABLES
# -----------------------------------------------------------------

#Create a variable outside of a function, and use it inside the function

#x = "deadass"

#def myfunc():
    #print ("Python is " + x)

#myfunc()

#Create a variable inside a function, with the same name as the global variable
#x = "patay na tumbong"

#def myfunc():
    #x = "depressing language"
    #print ("python is " + x)
#myfunc()
#print ("python is " + x)

#If you use the global keyword, the variable belongs to the global scope:
#def myfunc():
 #global x
 #x = "migga ain't shit"

#myfunc()

#print ("python is " + x)

#To change the value of a global variable inside a function, refer to the variable by using the global keyword:
#x = "awesome"
#def myfunc():
 #global x
 #x = "migga ain't shit"

#myfunc()

#print ("python is " + x)

#PYTHON DATA TYPE"
'''
Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType

'''
