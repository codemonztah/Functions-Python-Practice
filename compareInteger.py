def getInput(numberOrder):
  if numberOrder == "first":
    num1=int(input("PLease enter the 1st integer"))
    return num1
  elif numberOrder =="second":
    num2=int(input("PLease enter the 2nd integer"))
    return num2
def findMax(num1,num2):
  if num1>num2:
    print("1st number is bigger")
  elif num2>num1:
    print("2nd number is bigger")
  elif num1==num2:
    print("The 2 numbers are equal")
  
  
num1 =getInput("first")
num2=getInput("second")
findMax(num1,num2)
