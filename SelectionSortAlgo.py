#Sorting Algoroithims or however you spell it
#if this returns an error then you are bad not the code!!


age = [32, 54, 67, 12, 3, 93, 13, 59, 78]
def selection(var):
    print("Before sort: ")
    for i in range(len(var)):
        print(var[i],end=" ") 
    for i in range(len(var)-1):#runs the same as the length of the range
                   minium = i#sets the minium value as the current testing
                   for j in range(i+1, len(var)):# for every value ahead of it until the end it checks to see if infact it is already sorted
                      if var[minium] > var[j]:
                           minium = j# if so then theminium is now j
                   var[i], var[minium] = var[minium], var[i]#in the array they swap the two values over
    print("\nAfter sort: ")
    for i in range(len(var)):
        print(var[i],end=" ") 


action = str(input("Do you want to enter an array or not? if no is selected then a predetermined array will run the code. : "))
inputArray = [] 
if action.lower() == 'no':
    selection(age)
elif action.lower() == 'yes':
    action = int(input("enter the length of your desired array: "))
    for i in range(action):
        number = int(input("Enter number: "))
        print(i)
        inputArray.append(number)
    selection(inputArray)
else:
    print("Why the hell you do this for you pagan")
        

