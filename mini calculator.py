def sum(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    return x/y

def power(x,y):
    return x**y

def fmod(x,y):
    return x%y


while True:
   operation=input("use (+,-,*,/,**,%) or 'quit':")
   if (operation=="quit"):
       break
   print(f"You chose: {operation}")

   x=float(input("input first number:"))
   y=float(input("input second number:"))


   match operation:
     case "+":
        print(sum(x,y))

     case   "-":
        print(subtract(x,y)) 

     case "*":
        print(multiply(x,y))

     case "/":
        print(divide(x,y))

     case "**":
        print(power(x,y))

     case "%":
        print(fmod(x,y))

     case _:
        print("⚠️ invalid operator")

