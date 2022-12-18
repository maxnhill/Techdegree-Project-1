"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces. 

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""
import random
import time

def start_game():
    name=input("What is your name: ")
    print(f"Welcome to Maximilian's guessing game {name}, lets have some fun!")
    time.sleep(2)
    score=[]
    game= True
    while game: 
        answer= random.randint(1,20)
        guess= int()
        num_guess= 0
        while guess != answer:
            num_guess +=1
            try:
                guess=int(input("Please choose a number between 1 and 20: "))
                time.sleep(1)
                          
            except ValueError:
                print("That is not a number. Please try again")
                time.sleep(2)
                continue
                      
            if guess < answer:
                print("Looks like you need to go higher")
                time.sleep(1)   
                
            elif answer < guess < 20:
                print("Looks like you need to go lower")
                time.sleep(1)
                
                
            else:
                print(f"The correct asnwer is {answer}. It took you {num_guess} attempt(s)")
                time.sleep(2)
                print("Thank you for playing Maximilian's guessing game!")
                time.sleep(1)
                score.append(num_guess)
                max_score=min(score)
                
        again= input("Do you want to play again? (Yes/No): ")
        if again.lower()== 'no':
            print("OK bye, thank you for playing my game!") 
            time.sleep(1)
            game= False
        elif again.lower()=='yes':
            print(f"The high score is {max_score} attempt(s). Can you beat it?")
            
start_game()
    
            


        
        
            



                



                
            

        
            
        
    