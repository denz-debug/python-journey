class Calculator:
    def myBuild(Self, x: float, y: float, choice: int) -> float:
       match case:
         case 1: return x + y
         case 2: return x - y
         case 3: return x * y
         case 4: return x / y
       raise ValueError
   
   
def showMenu():
       print("WELCOME TO MY CALUCLATOR!")
       print("\n"+"*"* 16)
       print("#1 ADD")
       print("#2 SUB")
       print("#3 MULTIP")
       print("#4 DIVISION")
       print("#5 EXIT")
       print("\n"+"*"* 16)
       
calc.Calculator()

while True:
    Calculator.showMenu()
    
    try: 
        choice = int(input ("Enter the number you want to perform: ").strip())
        if choice not in range (1, 6):
    raise ValueError
        except ValueError
        print("invalid input! please select number from 1-5")
        
        continue
        if choice == 5:
        print ("BYE BYE!!!")
    
       
       