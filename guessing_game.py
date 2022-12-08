"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces. 

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""
import random
#Display Intro Message
print("Welcome to Maximilian's guessing game, lets have some fun!")
#Store a random number between 1 and 10
answer= random.randint(1,10)
num_guess=0
guess= int(input("Please choose a number between 1 and 10: ")) 
#Initiate While loop
while guess!= answer:
    num_guess +=1
    #Institute Try Block
    #try:
        #Prompt user for choosen number
    #except ValueError:
        #print("Oops. Looks like you didnt enter a number. Try again!")
    #if guess is to high
    if guess == answer:
        print(f"{answer} was the correct answer. It took you {num_guess} attempt(s)")

    elif guess < answer < 10:
        #print go lower
        print("Looks like you need to go lower")    
        
    else:
        #print go higher
        print("Looks like you need to go higher")
        
print("Thank youfor playing Maximilian's guessing game!")
    