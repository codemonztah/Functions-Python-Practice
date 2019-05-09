def readYear():
  year=int(input("Enter the year you wish to check if it is a leap year"))
  return year

year=readYear()

def isLeapYear(year):
  if (year%4==0 and year%100!=0) or year%400==0:
  	return True
  else:
    return False
  
output=isLeapYear(year)

if output==True:
  print("LEAP YEAR")
elif output== False:
  print("NOT A LEAP YEAR")
