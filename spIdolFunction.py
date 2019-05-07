spIdol=[[1,1000],[2,800],[3,700],[4,300],[5,300],["Others",20]]

def getInput():
  	
    userInput=input("Enter the rank of the contestant")
    if userInput.isdigit():
    	return int(userInput)
    elif userInput.lower()=="others":
    	return userInput.lower()
    else:
      print("Incorrect entry")


def printPrize():
    for i in range(len(spIdol)):
      if rank=="others":
        print(spIdol[-1][1])
        break
      elif rank ==i:
        print(spIdol[i-1][1])
	
rank=getInput()
print(printPrize())



