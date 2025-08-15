#Type conversion i python
'''''''''''''''''''''''''''''''''
a = 12
b = 3.14
c = "Hello"

a = float(a)
b = int (b)
c = str(a)

print (a)
print (b)
print (c)

print(type(a))
print(type(b))
print(type(c))

'''''''''''''''''''''''''''''''''''
#====================================

#import random

#print (random.randrange(1, 10))

#====================================

#Specify variable types
''''''''''''''''''''''''''''''''''''''''
a = int(12)
b = int(3.14)
c = str("Hello Denzel")

print(a)
print(b)
print(c)
'''''''''''''''''''''''''''''''''''''''''



#Strings
"""""""""""""""""""""""
a = "Hello"
b = "Denzul"
print( a,  b )

"""""""""""""""""""""""


#Strings are arrays
""""""""""""""""""""""""
#a = "Hello worlld"
#print (a[3])

""""""""""""""""""""""""

#Loops through string

#for x in "banana":
   # print (x)
   
   
#Check String length
#a = "Hello Denzul"
#print(len(a))


#Check String
#txt = "Python is free for everyone!"
#print("free" in txt)

#txt = "Denzel is pogi or nah?"
#if "pogi" in txt:
    #print ("yes is true!")
#else:
    #print ("no yuck!!!!")
    
    

#Check if NOT in string
#txt = "This rolex is so expensive!"
#if txt not in "expensive":
   # print ("this rolex is local and not expensive!")
#else:
    #print("This fucking rolex is so expensivve")
    
#String Slicing
#b = "Hello, Denzul!"
#print(b[-5:-1])


#Modify Strings
'''''''''''''''''''''''''''''''''''
a = " Hello, World! "
b = "HELLO DENZUL!!"
print(a.lower())

a = " Hello, World! "
b = "HELLO DENZUL!!"
print(a.upper())

a = " Hello, World! "
b = "HELLO DENZUL!!"
print(a.strip())

a = " Hello, World! "
b = "HELLO DENZUL!!"
print(a.replace("H", "J"))

a = " Hello, World! "
b = "HELLO DENZUL!!"
print(b.split( "," ))

'''''''''''''''''''''''''''''''''''
#Concatemate strngs
#a = "Hello"kukuku
#b = "Denzul"
#c = a + " " + b

#print(c)

#format strings (f)
#age = 36
#txt = f"My name is Denzul and my age is {age}"
#print (txt)

#price = 578
#txt = f"The price of this item is {price}"

#print(txt)

#price = 59
#txt = f"The price is {price:.2f} dollars"

#print(txt)

#txt = f"The price is {20 * 59} dollars"
#print(txt)

# Crude way to find even numbers
#numbers = [1, 2, 3, 4, 5]
#evens = []
#for num in numbers:
    #if num % 1 == 0:
       # evens.append(num)
#print(evens)  # [2, 4]
