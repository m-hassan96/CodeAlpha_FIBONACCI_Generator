
print("\n<< ---------------------------------------- >>")
print("           Welcome to our program") 
print("<< ---------------------------------------- >>\n")
while True:
    num1 = input(f" - Please enter number 1 to generate the sequance: ")
    if num1.isdigit():
        num1 = int(num1)
        break
    print(" << Please enter numbers only >> ")

while True:   
    num2 = input(f" - Please enter number 2 to generate the sequance: ")
    if num2.isdigit():
        num2 = int(num2)
        break
    print(" << Please enter numbers only >> ")

while True:    
    length = input(f" - Please enter the length of your sequance: ")
    if length.isdigit():
        length = int(length)
        break
    print(" << Please enter numbers only >> ")

myList=[num1,num2]
for i in range(length-2): 
    myList.append(myList[i]+myList[i+1])
print("\n<< ---------------------------------------- >>")
print(f" - The Fibonacci series is: ",(myList)) 
print("<< ---------------------------------------- >>\n")