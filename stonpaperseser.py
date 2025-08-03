'''
1 for stone
-1 for paper
0 for seser
'''
import random
computer =  random.choice([1, -1, 0])
youstr=input("Enter your choice: ")
youDict = {'s':1, 'p':-1, 'k':0}
reversDict = {1:'stone', -1:'paper', 0:'seser'}
you=youDict[youstr]
print("You chose: ", reversDict[you])
print("Computer chose: ", reversDict[computer])
if(computer == you):
    print("It's a tie!")
else:
    if(computer == 1 and you == -1):
        print("You win!")
    elif(computer == 1 and you == 0):
        print("You lose!")
    elif(computer == -1 and you == 1):
        print("You lose!")
    elif(computer == -1 and you == 0):
        print("You win!")
    elif(computer == 0 and you == 1):
        print("You win!")
    elif(computer == 0 and you == -1):
        print("You lose!")
    else:
        print("Invalid input!") 