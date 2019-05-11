def getFahrenheit():
  userInput=int(input("Enter your temperature in Fahrenheit"))
  return userInput

def getResultCelcius(fahrenheit):
  print(5/9*(fahrenheit-32))

fahrenheit=getFahrenheit()


getResultCelcius(fahrenheit)